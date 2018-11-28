#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>

using namespace std;

const long long maxqn = 10000000;
const long long move[4][2]={{-1,0},{0,1},{1,0},{0,-1}};

long long final, init;

char board[15][15];
bool des[15][15];

long long q[maxqn];
long long step[maxqn];
long long mul[10];

map<long long, int> hash;

long long bn;
long long n, m;
long long ax[10], ay[10], b[10];

int testdanger()
{
	long long i, k, x, y, head, tail;
	long long q[10];
	if (bn==1) return 1;
	
	head=tail=0;
	bool f[10]={false};
	q[head]=0;
	f[0]=true;
	while (head<=tail)
	{
		for (i=0; i<bn; i++)
		  if (!f[i])
		    if ( abs(ax[i]-ax[q[head]])+abs(ay[i]-ay[q[head]])==1)
		    {
		    	f[i]=true;
		    	q[++tail]=i;
		    	if (tail==bn-1) return 1;
		    }
    	head++;
	}
	return 2;
}

long long BFS(long long init)
{
	if (init==final) return 0;
	long long head, tail, i, j, k, x, y;
	long long sta, temp;
	int danger, newdanger;
	bool canmove;
	memset(step, 0, sizeof(step));
	head=tail=0;
	q[head]=init;
	hash.clear();
	hash[init]=1;
	while (head<=tail)
	{
		sta=q[head];
		danger=hash[sta];
		for (i=0; i<bn; i++)
		{
			temp=sta%(n*m);
			sta/=n*m;
			ax[i]=temp/m;
			ay[i]=temp%m;
			board[ax[i]][ay[i]]='o';
		}
		for (i=0; i<bn; i++)
		{
			
		  canmove=true;
		  long long last=100;
		  for (k=0; k<4; k++)
		  {
		  	x=ax[i]+move[k][0];
		  	y=ay[i]+move[k][1];
		  	if(!(x>=0 && x<n && y>=0 && y<m) || board[x][y]=='#')
		  	{
		  		if (last==k-1) {
				  	canmove=false; 
					  break;
					  }
		  		last=k;
		  	}
		  }
		  
		  if (!canmove && !des[ax[i] ][ ay[i] ]) 
		  	break;
		  	
		  for (k=0; k<4; k++)
		  {
		  	x=ax[i]+move[k][0];
		  	y=ay[i]+move[k][1];
		  	if( !(x>=0 && x<n && y>=0 && y<m && board[x][y]=='.') ) continue;
		  	x=ax[i]-move[k][0];
		  	y=ay[i]-move[k][1];
		  	if( !(x>=0 && x<n && y>=0 && y<m && board[x][y]=='.') ) continue;
		  	canmove=true;
		  	swap(board[ ax[i] ][ ay[i] ], board[x][y]);
		  	long long tx, ty;
		  	tx=ax[i]; ty=ay[i];
		  	ax[i]=x; ay[i]=y;
		  	newdanger=testdanger();
			if (!(danger==2 && newdanger==2))
			{
				for (j=0; j<bn; j++)
				  b[j]=ax[j]*m+ay[j];
				sort(b, b+bn);
				sta=0;
				for (j=0; j<bn; j++)
				  sta += (long long)b[j]*mul[j];  
				if (hash[sta]==0) 
				{
					hash[sta]=newdanger;
					q[++tail]=sta;
					step[tail]=step[head]+1;
					if (sta==final) 
					return step[tail];
				}
			}
		  	ax[i]=tx; ay[i]=ty;			
		  	swap(board[ ax[i] ][ ay[i] ], board[x][y]);		  	
		  }
		}
		for (i=0; i<bn; i++)
		  board[ax[i]][ay[i]]='.';
		head++;  
	}
//	printf("%d %d\n", head, tail);
	return -1;
}

int main()
{
	
	long long cas=0, T, i, j, k;
	freopen("al.txt", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%I64d", &T);
while (T--)
{
	scanf("%I64d%I64d", &n, &m);
	mul[0]=1;
	final=0;
	bn=0;
	for (i=0; i<n; i++)
	  scanf("%s", board[i]);
	memset(des, false, sizeof(des));  
	for (i=0; i<n; i++)
	 for (j=0; j<m; j++)
	 {
	  if (board[i][j]=='x' || board[i][j]=='w')  
	  {
	  	des[i][j]=true;
	  	final+=mul[bn]*(long long)(i*m+j);
	  	bn++;
	  	mul[bn]=mul[bn-1]*(long long)n*m;
	  }
	 }
	init=0;  
	k=0;
	for (i=0; i<n; i++)
	 for (j=0; j<m; j++)
	  if (board[i][j]=='o' || board[i][j]=='w')
	    init+=(long long)(i*m+j)*mul[k++];
	for (i=0; i<n; i++)
	 for (j=0; j<m; j++)
	   if (board[i][j]!='.' && board[i][j]!='#')
	     board[i][j]='.';
	if (cas==6)
	{
		cas++;
		cas--;
	}
	printf("Case #%I64d: %I64d\n", ++cas, BFS(init));
}
	return 0;
}

