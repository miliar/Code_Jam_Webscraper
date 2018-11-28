#include <iostream>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX = 10000+1;
int M[MAX];
int N, L, H;

int main(){
	int Cases;
	cin >> Cases;
	for(int Case=1; Case <= Cases; ++Case){
		cin >> N >> L >> H;
		for (int i = 0; i < N; ++i){
			cin >> M[i];
		}
		int freq = 0;
		for (int i = L; i <= H && !freq; ++i){
			int j = 0;
			for (; j < N && !freq; ++j){
				if(M[j]%i != 0 && i % M[j] != 0)
					break;
			}
			if (j==N){
				freq = i;
				break;
			}
		}
		cout << "Case #" << Case << ": ";
		if (freq)
			cout << freq << "\n";
		else
			cout << "NO\n";
	}
	return 0;
}