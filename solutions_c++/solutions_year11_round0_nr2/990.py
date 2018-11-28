#include <iostream>
#include <cstring>
#include <vector>
#include <utility>
#include <set>
#include <map>

#define MAX 110

using namespace std;

int test, t=1, c, o, n, sz;
char a, b, ab, flag;
char comb[256][256], opose[256][256];
string res;

int main(){
	ios_base::sync_with_stdio(false);
	
	cin >> test;
	while (test--){
		memset(comb, 0, sizeof(comb));
		memset(opose, 0, sizeof(opose));
		res = "";
		
		cin >> c;
		for (int i=0; i<c; i++){
			cin >> a >> b >> ab;
			comb[a][b] = comb[b][a] = ab;
		}
		cin >> o;
		for (int i=0; i<o; i++){
			cin >> a >> b;
			opose[a][b] = opose[b][a] = 1;
		}
		cin >> n;
		for (int i=0; i<n; i++){
			cin >> a;
			if (sz = res.size()){
				// testa se combina
				if(comb[a][res[sz-1]]) res[sz-1] = comb[a][res[sz-1]];
				else{ res+=a;
					
					// testa se opoe
					flag = 0;
					for (int j=0; j<sz; j++){
						if (opose[a][res[j]]){
							res = "";
							break;
						}
					}
				}
			}
			else res += a;
		}
		cout << "Case #" << t++ << ": [";
		sz = res.size();
		for (int i=0; i<sz-1; i++) cout << res[i] << ", ";
		if (sz) cout << res[sz-1] << "]\n";
		else cout << "]\n";
	}
	return 0;
}