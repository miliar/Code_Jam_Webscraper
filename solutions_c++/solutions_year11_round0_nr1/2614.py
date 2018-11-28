#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)

char name[100];
int place[100];
int solve(int n){
	int pos[2] = {1,1};
	int can = 0 , ans = 0 , f = name[0] == 'B';
	rep(i,n){
		int c = name[i] == 'B';
		if(f != c){
			if(can >= abs(pos[c]-place[i]))pos[c] = place[i];
			else pos[c] = pos[c] + (place[i] > pos[c] ? 1 : -1) * can;
			can = 0;
			f = c;
		}
		while(pos[c] != place[i]){
			pos[c] += place[i] > pos[c] ? 1 : -1;
			can++; ans++;
		}
		can++; ans++;
	}
	return ans;
}
int main(){
	int N;
	cin >> N;
	rep(NN,N){
		int n;
		cin >> n;
		rep(i,n) cin >> name[i] >> place[i];
		
		cout << "Case #" << NN+1 << ": " << solve(n) << endl	;
	}
}