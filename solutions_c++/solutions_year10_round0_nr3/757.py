#include<iostream>
using namespace std;
long long int ar[1002][3],used[1002];
long long int T,R,K,N;
int main(){
	cin >> T;
	for(int I=1;I<=T;I++){
		for(int i=0;i<N;i++) used[i]=0;
		cin >> R >> K >> N;
		long long int sum=0;
		for(int i=0;i<N;i++){
			cin >> ar[i][0];
			sum += ar[i][0];
		}
		if(sum < K){
			cout << "Case #" << I << ": " << R*sum << endl;
			continue;
		}
		long long int cnt=0,q=0;
		sum=0;
		while(cnt<R && !used[q]){
			used[q] = 1;
			ar[q][1] = cnt;
			ar[q][2] = sum;
			for(long  long int x=0;x+ar[q][0] <= K;q=(q+1)%N){
				x+=ar[q][0];
				sum+=ar[q][0];
			}
			cnt++;
		}
	/*	for(int i=0;i<N;i++)
			cout << ar[i][0] << " " << ar[i][1] << " "<<ar[i][2] << endl;*/
		if(cnt == R){
			cout << "Case #" << I << ": " << sum << endl;
			continue;
		}
		int long long cntDiff = cnt - ar[q][1];
		int long long sumDiff = sum - ar[q][2];
		sum += ((R-cnt)/cntDiff) * sumDiff;
		cnt += ((R-cnt)/cntDiff) * cntDiff;
		while(cnt < R){
			for(long long int x=0;x+ar[q][0] <=K ; q=(q+1)%N){
				sum += ar[q][0];
				x+=ar[q][0];
			}
			cnt++;
		}
		cout << "Case #" << I << ": " << sum << endl;

	}
}
