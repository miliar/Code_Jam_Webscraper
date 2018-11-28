#include <iostream>
#include <string>

using namespace std;

int main(){
    unsigned int T, N, K;
    cin >> T;
    for (unsigned int k = 0; k < T; k++){
	cin >> N >> K;
        cout << "Case #" << k+1 << ": ";
	unsigned int b = (1 << N) - 1;
	if ((K & b) == b)
	  cout << "ON";
	else
	  cout << "OFF";
	cout << endl;
    }
    return 0;
}
