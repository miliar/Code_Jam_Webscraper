#include <iostream>
using namespace std;
const int MAX = 1100;
int R, k, N;
long long sum;
int times[MAX];
int quants[MAX];
int groups[MAX];
int main(){
	int Z=1;
	cin >> Z;
	for(int z=1; z<=Z; z++){
		cin >> R >> k >> N;
		for(int i=0; i<N; i++)
			cin >> groups[i];
			
		for(int i=0; i<N; i++){
			sum = 0;
			int j = i;
			while(sum+groups[j]<=k){
				sum+=groups[j];
				j=(j+1)%N;
				if(j==i) break;
			}
			times[i] = j;
			quants[i] = sum;
		}
//		cout << "times" << endl;
//		for(int r2d2 = 0; r2d2<=N-1; r2d2++)
//			cout << times[r2d2] << " ";
//		cout << endl;
//		cout << "quants" << endl;
//		for(int r2d2 = 0; r2d2<=N-1; r2d2++)
//			cout << quants[r2d2] << " ";
//		cout << endl;
		
		
		long long result = 0;
		int posi = 0;
		for(int i=1; i<=R; i++){
			result += quants[posi];
			posi = times[posi];
		}
		
		cout << "Case #" << z <<": " << result << endl;
	
	
	}
	return 0;
}


