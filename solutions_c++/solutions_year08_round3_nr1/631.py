#include <iostream>
#include <functional>

using namespace std;

int main()
{

	int t;
	cin >> t;
	
	for (int i=0; i<t; ++i) {
		int p,k,l;
		cin >> p >> k >> l;
		
		int fr[1000];
		
		for (int j=0; j<l; ++j) {
			cin >> fr[j];
		}
		
		sort(fr, fr+l,greater<int>());
		
		int kp = 0, tkp = 0;
		for (int j=0; j<l; j += k) {
			++kp;
			//int tf = 0;
			for (int m=j; (m<j+k) && (m < l); ++m) {
				tkp += (fr[m] * kp);
			}
		}
	
		cout << "Case #" << i+1 << ": " << tkp << '\n';
	}
	
	return 0;
}

