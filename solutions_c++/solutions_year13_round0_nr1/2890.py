/*Author : Vineet Kumar */
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stack>
#include<queue>
#include<fstream>
using namespace std;
 
#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))
#define max(a,b)	((a)>(b)?(a):(b))
#define min(a,b)	((a)<(b)?(a):(b))
#define	si(n)		scanf("%d",&n)
#define pi(n)		printf("%d ",n)
#define pil(n)		printf("%d\n",n)
#define ps(n)		printf("%s",n)
#define psl(n)		printf("%s\n",n)
#define sl(n)		scanf("%lld",&n)
#define sd(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define scan_in(v,n)	vector<int> v;rep(i,n){ int j;in>>j;v.pb(j);}
#define scan_in_s(v,n)	vector<string> v;rep(i,n){ string j;in>>j;v.pb(j);}
#define mod (int)(1e9 + 7)
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int main()
{
	int N;
	
	ifstream in("TTT.txt");
	ofstream out("TTT_out.txt");
	
	char str[10];
	in.getline(str,10);
	N = atoi(str);
	vector<string> s;
	char c[4][4] = {{'.','.','.','.'},{'.','.','.','.'},{'.','.','.','.'},{'.','.','.','.'}};
	int r = N;

	while(N--)
	{
		string status = "Game has not completed";
		rep(i,4)
		{
			in.getline(str,10);
			rep(j,4)
			{
				c[i][j] = str[j];
				//cout<<c[i][j];
				
			}
			//cout<<endl;
		}
		int v=0;
		rep(i,4)
		{
			
			rep(j,4)
			{
				if(c[i][j]!='.')v++;	
			}
		}
		if(v==16)status = "Draw";
		
		bool proceed = true;
		rep(i,4)
		{
			int k=0;
			rep(j,4)
			{
				if(c[i][j]=='X'||c[i][j]=='T')k++;	
			}
			if(k==4)
			{
				proceed = false;
				status = "X won";
				break;
				
			}
		}
		
		if(proceed==true)
		{
			rep(i,4)
			{
				int k=0;
				rep(j,4)
				{
					if(c[j][i]=='X'||c[j][i]=='T')k++;	
				}
				if(k==4)
				{
					proceed = false;
					status = "X won";
					break;
					
				}
			}
		}
		if(proceed==true)
		{
			
				int k=0;
				rep(j,4)
				{
					if(c[j][j]=='X'||c[j][j]=='T')k++;	
				}
				if(k==4)
				{
					proceed = false;
					status = "X won";
					
				}
		}
		if(proceed==true)
		{
			
				int k=0;
				rep(j,4)
				{
					if(c[j][3-j]=='X'||c[j][3-j]=='T')k++;	
				}
				if(k==4)
				{
					proceed = false;
					status = "X won";
					
				}
		}
		if(proceed==true)
		{
			rep(i,4)
			{
				int k=0;
				rep(j,4)
				{
					if(c[i][j]=='O'||c[i][j]=='T')k++;	
				}
				if(k==4)
				{
					proceed = false;
					status = "O won";
					break;
					
				}
			}
		}
		if(proceed==true)
		{
			rep(i,4)
			{
				int k=0;
				rep(j,4)
				{
					if(c[j][i]=='O'||c[j][i]=='T')k++;	
				}
				if(k==4)
				{
					proceed = false;
					status = "O won";
					break;
					
				}
			}
		}
		if(proceed==true)
		{
			
				int k=0;
				rep(j,4)
				{
					if(c[j][j]=='O'||c[j][j]=='T')k++;	
				}
				if(k==4)
				{
					proceed = false;
					status = "O won";
					
				}
		}
		if(proceed==true)
		{
			
				int k=0;
				rep(j,4)
				{
					if(c[j][3-j]=='O'||c[j][3-j]=='T')k++;	
				}
				if(k==4)
				{
					proceed = false;
					status = "O won";
					
				}
		}
		
		
		in.getline(str,10);
		//output init..
		char buffer[50];
		sprintf(buffer,"Case #%d: ",r-N);
		out<<buffer;
		//output
		out<<status<<endl;
	}
	
	in.close();
	out.close();
	return 0;
}

