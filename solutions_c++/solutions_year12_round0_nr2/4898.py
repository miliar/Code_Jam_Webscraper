#include <iostream>

using namespace std;

int main(){
	int cases;
	int n,s,p, k, kk, count;

	cin >> cases;
	for(int i=0;i<cases;i++){
		cin >> n >> s >> p;
		for(int j=0;j<n;j++){
			int score;
			cin >> score;

			k = score - p;
			kk = 2*p - k;
			if(k > 0 || k == 0){
				count++;
				if(kk > 4) count--;
				if(kk == 3 || kk == 4){
					if(s > 0) s--;	
					else count--;
				} 
			}
			else{}
		}
		cout << "Case #" << i+1 << ": " << count;
		if(i != (cases - 1)) cout << endl;
		count = 0;
	}
}
