#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;
#define foreach(c,itr) for (__typeof( (c).begin() ) itr=(c).begin();itr!=(c).end() ;itr++ )


int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}
int Rand16(){return rand();}
int Rand32(){return rand()*rand();}
double DRand(){return (double)rand()/RAND_MAX;}
int RandRange(int f,int r){return f+(int)(DRand()*(r-f)+0.5);}

#define mp make_pair

int n,m,t;
int ans;

struct Node
{
	string  na;
	map<string,int>lookup;
};

vector<Node>tree;
vector<string>pa;

bool cmp(string a,string b)
{
	if (a.size()!=b.size()) return a.size()<b.size();
	return a<b;
}

vector<string> split(string path)
{
	path+='/';
	int n=path.size();
	int beg=1;
	int i;
	vector<string> ret;
	for (i=1;i<n;i++)
	{
		if (path[i]=='/')
		{
			ret.push_back(path.substr(beg,i-beg));
			beg=i+1;
		}
	}
	return ret;
}

int main()
{
	int cas=0;
	int i,j;
	string path;
	Node tmp;

	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);
	while (t--)
	{
		cas++;
		scanf("%d%d",&n,&m);
		pa.clear();
		ans=0;

		for (i=0;i<n;i++)
		{
			cin>>path;
			pa.push_back(path);
		}

		sort(pa.begin(),pa.end(),cmp);

		tree.resize(1);
		tree[0].lookup.clear();

		for (i=0;i<n;i++)
		{
			vector<string> cp=split(pa[i]);			
		//	for (j=0;j<cp.size();j++)
		//		printf("%s ",cp[j].c_str());
		//	putchar('\n');
			int sta=0;
			for (j=0;j<cp.size();j++)
			{
				if (tree[sta].lookup.find(cp[j])==tree[sta].lookup.end())
				{
					tmp.na=cp[j];
					tmp.lookup.clear();
					tree.push_back(tmp);
					tree[sta].lookup[cp[j]]=tree.size()-1;
				}
				sta=tree[sta].lookup[cp[j]];
			}		
		}

		for (i=0;i<m;i++)
		{
			cin>>path;
			vector<string> cp=split(path);			
		//	for (j=0;j<cp.size();j++)
		//		printf("%s ",cp[j].c_str());
		//	putchar('\n');
			int sta=0;
			for (j=0;j<cp.size();j++)
			{
				if (tree[sta].lookup.find(cp[j])==tree[sta].lookup.end())
				{
					tmp.na=cp[j];
					tmp.lookup.clear();
					tree.push_back(tmp);
					tree[sta].lookup[cp[j]]=tree.size()-1;
					ans++;
				}
				sta=tree[sta].lookup[cp[j]];
			}		
		}
		printf("Case #%d: %d\n",cas,ans);		
	}
	return 0;
}
