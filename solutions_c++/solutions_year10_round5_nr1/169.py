#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

// Igor's number theory functions from shygypsy.com
template< class Int >
struct Triple
{
    Int d, x, y;
    Triple( Int q, Int w, Int e ) : d( q ), x( w ), y( e ) {}
};


template< class Int >
Triple< Int > egcd( Int a, Int b )
{
    if( !b ) return Triple< Int >( a, Int( 1 ), Int( 0 ) );
    Triple< Int > q = egcd( b, a % b );
    return Triple< Int >( q.d, q.y, q.x - a / b * q.y );
}


template< class Int >
Int inverse( Int a, Int n )
{
	if(a<0) a=((a%n)+n)%n;
    Triple< Int > t = egcd( a, n );
    if( t.d > Int( 1 ) ) return Int( 0 );
    Int r = t.x % n;
    return( r < Int( 0 ) ? r + n : r );
}

template< class Int >
bool isPrime( Int n )
{
    if( n < 2 ) return false;
    Int sq = Int( sqrt( n ) );
    for( Int i = 2; i <= sq; i++ )
        if( !( n % i ) ) return false;
    return true;
}



#define fu(i,m,n) for(int i=m; i<n; i++)

vector<int> factor(int M) {
	vector<int> ret;
	for(int i=2; i*i<=M; i++) {
		if(M%i == 0) {
			ret.push_back(i);
			while(M%i==0) M/=i;
		}
	}
	if(M>1) ret.push_back(M);
	return ret;
}

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		cout << "Case #" << tc << ": ";
		int bestp = 0;
		int D,K;
		cin >> D >> K;
		int maxP = 1;
		fu(i,0,D) maxP*=10;
		vector<int> SS(K);
		fu(i,0,K) cin >> SS[i];
				int xss = 0;
				fu(i,0,K) xss=max(xss, SS[i]);
		bool done = false;
		if(K==1) cout << "I don't know." << endl, done=true;
		if(!done) fu(i,0,K) fu(j,0,i) if(!done && SS[i]==SS[j]) {
			cout << SS[(K-j)%(i-j)+j] << endl;
			done = true;
		}
		if(!done && K==2) {
			cout << "I don't know." << endl;
			done = true;
		}
		if(!done) {
			for(int i=0; i+3<K; i++) {
				bestp = __gcd(bestp, (SS[i+1]-SS[i+2])*(SS[i+1]-SS[i+2])-(SS[i]-SS[i+1])*(SS[i+2]-SS[i+3]));
			}
			if(bestp<0) bestp=-bestp;
			if(bestp==0) {
				int primes = 0;
				for(int y=xss+1; y<maxP; y++) {
					if(isPrime(y)) {
						primes++;
						if(primes==2) {
							int nn = SS[1]-SS[2];
							int dd = SS[0]-SS[1];
							bool good=true;
							if(dd<0) {
								nn=-nn; dd=-dd;
							}
							int gg = abs(__gcd(nn,dd));
							nn/=gg;
							dd/=gg;
							int b;
							if(good) {
								fu(i,0,K) if(SS[i]%dd) good=false;
								b = SS[1] - SS[0]/dd*nn;
								fu(i,1,K) if(SS[i]!= SS[i-1]/dd*nn + b) good=false;
							}
							if(good) {
								int ret = SS[K-1]/dd*nn + b;
								if(ret >=0 && ret<bestp) cout << ret << endl;
								else good=false;
							}
							//if(SS[1]-SS[2] == SS[0]-SS[1] && 2*SS[K-1]-SS[K-2]<bestp && 2*SS[K-1]-SS[K-2]>=0) {
								//cout << 2*SS[K-1]-SS[K-2] << endl;
							//} else {
							if(!good) {
								cout << "I don't know." << endl;
							}
							done=true;
							break;
						}
						bestp = y;
					}
				}
			}
			if(!done) {
				vector<int> ps = factor(bestp);
				set<int> ret;
				fu(j,0,ps.size()) if(ps[j]>xss && ps[j]<maxP) {
					int a = (inverse<int>(SS[0]-SS[1],ps[j])*(SS[1]-SS[2])) % ps[j];
					a = (a+ps[j])%ps[j];
					int b = SS[1]-a*SS[0];
					b = (b+ps[j])%ps[j];
					int x = (a*SS[K-1]+b)%ps[j];
					x = (x+ps[j])%ps[j];
					ret.insert(x);
				}
				if(ret.size()==1) {
					cout << *ret.begin() << endl;
				} else {
					cout << "I don't know." << endl;
				}
			}
		}
	}
}
