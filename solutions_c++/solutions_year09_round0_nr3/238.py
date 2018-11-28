#include <iostream>

using namespace std;

int main(){
				int n;

				string s;
				string target="welcome to code jam";
				int k = target.length();

				cin >> n >> ws;
				for (int cnt=0; cnt<n; ++cnt){
								getline(cin, s);
								int m = s.length();	

								int fit[500][20];
								if (s[0] == target[0])
												fit[0][0] = 1;
								else 
												fit[0][0] = 0;
								for (int i=1; i<m; ++i){
												if (s[i] == target[0]){
														fit[i][0] = fit[i-1][0]+1;
												} else {
														fit[i][0] = fit[i-1][0];
												}
								}
								for (int j=1; j<k; ++j){
												fit[0][j] = 0;
								}
							
								for (int j=1; j<k; ++j)
										for (int i=1; i<m; ++i){
																if (s[i] != target[j])
																				fit[i][j] = fit[i-1][j];
																else 
																				fit[i][j] = (fit[i-1][j] + fit[i-1][j-1]) % 10000;
										}
								int ans = fit[m-1][k-1];

								cout << "Case #" << cnt+1 << ": ";
								if (ans>=1000)
												cout << ans << endl;
								else if (ans>=100)
												cout << "0" << ans << endl;
								else if (ans>=10)
												cout << "00" << ans << endl;
								else cout << "000" << ans << endl;


				}

				return 0;
}
