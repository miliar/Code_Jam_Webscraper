using namespace std;

#include <iostream>

//#define TEST
//#define SMALL
#define LARGE
int main(void) {
#ifdef TEST
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

#ifdef SMALL
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	unsigned int T;
	unsigned int N;
	long int K;
	bool state = false;

	cin >> T;

	for(unsigned int i=0; i<T; i++) {
		cin >> N;
		cin >> K;

		if(K < N)
			state = false;
		else {

			unsigned int prec = 0;
			for(unsigned int j=0; j<N; j++) {
				prec = prec*2+1;
			}
			while(K > 0) {
				K = K - prec - 1;
			}

			if(K == -1)
				state = true;
			else
				state = false;
		}
		printf("Case #%d: %s\n",(i+1),(state)?"ON":"OFF");
	}

	return 0;
}
