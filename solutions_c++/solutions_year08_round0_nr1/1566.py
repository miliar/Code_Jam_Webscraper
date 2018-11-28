#include <iostream>
#include <string>

using namespace std;

const int M=300001;
const int maxn=100;
const int INF=20000000;

struct Node {
	char str[101];
	int c;
	Node* next;
};

Node* hash[M];
int n,m;
char se[maxn][101];
char query[101];
int q[1001];
int d[1001][101];
int ans;
string sa,sb,cbClass;

int ELFhash(char* key)
{
	unsigned long h=0,g;
	int i;
	i = 0;
	while(key[i])
	{
		h = (h << 4) + key[i];
		g = h & 0xf0000000L;
		if(g) h^= g>>24;
		h &= ~g;
		i++;
	}
	return h%M;
}

void InsertToHash(int s,char* str,int i)
{
	Node* pnode = new Node;  
	strcpy(pnode->str, str);  pnode->c = i;
	pnode->next = hash[s];
	hash[s] = pnode;
}

void Init()
{
	int i;
	for(i=0;i<M;i++) 
        hash[i] = NULL;
}

void Dp()
{
	int i,j,min,k;
	for(i=0;i<n;i++)  d[m][i] = 0;

	for(i=m-1;i>=0;i--)  {
		for(j=0;j<n;j++)  {
			min = INF;
			if(q[i]==j)  {
				for(k=0;k<n;k++)
					if(q[i]!=k)  {
						if(min>d[i+1][k]+1)  min = d[i+1][k] + 1;
					}
			}
			else if(d[i+1][j]<min)  min = d[i+1][j];
			d[i][j] = min;
		}
	}
	ans = INF;
	for(i=0;i<n;i++)
		if(ans>d[0][i])
			ans = d[0][i];
}

int main()
{
	int kase;
	int i,j,s,k;
	bool flag;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>kase;
	for(i=1;i<=kase;i++)  {
		Init();
		cin>>n;  cin.getline( query, 101, '\n' );
		for(j=0;j<n;j++)  {
			cin.getline( se[j], 100, '\n' ); 
			s = ELFhash(se[j]);
			InsertToHash(s,se[j],j);
			//cout<<se[j]<<endl;
		}
		cin>>m;   cin.getline( query, 100, '\n' );
		//cout<<"m:"<<m<<endl;
		for(j=0;j<m;j++)  {
			cin.getline( query, 100, '\n' );
			s = ELFhash(query);
			//cout<<j<<"qs:"<<s<<endl;
			Node* hp = hash[s];
			
			while(hp!=NULL) {
				if( strcmp(hp->str, query)==0 ) {  q[j] = hp->c;  break;  }		
				hp = hp->next;
			}//while
		}//for

		Dp();

		cout<<"Case #"<<i<<": "<<ans<<endl;		
	}
	fclose(stdin);
	fclose(stdout);
	//system("PAUSE");

	return 0;
}