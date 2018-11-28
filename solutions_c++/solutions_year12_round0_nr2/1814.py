#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream cin("input.txt");
	ofstream cout("bout.txt");
	int T;
	cin >> T;
	for(int cnt=1 ; cnt<=T ; cnt++){
		int N;
		int S;
		int p;
		int ans = 0;
		int t;

		cin >> N >> S >> p;
		while(N--){
			cin >> t;
			if(p != 1){
				if(t >= p*3 - 2)
					ans++;
				else if(t >= p*3 - 4 && S){
					ans++;
					S--;
				}
			}
			else{
				if(t != 0)
					ans++;
			}
		}

		cout <<"Case #"<<cnt<<": " << ans << endl;
	}
}