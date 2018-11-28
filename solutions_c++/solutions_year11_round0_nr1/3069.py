#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>

#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define pii pair<char,int>
#define pb(x) push_back(x)

using namespace std;

vector <pii> CC;
vector <int> AA;
vector <int> BB;

int main()
{
	int n;
	int i;
	int Test;
	char a;
	int b;
	scanf("%d",&Test);
		
	int pos1, pos2 , ind1 , ind2 , t , time;
	int test = 1;
	while(Test--) {
		
		scanf("%d",&n);
		time = 0;
		CC.clear();
		AA.clear();
		BB.clear();
		FOR(i,1,n) {
			cin >> a >> b;
			CC.pb(pii(a,b));
			if(a == 'O') {
				AA.pb(b);
			}
			else {
				BB.pb(b);
			}
		}
		pos1 = 1;
		pos2 = 1;
		ind1 = 0;
		ind2 = 0;

		FOR(i,0,n-1) {
			if(CC[i].first == 'O') {
				t = ABS(CC[i].second-pos1)+1;
				pos1 = CC[i].second;
				ind1++;
				
				if (BB[ind2] < pos2){
					pos2 = pos2 - (t);
					if (pos2 < BB[ind2]){
						pos2 = BB[ind2];
					}
				}else {
					pos2 = pos2 + (t);
					if (pos2 > BB[ind2]){
						pos2 = BB[ind2];
					}
				}
				time += t;
			}else {
				t = ABS(CC[i].second-pos2) + 1;
				pos2 = CC[i].second;
				ind2++;

				if( AA[ind1] < pos1 ){
					pos1 = pos1 - (t);
					if( pos1< AA[ind1] ){
						pos1 = AA[ind1];
					}
				}else {
					pos1 = pos1 + (t);
					if( pos1 > AA[ind1] ){
						pos1 = AA[ind1];
					}
				}
				time += t;
			}
		}
		printf("Case #%d: %d\n", test, time);
		test++;
	}	
	return 0;
}
