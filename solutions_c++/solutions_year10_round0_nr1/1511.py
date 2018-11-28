#include <iostream>

using namespace std;

void solve()
{
	int N;
	long long K;
	cin >> N >> K;
	for(int i=0;i<N;++i) {
		if(!(K&1)) {
			cout << "OFF" << endl;
			return;
		}
		K >>= 1;
	}
	cout << "ON" << endl;
}


int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for( int i = 0; i < T; ++i ) {
                cout << "Case #" << i+1 << ": ";
                solve();
	}
	return 0;
}
//---------------------------------------------------------------------------
