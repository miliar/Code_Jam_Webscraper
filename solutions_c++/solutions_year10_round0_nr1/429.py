#include <iostream>
using namespace std;

int main() {

freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);

unsigned int N, K, T, t;

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;
cin >> K;

cout << "Case #" << t << ": ";
if (K%(1U<<N) == ((1U<<N)-1U)) cout << "ON" << endl;
else cout << "OFF" << endl;

}

return 0;
}
