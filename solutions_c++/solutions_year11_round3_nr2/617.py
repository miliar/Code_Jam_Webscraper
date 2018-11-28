#include <iostream>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX = 1000+1;
lli M[MAX];
lli L, t, N, C;
lli Arrived[MAX];

int main(){
	int Cases;
	cin >> Cases;
	for(int Case=1; Case <= Cases; ++Case){
		int C;
		cin >> L >> t >> N >> C;
		for (int i = 0; i < C; ++i){
			int x;
			cin >> x;
			for (int j = i; j < N; j += C)
				M[j] = x;
		}
		/*for (int i = 0; i < N; ++i){
		cerr << M[i] << " ";
		}
		cerr << endl;*/
		lli fullTime = 0;
		for (int i = 0; i < N; ++i){
			Arrived[i] = fullTime;
			fullTime += M[i]*2;
		}
		lli minTime = fullTime;
		if(L>0){
			for (int i = 0; i < N; ++i){
				lli buildTime = max(0LL, t-Arrived[i]);
				buildTime = min (buildTime, M[i]*2);
				if(( buildTime)%2)
					cerr << "1M[i] - buildTime)%2" << i << " " <<  " " << M[i]<< endl;
				lli savedTime = M[i] - buildTime/2;
				lli newTime = fullTime-savedTime;
				if(newTime < minTime)
					minTime = newTime;
				if(L>1){
					for (int j = i+1; j < N; ++j){
						lli buildTime = max(0LL, t-(Arrived[j]-savedTime));
						buildTime = min (buildTime, M[j]*2);
						if(( buildTime)%2)
							cerr << "M[j] - buildTime" << endl;
						lli savedTime2 = M[j] - buildTime/2;
						lli newTime2 = newTime-savedTime2;
						if(newTime2 < minTime)
							minTime = newTime2;
					}
				}
			}
		}
		cout << "Case #" << Case << ": " << minTime <<endl;
	}
	return 0;
}