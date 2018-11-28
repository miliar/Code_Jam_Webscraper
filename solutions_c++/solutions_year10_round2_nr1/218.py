#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000


//typedef long long LL;


map<string,int> S;
map<int,int> all[100005];
vs name;
int tot,nnew;
vs A[102],B[102];

void visit(int node,int x)
{
	int i,j;

	if(x==name.size()) return ;	
	int a=S[name[x]];


	//printf("%d %s\n",node,name[x].c_str());

	if(all[node].find(a)==all[node].end())
	{
		//printf("%d\n",x);
		int sz=name.size();
		nnew=sz-x;

		int now=node;

		for(j=x;j<sz;j++)
		{
			int id=S[name[j]];
		//	printf("%s\n",name[j].c_str());
		//	printf("%s %d %d\n",name[j].c_str(),id,j);
			all[now][id]=++tot;
			now=tot;
			all[tot].clear();
		}
		return ;
	}

	visit(all[node][a],x+1);
}

char str[100004];

int main()
{
	int i,j,k,l,tests,cs=0,n,m;
	

//	freopen("A-large.in","r",stdin);
	freopen("Alarge.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d%d",&n,&m);
		S.clear();
		all[0].clear();

		int cnt=0;
		int ans=0;


		tot=0;

		for(i=0;i<n;i++)
		{
			scanf("%s",str);

			for(j=0;str[j];j++)
				if(str[j]=='/') str[j]=' ';

			istringstream sin(str);
			string s;
			name.clear();

			while(sin>>s)
			{
				if(S.find(s)==S.end()) S[s]=cnt++;
				name.push_back(s);
			}
			visit(0,0);
		}

		
		for(i=0;i<m;i++)
		{
			scanf("%s",str);

			for(j=0;str[j];j++)
				if(str[j]=='/') str[j]=' ';

			istringstream sin(str);
			string s;
			name.clear();


			while(sin>>s)
			{
				if(S.find(s)==S.end()) S[s]=cnt++;
				name.push_back(s);
			}

			nnew=0;
			visit(0,0);
			ans+=nnew;
		}

	
		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 


