#include <iostream>
typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned char UC;

using namespace std;
//using namespace boost::math;
//using namespace boost::numeric;
//using namespace boost::numeric::interval_lib::compare::certain;

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {

		UL n, k;
		cin >> n >> k;

		if((((((1<<n)-1)&k)+1)>>n)&1) {
			cout << "Case #" << nn+1 << ": ON" << endl;
		} else {
			cout << "Case #" << nn+1 << ": OFF" << endl;
		}
	}
	
	return 0;
}
