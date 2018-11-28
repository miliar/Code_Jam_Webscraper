// Started 11am
#include <iostream>
#include <utility>
#define for0(i,n) for(int i = 0; i < n; i ++)

using namespace std;

int main()
{

	int kases; cin >> kases;
	for0(kase,kases)
	{
		long long r,k,n;
		cin >> r >> k >> n;
		int* qu = new int[n];
		
		for0(i,n) cin >> qu[i];
		
		int qi = 0;
		long long pf = 0;
		
		pair<int, long long>* QItoQJandPD = new pair<int, long long>[n];
		for0(i,n) QItoQJandPD[i].first = -1;
		
		
		for0(ri, r)
		{
			if (QItoQJandPD[qi].first != -1)
			{
				int oldqi = qi;
				qi = QItoQJandPD[oldqi].first;
				pf += QItoQJandPD[oldqi].second;
			}
			else
			{
				int oldqi = qi;
				
				long long ki = k;
				int w = 0;
				while(ki - qu[qi] >= 0 && (qi != oldqi || w==0)) {
					w=1;
					ki -= qu[qi];
					qi = (qi + 1) % n;
				}
				pf += k-ki;
				
				QItoQJandPD[oldqi].first = qi;
				QItoQJandPD[oldqi].second = k-ki;
			}
		}
		cout << "Case #" << (kase+1) << ": " << pf << endl;
		
		delete [] QItoQJandPD;
		delete [] qu;
	}
	return 0;
}