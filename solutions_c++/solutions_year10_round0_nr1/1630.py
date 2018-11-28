#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int T, N, K;
    
    cin >> T;
    for (int i = 0; i < T; ++i) {
		cin >> N;
		cin >> K;
		++K;
		if ( K & ( (1 << N) - 1) ) {
			printf("Case #%d: OFF\n", i + 1);
		} else {
			printf("Case #%d: ON\n", i + 1);
		}
	}
	
    return EXIT_SUCCESS;
}
