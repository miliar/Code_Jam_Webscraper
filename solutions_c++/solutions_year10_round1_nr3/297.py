#include <iostream>
#include <cmath>

using namespace std;

int main(){
	int TEST; cin >> TEST;
/*
	bool win[20][20];
	memset(win, false, sizeof(win));
	for(int i=1;i<20;i++){
		for(int j=1;j<i;j++){
			if(i%j==0) win[i][j] = win[j][i] = true;
			else {
				bool flag = true;
				for(int k=1;i-k*j>=0;k++){
					flag &= win[i-k*j][j];
				}
				if(!flag) win[i][j] = win[j][i] = true;
			}
		}
	}
	for(int i=1;i<20;i++){
		for(int j=1;j<20;j++) cout << win[i][j] << " "; cout << endl;
	}
*/
	static int first[1000001], last[1000001];
	memset(first, 0, sizeof(first));
	for(int i=1;i<=1000000;i++) last[i] = (int)min((long long)10000000, (long long)ceil(i*(1+sqrt(5.0))/2.0));
	for(int i=1000000;i>=1;i--){
		for(int j=last[i];j<=1000000&&first[j]==0;j++)
			first[j] = i;
	}
	for(int test=1;test<=TEST;test++){
		int A1, A2, B1, B2; cin >> A1 >> A2 >> B1 >> B2;
		int ans = 0;
		for(int i=A1;i<=A2;i++){
			if(B2 <= first[i]) ans += B2-B1+1;
			else if(B1 <= first[i]) ans += first[i]-B1+1;
			if(B1 >= last[i]) ans += B2-B1+1;
			else if(B2 >= last[i]) ans += B2-last[i]+1;
		}
		printf("Case #%d: %d\n", test, ans);
	}
}