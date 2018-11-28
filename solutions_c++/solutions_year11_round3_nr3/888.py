#include <iostream>
#include <vector>
using namespace std;

bool isHarm(long long a, long long b){
	return max(a,b)%min(a,b)==0;
}

int main(){
	long long n, m, a, b, temp;
	bool success;
	cin >> n;
	for(int i=1; i<=n; i++){
		cout << "Case #" << i << ": ";
		vector<long long> player;
		cin >> m >> a >> b;
		for(int j=0; j<m; j++){
			cin >> temp;
			player.push_back(temp);
		}
		for(int j=a; j<=b; j++){
			success = true;
			for(long long k=0; k<m; k++){
				if(!isHarm(j,player[k])){
					success = false;
					break;
				}
			}
			if(success){
				cout << j << endl;
				break;
			}
		}
		if(!success){
			cout << "NO" << endl;
		}
	}
	//system("pause");
}
