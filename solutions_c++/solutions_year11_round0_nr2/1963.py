#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

int c, d, n;

void single_case(int caseID) {
	vector<char> X, C;
	vector< pair<char,char> > Cp, Dp;
	scanf("%d",&c);
	while(c--) {
		char in[4];
		scanf("%s",in);
		Cp.PB(MP(in[0],in[1]));
		Cp.PB(MP(in[1],in[0]));
		C.PB(in[2]);
		C.PB(in[2]);
	}
	scanf("%d",&d);
	while(d--) {
		char in[3];
		scanf("%s",in);
		Dp.PB(MP(in[0],in[1]));
		Dp.PB(MP(in[1],in[0]));
	}
	scanf("%d",&n);
	char in[123];
	scanf("%s",in);
	for(int i = 0 ; i < n ; i++) {
		X.PB(in[i]);
		int t = X.size();
		if ( t  < 2 )
			continue;
		bool a = false;
		for(int k = 0 ; k < Cp.size() ; k++) 
			if ( X[t-2] == Cp[k].ST && X[t-1] == Cp[k].ND ) {
				X.pop_back(); X.pop_back();
				X.PB(C[k]);
				a = true;
				break;
			}
		if ( a ) continue;
		for(int k = 0 ; k < Dp.size() ; k++) {
			for(int j = 0 ; j < t-1 ; j++)
				if ( X[t-1] == Dp[k].ST && X[j] == Dp[k].ND ) {
					a = true;
					X.clear();
					break;
				}
			if ( a ) 
				break;
		}
	}
	printf("Case #%d: [",caseID);
	if ( X.size() ) {
		printf("%c",X[0]);
		for(int i = 1 ; i < X.size(); i++)
			printf(", %c",X[i]);
	}
	printf("]\n");
}

int main() {
	int z;
	scanf("%d",&z);
	for(int i = 1 ; i <= z ; i++) {
		single_case(i);
	}
}
