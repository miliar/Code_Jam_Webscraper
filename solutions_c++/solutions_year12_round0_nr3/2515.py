#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

int numeroDigitos( int n ) {
	static char s[32];
	static int len;
	len = sprintf( s, "%i", n );
	return len;
}

unsigned int shift(unsigned int mov, unsigned int len, const char s[]) {
	char aux[32];
	for(unsigned int i=0; i<len; i++)
		aux[ (mov+i) % len ] = s[i];
	return atoi( aux );
}
int main(int argc, char *argv[]) {
	int T;
	cin>>T;
	vector<unsigned int> As(T), Bs(T), R(T, -1);
	vector<unsigned int> pasados(8);
	
	for(int i=0; i<T; i++) {
		cin>>As[i]>>Bs[i];
	}

	for(int i=0; i<T; i++) {
		unsigned int A = As[i], B = Bs[i];
		unsigned int dig = numeroDigitos( A );
		
		if( A == B || dig < 2) {
			R[i] = 0;
		}
		else {
			unsigned int c = 0, m, len;
			char s[32];
			for(unsigned int n=A; n<B; n++) {
				pasados.clear();
				len = sprintf( s, "%i", n );
				for(unsigned int j=1; j<dig; j++) {
					
					m = shift(j, len, s);
					if( m > n && m <= B && m >= A && find(pasados.begin(), pasados.end(), m) == pasados.end() ) {
						c++;
						pasados.push_back( m );
					}
				}
			}
			R[i] = c;
		}
	}
	
	for(int i=0; i<T; i++) {
		assert( R[i] >= 0 );
		cout<<"Case #"<<i+1<<": "<<R[i]<<endl;
	}
	
	return 0;
}

