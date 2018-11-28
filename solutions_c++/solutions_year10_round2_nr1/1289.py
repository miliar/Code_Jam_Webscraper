#include <iostream>
#include <string>
#include <vector>

#define Max 200

using namespace std;



void read(int limit, vector<string> io[Max]){
	for (int i = 0; i < limit; ++i){
		string tmp, tmpword;
		cin >> tmp;
		for (int k = 1; k < tmp.size(); ++k){
			if (tmp[k] != '/' ){
				tmpword += tmp[k];
			}
			else {
				io[i].push_back(tmpword);
				tmpword = "";
			}
		}
		io[i].push_back(tmpword);
		//cout << tmpword << endl;
	}
}
int main(){
	int cases, exist, create;
	cin >> cases ;
	//cout << cases << exist << create << endl;
	for (int m = 0; m < cases; ++m){
		cin >> exist >> create;
		vector<string> exi[Max];
		vector<string> cre[Max];
		int res = 0;
		read(exist, exi);
		read(create, cre);
		for (int i = 0; i < create; ++i){
			for (int j = 0; j < cre[i].size(); ++j){
				bool find = false;
				//cout << "s" << endl;
				for (int k = 0; k < exist; ++k){
					if (j >= exi[k].size()){
						continue;
					}
					else if (cre[i][j] == exi[k][j]){
						bool equ = true;
						for (int l = 0; l < j; ++l){
							if (cre[i][l] != exi[k][l])
								equ = false;
						}
						if (equ){
						//	cout << exi[k][j] << k << " " << j << endl;
							find = true;
							break;
						}
					}
				}
				if (!find){
					res += cre[i].size() - j;
					//cout << cre[i].size() << " " << j << " " << cre[i][j] << " " << res << endl;
					for (int k = 0; k < cre[i].size(); ++k)
						exi[exist].push_back(cre[i][k]);
					exist ++;
					break;
				}
			}
		}
		cout << "Case #" << m + 1 << ": " << res << endl;
	}
	return 0;
}