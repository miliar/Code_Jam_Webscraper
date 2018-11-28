#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <math.h>

#define max(x,y) (x>y?x:y)
#define min(x,y) (x>y?y:x)

using namespace std;


int main(){
	int i=0, n;
	int line = 1;
	cin >> n;
	while(++i<=n){
		int result = 0;
		int j=0;
		int N;
		int L,H;
		bool impossible;
		cin >> N >> L >> H;
		vector<int> players(N);
		while(++j<=N){
			cin >> players[j-1];
		}
		for(int k=L; k<=H; k++){
			impossible = false;
			for(int l=0;l<N;l++){
				if(!(k<players[l]&&players[l]%k==0||k>=players[l]&&k%players[l]==0)){
					impossible=true;
					break;
				}
			}
			if(impossible==false){
				result = k;
				goto END;
			}
		}
		//cout << "line:" << line << endl;
		END:
		cout << "Case #" << i << ": ";
		if(impossible){
			cout << "NO" << endl;
		}else{
			cout << result << endl;
		}
	}
	return 0;
}