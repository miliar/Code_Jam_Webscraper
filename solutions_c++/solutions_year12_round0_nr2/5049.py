
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>

using namespace std;

#define db(x) cout << #x " == " << x << endl
#define _ << ", " <<
#define Fr(a,b,c) for( int a = b ; a < c ; ++a )
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
#define F first
#define S second
#define MP make_pair
#define PB push_back

int t, n, s, p, dv, mod, tmp, res;

int main(){
	scanf("%d",&t);
	Fr(cas,1,t+1){
		scanf("%d%d%d",&n,&s,&p);
		res=0;
		Fr(j,0,n){
			scanf("%d",&tmp);
			dv = tmp/3;
			mod = tmp%3;
			if(dv<p){
		//		printf("%d %d\n",dv,mod);
				if(mod == 0){
					if(s && (p-dv)==1 && dv>0){
	//					printf("(%d %d %d)\n",dv-1,dv,dv+1);
						--s;
						++res;
					}
				} else if(mod == 1){
					if((p-dv)==1){
	//					printf("(%d %d %d)\n",dv,dv,dv+1);
						++res;
					}
				} else {
					if((p-dv)==1){
	//					printf("(%d %d %d)\n",dv,dv+1,dv+1);
						++res;
					} else if(s && (p-dv)==2 && dv>0){
	//					printf("(%d %d %d)\n",dv-1,dv,dv+1);
						++res;
						--s;
					}
				}
			} else {
	//			printf("(%d %d %d)\n",dv,dv,dv);
				++res;
			}
		}
		printf("Case #%d: %d\n",cas,res);
	}
	return 0;
}