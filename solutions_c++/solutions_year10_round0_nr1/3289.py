#include <iostream>
#include <vector>

using namespace std;

int main (int argc, char * const argv[]) {
	int T;
	int N;
	uint32_t K;
	
	cin >> T;
	
	for (int C=1; C<=T; C++) {
		cin >> N;
		cin >> K;
		
		vector<bool> snappers(N, false);

		for (int i=0; i<K; i++)
		{
			for (int S=0; S<N; S++)
			{
				if (snappers[S] == true)
				{
					snappers[S] = false;
				}
				else {
					snappers[S] = true;
					break;
				}
			}
		}

		bool result = true;
		
		for (int S=0; S<N; S++)
		{
			result &= snappers[S];
		}
		
		cout << "Case #" << C << ": " << (result ? "ON" : "OFF") << endl;
	}
	
    return 0;
}
