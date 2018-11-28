
#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int n;
	cin >> n;

	
	for (int i = 0; i < n; i++){
		int p, nn, sur, ti, res;

		cin >> nn >> sur >> p;
		res = 0;

		for (int j = 0; j < nn; j++){
			cin >> ti;

			if (ti % 3 == 0){
				if (ti / 3 >= p) res++; 
				else if (sur > 0 && ti / 3 + 1 >= p && ti > 0){
					res++; 
					sur--;
				}

			} else if (ti % 3 == 1){
				if (ti / 3 + 1 >= p) res++; 
			} else { // ti % 3 == 2
				if (ti / 3 + 1 >= p) res++; 
				else if (sur > 0 && ti / 3 + 2 >= p){
					res++; 
					sur--;
				} else {
					if (ti / 3 + 1 >= p) res++; 
				}
			}

			
		}

		cout << "Case #" << (i+1) << ": " << res << endl;
	}
	



	return 0;
}

