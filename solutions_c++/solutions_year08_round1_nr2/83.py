#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

const int max_n=2*1000+218;

int n,m;
vi z[max_n];
int o[max_n];
int ans[max_n];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tn;
	cin>>tn;
	
	for (int tst=0; tst<tn; tst++) {
		fprintf(stderr,"Case #%d: ",tst+1);
		printf("Case #%d: ",tst+1);
		cin>>n>>m;
		for (int i=0; i<m; i++) {
			int cnt;
			cin>>cnt;
			z[i].clear();
			o[i]=-1;
			for (int j=0; j<cnt; j++) {
				int tmp,type;
				cin>>tmp>>type;
				tmp--;
				if (type==0)
					z[i].pb(tmp);
				else
					o[i]=tmp;
			}
		}
		memset(ans,0,sizeof(ans));
		bool ok=true;
		for (;;) {
			if (!ok) break;
			int I=-1;
			for (int i=0; i<m; i++) {
				bool cov=false;
				if (o[i]!=-1) 
					if (ans[o[i]]==1) {
						cov=true;
						continue;
					}
				for (int j=0; j<sz(z[i]); j++)
					if (ans[z[i][j]]==0) {
						cov=true;
						break;
					}
				if (!cov) {
					I=i;
					break;
				}
			}
			if (I==-1) break;
			if (o[I]==-1) {
				ok=false;
				break;
			}
			if (ans[o[I]]==1) {
				ok=false;
				break;
			}
			ans[o[I]]=1;
		}
		if (!ok)
			cout<<"IMPOSSIBLE\n";
		else {
			for (int i=0; i<n; i++) 
				cout<<ans[i]<<" ";
			cout<<endl;
		}
	}

	return 0;
}
