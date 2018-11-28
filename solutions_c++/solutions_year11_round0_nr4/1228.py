#include <iostream>
#include <iomanip>

using namespace std;

int main (int argc, char const *argv[])
{
	int T, N;
	double ans;
	cin >> T;
	int data[1000];
	
	
	for(int i=0 ; i< T; i++){
		ans = 0;
		cin >> N;
		for(int j = 0; j < N; j++) {
	        cin >> data[j];
	        if (data[j] != j+1) ans++;
	    }
		cout<<"Case #"<<i+1<<": "<<setprecision(6)<<ans<<endl;
	}
	return 0;
}