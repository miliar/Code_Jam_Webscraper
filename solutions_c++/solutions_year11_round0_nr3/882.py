#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

ifstream cin ("C-Large.in");
ofstream cout ("C-Large2.out");


int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int N;
		vector <int> vc;
		cin >> N;
		int sum = 0;
		int xr = 0;
		int mn = 2*1000*1000;
		for(int j=0;j<N;j++){
			int a;
			cin >> a;
			vc.push_back(a);
			sum+=a;
			xr = xr^a;
			mn = min(mn,a);
		}
		if(xr!=0){
			cout << "Case #"<<i+1<<": NO"<< endl;
			continue;
		}
		else{
			cout << "Case #" <<i+1<<": " << sum-mn << endl;
		}
	}
	return 0;
}
