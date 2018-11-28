#include <iostream>

using namespace std;

int main(){
	int n, ni, comc, oppc, p, ec, i, j;
	char c1, c2, c3, c;
	bool cmb;
	char e[101];
	char com['Z'-'A'+1]['Z'-'A'+1];
	char opp['Z'-'A'+1]['Z'-'A'+1];
	
	cin >> n;

	for (ni = 1; ni <= n; ni++){

		ec = 0;

		for (i = 0; i <= 'Z'-'A'; i++)
			for (j = 0; j <= 'Z'-'A'; j++){
				com[i][j] = '.';
				opp[i][j] = '.';
			}

		cin >> comc;
		for (i = 0; i < comc; i++){
			cin >> c1 >> c2 >> c3;
			com[c1-'A'][c2-'A'] = c3;
			com[c2-'A'][c1-'A'] = c3;
		}
		cin >> oppc;
		for (i = 0; i < oppc; i++){
			cin >> c1 >> c2;
			opp[c1-'A'][c2-'A'] = '!';
			opp[c2-'A'][c1-'A'] = '!';
		}

		cin >> p;
		
		for (i=0; i<p; i++){
			cin >> c;
			e[ec] = c;
			ec++;
			if ((ec > 1) && (com[e[ec-1]-'A'][e[ec-2]-'A'] != '.')){
					e[ec-2] = com[e[ec-1]-'A'][e[ec-2]-'A'];
					ec--;
			}else{
				for (j=0; j<ec-1; j++) if (opp[e[j]-'A'][e[ec-1]-'A'] != '.'){
					ec=0;
					break;
				}
			}
		}
		
		cout << "Case #" << ni << ": [";
		for (i=0; i<ec; i++){
			cout << e[i];
			if (i < ec-1) cout << ", ";
		}
		cout << "]" << endl;
	}
}
