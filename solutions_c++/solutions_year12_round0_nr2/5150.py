#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int round = 0;
	cin>>round;
	cin.get();
	int t, s, p;
	int num[101];
	for (int n = 1; n <= round; n++){
		cin>>t>>s>>p;
		for ( int i = 0; i < t; i++ ){
			cin>>num[i];
		}
		int count = 0;
		for ( int i = 0; i < t; i++ ){
			if ( num[i]/3 >= p ){
				count++;
				continue;
			}
			if ( num[i] <= p ) {
				continue;
			}
			int gap = num[i] - p;
			if ( gap/2 >= p-1 ){
				count++;
				continue;
			}
			if ( gap/2 >= p-2 ){
				if ( s > 0 ){
					s--;
					count++;
				}
				continue;
			}
		}
		cout<<"Case #"<<n<<": "<<count<<endl;
	}
	return 0;
}