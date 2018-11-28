#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<fstream>
using namespace std;
map<int, int> mp;
int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt.out", "w", stdout);
	int t, n;
	cin >> t;
	for(int i = 0; i < t; i++){
		cin >> n;
		int s[20];
		for(int i = 0; i < n; i++)
			cin >> s[i];
		mp.clear();
		int a = -1, b = -1;
		for(int i = 1; i < (1 << n); i++){
			int y = 0;
			for(int j = 0; j < n; j++){
				if(i & (1 << j)){
					y += s[j];
				}
			}
			if(mp.find(y) != mp.end()){
				a = mp[y];
				b = i;
				break;
			}
			mp[y] = i;
		}
		cout << "Case #" << i + 1 << ":" << endl;
		if(a == -1)
			cout << "Impossible" << endl;
		else{
			int k = 0;
			for(int i = 0; i < n; i++){
				if( a & (1 << i)){
					if(k)
						cout << " ";
					cout << s[i] ;
					k++;
				}
			}
			cout << endl;
			k = 0;
			for(int i = 0; i < n; i++){
				if( b & (1 << i)){
					if(k)
						cout << " ";
					cout << s[i] ;
					k++;
				}
			}
			cout << endl;
		}
	}
	return 0;
}
