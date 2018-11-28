/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <cstdio>

using namespace std;

const int maxN= 100 + 5;

char col[maxN];
int Q,n;
int pos [maxN];

inline int ABS (int x){
	return x<0 ? -x : x;
}
/*************************************/
inline int solve(){
	
	int ret=0;

	int pos1= 1, pos2= 1;
	int rem1= 0, rem2= 0;

	for (int i=1;i<=n;i++){
		
		if (col[i]=='O'){
			int diff= ABS (pos[i]-pos1);
			if (diff<=rem1){
				ret++;
				rem2++;
			}
			else{
				ret += diff-rem1+1;
				rem2+= diff-rem1+1;
			}
			rem1=0;
			pos1= pos[i];
		}

		if (col[i]=='B'){
			int diff= ABS (pos[i]-pos2);
			if (diff<=rem2){
				ret++;
				rem1++;
			}
			else{
				ret += diff-rem2+1;
				rem1+= diff-rem2+1;
			}
			rem2=0;
			pos2= pos[i];
		}
	}

	return ret;
}
/************************************/
int main(){
	cin >> Q;
	
	for (int t=1;t<=Q;t++){
		cin >> n;
		for (int i=1;i<=n;i++)
			cin >> col[i] >> pos[i];

		cout << "Case #" << t << ": " << solve() << endl; 
	}

	return 0;
}
