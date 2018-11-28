#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set>
#include <iterator>
#include <map>
#include <iomanip>
#include <cmath>
#include <stack>

using namespace std;

int A, N, M;

#define NN 10000
unsigned int prime[NN / 64];
#define gP(n) (prime[n>>6]&(1<<((n>>1)&31)))
#define rP(n) (prime[n>>6]&=~(1<<((n>>1)&31)))
void sieve()
{
        memset( prime, -1, sizeof( prime ) );

        unsigned int i;
        unsigned int sqrtN = ( unsigned int )sqrt( ( double )NN ) + 1;
        for( i = 3; i < sqrtN; i += 2 ) if( gP( i ) )
        {
                unsigned int i2 = i + i;
                for( unsigned int j = i * i; j < NN; j += i2 ) rP( j );
        }
}

vector<int> primes;

class State {
public:
        int i;
        long long int n;
        State(int _i, long long int _n) : i(_i), n(_n) {};
};


pair<int,int> backtrack() {

        stack<State> stateStack;

        State s(0, 1);
        stateStack.push(s);

        while (! stateStack.empty()) {
                State s = stateStack.top();
                stateStack.pop();
                
            //  cout << "State: prime factor " << primes[s.i] << " n " << s.n << endl;
							
                if ((s.n <= M ) && (A/s.n <= N)) {
									return make_pair(s.n, A/s.n);
								}

                if (A/s.n % primes[s.i] == 0) {
                        stateStack.push(State(s.i, s.n*primes[s.i]));
								}

								if (s.n == A) continue;
								
                if ((s.i+1) < primes.size()) stateStack.push(State(s.i+1, s.n));
        }

				return make_pair(-1,-1);
}


int main()
{
	int C;
	

	cin >> C;
	for (int c=0;c<C;c++) {

		cout << "Case #" << c+1 << ": ";

		cin >> N >> M >> A;

		for (int i1=0;i1<=N;i1++) {
			for (int j1=0;j1<=M;j1++) {
				for (int i2=0;i2<=N;i2++) {
					for (int j2=0;j2<=M;j2++) {
				if ((i1*j2-j1*i2) == A) {
					cout << "0 0 " << i1 << " " << j1 << " "  << i2 << " " << j2 << endl;
				goto end; 
			}
			}
		}
	}
}
	
	cout << "IMPOSSIBLE" << endl;
	end: ;
}
}
