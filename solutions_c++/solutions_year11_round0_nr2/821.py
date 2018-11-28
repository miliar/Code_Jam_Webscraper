#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;

typedef pair<int,int> pii;
typedef long long LL;

const int MAXN = 1001;

int C[30][30];
bool OP[30][30];
char S[105];
int main()
{
	int o,q;
	scanf("%d",&o);
	fru(oo,o)
	{
		 printf("Case #%d: ",oo+1);
		 fru(i,30)fru(j,30) 
		 {
			 OP[i][j]=0;
			 C[i][j]=-1;
		 }
		 scanf("%d",&q);
		 char a,b,c;
		 fru(i,q)
		 {
			 scanf(" %c%c%c",&a,&b,&c);
			 a-='A'; b-='A';c-='A';
			 C[a][b]=c;
			 C[b][a]=c;
		 }
		 scanf("%d",&q); fru(i,q)
		 {
			 scanf(" %c%c",&a,&b);
			 a-='A';b-='A';
			 OP[a][b]=1;
			 OP[b][a]=1;
		 }
		 list<int> L;
		 L.clear();
		 scanf("%d %s",&q,S);
		 fru(i,q)
		 {
			 char e=S[i]-'A';
			 if(L.empty()) 
			 {
				 L.push_back(e);
				 continue;
			 }
		 	if(C[L.back()][e]!=-1)
			{
				e=C[L.back()][e];
				L.pop_back();
				L.push_back(e);
			}
			else
			{
				bool ok=1;
				tr(it,L) if(OP[*it][e]) ok=0;
				if(!ok) L.clear();
				else L.push_back(e);
			}
		 }
		printf("["); 
		tr(it,L)
		{
			if(it!=L.begin()) printf(", ");
			printf("%c",*it+'A');
		}
		printf("]\n");
	}
    return 0;
}
