#include <iostream> 

using namespace std;

int main(){
	int T; 
	int N;
	int x;
	int d;

	cin >> T;

	for (int cnt = 1; cnt <=T; ++cnt){
		cin >> N;
		d = 0;
		for (int i=1; i<=N; ++i){
			cin >> x;
			if (x!=i)
				d++;
		}
		cout << "Case #" << cnt << ": ";
		cout << d << endl;
	}

	return 0;
}
