#include <iostream>

using namespace std;

int main(){
				int L, D, N;
				string word[5010];
				bool letter[16][30];

				cin >> L >> D >> N;
				for (int i=0; i<D; ++i){
								cin >> word[i];
				}
				for (int i=0; i<N; ++i){
								memset(letter, 0, sizeof(letter));
								for (int j=0; j<L; ++j){
												char c;
												cin >> c;
												if (c!='('){
																letter[j][c-'a'] = true;
//																cout << c;
												} else {
//																cout << "(";
																do {
																				cin >> c;
																				if (c!=')'){
																								letter[j][c-'a'] = true;
//																								cout << c;
																				}
																} while (c!=')');
//																cout << ")";
												}
								}
//								cout << endl;
								int count = 0;
								for (int j=0; j<D; ++j){
												bool okay = true;
												for (int k=0; k<L; ++k){
																if (!letter[k][word[j][k]-'a'])
																				okay = false;
												}
												if (okay) 
																count++;
								}
								cout << "Case #" << i+1 << ": " << count << endl;

				}
				return 0;
}
