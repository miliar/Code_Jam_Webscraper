#include <iostream>
#include <algorithm>
using namespace std;


const int MAX_N=100+10;
int sum[MAX_N];

int main(){
	int T;
	cin >> T;
	for (int test=0;test<T;test++){
		int n;
		int s;
		int p;
		cin >>n >> s >> p;
		for (int i=0;i<n;i++)
			cin >> sum[i];
		sort(sum,sum+n);
		//for (int i=0;i<n;i++) cout << sum[i] << " "; cout << endl;
		int high=3*p-2;
		int low=3*p-4;
		if (p==1) low=1;
		//cout << "s " << s << " p " << p << " high " << high << " low " << low << endl;
		int ans=0;
		for (int i=n-1;i>=0;i--){
			if (sum[i]>=high) ans++;
			else if (sum[i]>=low && s>0) {s--; ans++;}
			else break;
		}
		cout << "Case #" << test+1 << ": " << ans << endl;
			
		
		
	}

}