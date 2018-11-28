#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#define FWD(a,b,c) for(int a=(b); a<(c); a++)
#define BCK(a,b,c) for(int a=(b); a>(c); a--)
#define FE(a,b) for(typeof(b.end()) a=b.begin(); a!=b.end(); a++)
#define ALL(a) a.begin(), a.end()
#define RINT(a) scanf("%d", &a)
#define RCH(a) scanf("%c", &a)
#define RLL(a) scanf("%lld", &a)
#define RSTR(a) scanf("%s", a)
#define UNIQUE(a) erase(unique(a.begin(), a.end()), a.end())
#define ULL unsigned long long
#define PII pair<int, int>
#define PACKS(a) int a; scanf("%d", &a); a++; while(--a)

//#define DEBUG
#ifdef DEBUG
	#define debug printf
#else
	#define debug
#endif

using namespace std;

int k, mk;
int D[220][220];
int minc, c, d, e;

inline bool in(int x, int y){
	return 0<=x && x<220 && 0<=y && y<220;
}

int main(){
	int z;
	scanf("%d", &z);
	z++;
	FWD(q,1,z){
		scanf("%d", &k);
		FWD(i,0,220)
			FWD(j,0,220)
				D[i][j]=-1;
		minc=240*240;
		e=((k+1)&1);
		FWD(i,1,k+1){
			FWD(j,0,i){
				scanf("%d", &D[110-k+i][110-i+2*j+1]);
			}
		}
		FWD(i,k+1,2*k){
			FWD(j,0,2*k-i){
				scanf("%d", &D[110-k+i][110-2*k+i+2*j+1]);
			}
		}		
		FWD(mx,110-k-2,110+k+2){
			FWD(my,110-k-2,110+k+2){
				c=0;
				mk=0;
				//FWD(i,max(0, 110-2*k-10), min(220, 110+2*k+10)){
				//	FWD(j,max(0, 110-2*k-10), min(220, 110+2*k+10)){
				FWD(i,0,220){
					FWD(j,0,220){
						if(in(2*mx-i, 2*my-j)){
							if(D[i][j]!=-1){
								if(D[2*mx-i][j]!=-1 && D[2*mx-i][j]!=D[i][j]){c=1; break;}
								if(D[i][2*my-j]!=-1 && D[i][2*my-j]!=D[i][j]){c=1; break;}
								if(D[2*mx-i][2*my-j]!=-1 && D[2*mx-i][2*my-j]!=D[i][j]){c=1; break;}
								mk=max(mk, abs(mx-i)+abs(my-j));
							}
						}					
					}
					if(c==1) break;
				}
				if(c==0){
					d=0;
					FWD(i,0,220){
						FWD(j,0,220){
							if(((i+j)&1)==e && D[i][j]==-1 && abs(mx-i)+abs(my-j)<=mk) d++;
						}
					}
					minc=min(minc, d);
				}
			}
		}
		printf("Case #%d: %d\n", q, minc);
	}
}
