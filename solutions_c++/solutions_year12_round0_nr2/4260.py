
#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
	int T;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	cin>>T;
	int count = 1;
	while (T--) {
		int N, S, p,result = 0;
		cin>>N>>S>>p;
		int i = N;
		int temp;
		while ( i-- ) {
			cin>>temp;
			if (temp >= ((p-1)*3+1)) {
				++result;
			} else if (S > 0) {
				if (temp >=  ((p-2)*3+2) && temp >= p) {
					++result;
					--S;
				}
			}
		}
		cout<<"Case #"<<count++<<": "<<result<<endl;
	}
	return 0;
}
