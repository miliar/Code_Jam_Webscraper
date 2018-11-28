#include <queue>
#include <iostream>
using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)

int main(){
	int T; cin >> T;
	forn(t,T){

		queue<int> q;
		int money = 0;

		int R, k, N;
		cin >> R >> k >> N;
		forn(n,N){
			int g;
			cin >> g;
			q.push(g);
		}

		forn(i,R){
			int people = 0;
			queue<int> riding;
			while( !q.empty() && people+q.front() <= k){
				people += q.front();
				riding.push(q.front());
				q.pop();
			}
			money += people;
			while(!riding.empty()){
				q.push(riding.front());
				riding.pop();
			}
		}

		cout << "Case #" << t+1 << ": " << money << endl;

	}
	return 0;
}
