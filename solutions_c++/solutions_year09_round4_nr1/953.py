#include <iostream>
using namespace std;

int main(){
	int T, N;
	cin >> T;
	char matrix[50][50];	
	int ans;
	int maxcol[50];
	for (int t=1; t<=T; t++){
		cin >> N;
		for (int i=0; i<N; i++){
			char row[50];
			cin >> row;
			int max = 0;
			for (int j=0; j<N; j++){
				if (row[j] == '1'){
					max = j+1;
				}
			}
			maxcol[i+1] = max;
		}
		
		ans = 0;
		for (int i=1; i<=N; i++) {
			if (maxcol[i] > i){
				for (int j=i+1; j<=N; j++){
					if (maxcol[j] <= i){
					//cerr << "swap " << i << " " << j << endl;
						int temp = maxcol[j];
						for (int k=j; k>i; k--){
							maxcol[k] = maxcol[k-1];
						}						
						maxcol[i] = temp;
						ans += (j-i);
						break;
					}
				}
			}
			//for (int j=1; j<=N; j++) cerr << maxcol[j]; cerr << endl;
		}
	
		cout << "Case #" << t << ": " << ans << endl;
	}
}