#include <iostream>
#include <vector>
using namespace std;

char c;
vector<int> o;
vector<int> b;
vector<pair<char, int> > s;

int main(){
	int n, t, d;
	cin >> n;
	
	for (int C = 1; C <= n; C++){
		o.clear(), b.clear(); s.clear();
		
		cin >> t;
		for (int i = 0; i < t; i++){
			cin >> c >> d;
			if (c == 'O')
				o.push_back(d);
			else
				b.push_back(d);
			s.push_back(make_pair<char, int>(c, d));
			//cout << c << ' ' << d << endl;
		}
		
		int sO = 0, sB = 0, ans = 0, T = 0, O = 1, B = 1, mO, mB;
		while (T != s.size()){
			//printf("Time: %d", ans);
			mO = mB = 0;
			if (sO != o.size()){	// O need to move
				if (O != o[sO]){
					if (O > o[sO])
						O--;
					else
						O++;
					mO = 1;
					//printf(" O: Move to button %d", O);
				}
			}
			if (sB != b.size()){	// B need to move
				if (B != b[sB]){
					if (B > b[sB])
						B--;
					else
						B++;
					mB = 1;
					//printf(" B: Move to button %d", B);
				}
			}
			
			if (sO != o.size() && s[T].first == 'O' && !mO && s[T].second == O){
				T++;
				sO++;
				//printf(" O: Push button %d", O);
			}
			else if (sB != b.size() && s[T].first == 'B' && !mB && s[T].second == B){
				T++;
				sB++;
				//printf(" B: Push button %d", B);
			}
			//printf("\n");
			ans++;
			//system("pause");
		}
		printf("Case #%d: %d\n", C, ans);
	}
	
	return 0;
}
