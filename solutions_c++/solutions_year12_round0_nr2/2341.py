#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <bitset>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define forall(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dforn(i,n) for(int i=((int)(n)-1);i>=0;i--)
#define dforsn(i,s,n) for(int i=((int)(n)-1);i>=(int)(n);i--)
#define esta(i,c) ((c).find(i) != (c).end())
#define dbg(x) cerr << #x << " = " << x << endl;
#define raya cerr << string('=',80) << endl;

typedef long long tint;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< pair<int,int> > vii;

inline int iabs(int x){ return (x < 0) ? -x : x; }

inline bool checkNoSurpriseTriple(int a, int b, int c){
	return iabs(a-b) < 2 && iabs(b-c) < 2 && iabs(c-a) < 2;
}

bool checkSurpriseTriple(int a, int b, int c){
	int check[] = {a,b,c};
	forn(i,3){
		int j = (i+1)%3, k = (i+2)%3;
		int x = check[i], y = check[j], z = check[k];
		if(iabs(x-y) == 2 && iabs(x-z) <= 2 && iabs(z-y) <= 2){
			return true;
		}
	}
	return false;
}
int main(){
	#ifdef JUAMPI
		freopen("DancingWithTheGooglers.in","r",stdin);
		freopen("DancingWithTheGooglers.out","w",stdout);
	#endif

	int n,t,s,p;
	
	scanf("%d",&t);
	forn(tt,t){
		vector<int> scores; 
		scanf("%d%d%d",&n,&s,&p);

		forn(i,n){
			int a; scanf("%d",&a);
			scores.push_back(a);
		}
		
		int res = 0, surpr = 0;
		forn(i,n){
			bool possible = false;
			forn(x,max(11,scores[i]+1))
			forn(y,max(11,scores[i]+1-x))
			{
				int z = scores[i]-x-y; 
				if(z < 0 || z > 10) continue;

				if(checkNoSurpriseTriple(x,y,z) && max(x,max(y,z)) >= p){					
					res++; 
					possible = true;
					goto fin;
				}
			}
			
			fin: ;
			if(!possible && surpr < s){
				forn(x,max(11,scores[i]+1))
				forn(y,max(11,scores[i]+1-x))
				{
					int z = scores[i]-x-y; 
					if(z < 0 || z > 10) continue;
					
					if(checkSurpriseTriple(x,y,z) && max(x,max(y,z)) >= p){
						res++; 
						surpr++;
						goto found;
					}
				}
				found:;
			}
		}
		printf("Case #%d: %d\n",tt+1,res);
	}
	
	return 0;
}
