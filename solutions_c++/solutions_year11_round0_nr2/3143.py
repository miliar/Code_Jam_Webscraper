/*
 * Magicka.cpp
 *
 *  Created on: 2011/05/08
 *      Author: masamichi1222
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	int T, C, D, N;
	string temp;
	vector <string> cst;
	vector <string> dst;
	string nst;
	vector <char> ans;

	cin >> T;
	for(int i=0; i<T; i++){
		cin >> C;
		cst.clear();
		for(int s=0; s<C; s++){
			cin >> temp;
			cst.push_back(temp);
		}
		//		for(int s=0; s<C; s++) cout << cst[s] << endl;


		cin >> D;
		dst.clear();
		for(int s=0; s<D; s++){
			cin >> temp;
			dst.push_back(temp);
		}
		//		for(int s=0; s<D; s++) cout << dst[s] << endl;

		cin >> N;
		cin >> nst;
		//		cout << nst << endl;

		ans.clear();

		cout << "Case #" << i+1 << ": [";
		ans.push_back(nst[0]);
		for(int t=1; t<N; t++){
			ans.push_back(nst[t]);
			for(int s=0; s<C; s++){
				if(C!=0){
					if((cst[s][0]==ans[ans.size()-2] && cst[s][1]==ans[ans.size()-1]) || (cst[s][1]==ans[ans.size()-2] && cst[s][0]==ans[ans.size()-1])){
						ans.pop_back();
						ans.pop_back();
						ans.push_back(cst[s][2]);
						break;
					}
				}
			}
			for(int s=0; s<D; s++){
				if(D!=0){
					for(int m=0; m<(int)ans.size()-1; m++){
						if((dst[s][0]==ans[ans.size()-1] && dst[s][1]==ans[m]) || (dst[s][1]==ans[ans.size()-1] && dst[s][0]==ans[m])){
							ans.clear();
							break;
						}
					}
				}
			}
		}

		if(ans.size()!=0) cout << ans[0];
		for(int k=1; k<(int)ans.size(); k++) cout << ", " << ans[k];

		cout << "]" << endl;
	}

	return 0;
}
