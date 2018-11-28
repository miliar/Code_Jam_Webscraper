#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <iostream>

#define show(x) cerr<<#x<<'='<<x<<endl
#define eps 1e-8
using namespace std;
typedef pair<int, int> pii;
const int MAXN=100*1000+10;
double p[MAXN], q[MAXN], ans;
int A, B;

int main() {
	int T;
	cin>>T;
	for (int testnum=0; testnum<T; ++testnum) {
		cin>>A>>B;
		for (int i=0; i<A; ++i)
			cin>>p[i];
		ans=B+2;
		q[0]=p[0];
		for (int i=1; i<A; ++i)
			q[i]=q[i-1]*p[i];
		for (int i=A-1; i>=0; --i) {
			double c=q[i]*(B-i)+(1-q[i])*((B-i)+(B+1))+(A-1-i);
			if (ans-eps>c)
				ans=c;
		}
		cout<<"Case #"<<testnum+1<<": "<<fixed<<setprecision(6)<<ans<<endl;
	}
	return 0;
}
