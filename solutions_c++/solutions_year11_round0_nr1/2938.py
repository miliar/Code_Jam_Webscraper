#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>

#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define pii pair<char,int>
#define pb(x) push_back(x)

using namespace std;

vector <pii> C1;
vector <int> A1;
vector <int> B1;

int main()
{
	int n;
	int i;
	int T;
	char a;
	int b;
	scanf("%d",&T);
		
	int idx1, idx2 , ind1 , ind2 , t , time;
	int test = 1;
	while(T--) {
		
		scanf("%d",&n);
		time = 0;
		C1.clear();
		A1.clear();
		B1.clear();
		for(i=1;i<=n;i++) {
			cin >> a >> b;
			C1.pb(pii(a,b));
			if(a == 'O') {
				A1.pb(b);
			}
			else {
				B1.pb(b);
			}
		}

		idx1= 1;
		idx2 = 1;
		ind1 = 0;
		ind2 = 0;

		for(i=0;i<=n-1;i++) {
			if(C1[i].first == 'O') {
				t = ABS(C1[i].second-idx1)+1;
				idx1= C1[i].second;
				ind1++;
				
				if(B1[ind2] < idx2) {
					idx2 = idx2 - (t);
					if(idx2 < B1[ind2]) {
						idx2 = B1[ind2];
					}
				}
				else {
					idx2 = idx2 + (t);
					if(idx2 > B1[ind2]) {
						idx2 = B1[ind2];
					}
				}
				time += t;
			}
			else {
				t = ABS(C1[i].second-idx2)+1;
				idx2 = C1[i].second;
				ind2++;

				if(A1[ind1] < idx1) {
					idx1= idx1- (t);
					if(idx1< A1[ind1]) {
						idx1= A1[ind1];
					}
				}
				else {
					idx1= idx1+ (t);
					if(idx1> A1[ind1]) {
						idx1= A1[ind1];
					}
				}
				time+=t;
			}
		}
		printf("Case #%d: %d\n",test,time);
		test++;
	}	
	return 0;
}
