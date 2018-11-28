#include <iostream>
#include <queue>

using namespace std;

int main() {
  queue<int, deque<int> > Q;
  queue<int, deque<int> > P;
  int T, r, k, n;
  long money, passengers;
  cin >> T;

  for(int i = 1; i <= T; i++) {
    cin >> r >> k >> n;

    while(! Q.empty()) {
      Q.pop();
    }

    for(int j = 0; j < n; j++) {
      cin >> passengers;
      Q.push(passengers);
    }

    cout << "Case #" << i << ": ";

    money = 0;

    for(int j = 0; j < r; j++) {
      passengers = 0;
      while(!Q.empty() && passengers + Q.front() <= k) {
	passengers += Q.front();
	P.push(Q.front());
	Q.pop();
      }
      while(!P.empty()) {
	Q.push(P.front());
	P.pop();
      }
      money += passengers;
    }
    cout << money << endl;
  }
  return 0;
}
