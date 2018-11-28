#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <iostream>

using namespace std;


#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)

using namespace std;

int pos[300];
bool r[300];

int main() {
	int n;
	scanf("%d\n",&n);
	FR(i,n) {
		cout << "Case #" << (i+1) << ": ";
		int cura=1,curb=1;
		int k;
		cin >> k;
		FR(j,k) {
			char c;
			cin >> c;
			r[j]=(c=='B');
			scanf("%d",&pos[j]);
		}
		int cur=0; // next thing to be pressed
		int tm=0;
		int nxta,nxtb;
		int posa,posb;
		FR(j,k) {
			if(r[j]) {
				nxta=pos[j];
				posa=j;
				break;
			}
		}
		FR(j,k) {
			if(!r[j]) {
				nxtb=pos[j];
				posb=j;
				break;
			}
		}
		
		for(;;) {
			if(cur==k) break;
			bool adv=false;
			if(cura!=nxta) {
				if(nxta>cura) {
					cura++;
				} else {
					cura--;
				}
			} else {
				if(cur==posa) {
					adv=true;
					FOR(j,posa+1,k) {
						if(r[j]) {
							nxta=pos[j];
							posa=j;
							break;
						}
					}
					if(posa==cur) posa=k;
				}
			}
			
			
			if(curb!=nxtb) {
				if(nxtb>curb) {
					curb++;
				} else {
					curb--;
				}
			} else {
				if(cur==posb) {
					adv=true;
					FOR(j,posb+1,k) {
						if(!r[j]) {
							nxtb=pos[j];
							posb=j;
							break;
						}
					}
					if(posb==cur) posb=k;
				}
			}
			
			
			
			
			if(adv) cur++;
			tm++;
		}
		
		cout << tm << endl;
		
	}
}