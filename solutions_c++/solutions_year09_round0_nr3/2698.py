#include <iostream>
#include <string>
using namespace std;

int main(){
	int n,len,count,cases;
	string input;
	
	cin >> n;
	cin.ignore();
	cases = 1;
	
	for(int i=0 ; i < n ; ++i){
		getline(cin,input);
		len = input.size();
		count = 0;
		
		for(int a=0 ; a < len ; ++a){
			if(input[a] == 'w'){
				for(int b=a ; b < len ; ++b){
					if(input[b] == 'e'){
						for(int c=b ; c < len ; ++c){
							if(input[c] == 'l'){
								for(int d=c ; d < len ; ++d){
									if(input[d] == 'c'){
										for(int e=d ; e < len ; ++e){
											if(input[e] == 'o'){
												for(int f=e ; f < len ; ++f){
													if(input[f] == 'm'){
														for(int g=f ; g < len ; ++g){
															if(input[g] == 'e'){
																for(int h=g ; h < len ; ++h){
																	if(input[h] == ' '){
																		for(int j=h ; j < len ; ++j){
																			if(input[j] == 't'){
																				for(int k=j ; k < len ; ++k){
																					if(input[k] == 'o'){
																						for(int l=k ; l < len ; ++l){
																							if(input[l] == ' '){
																								for(int m=l ; m < len ; ++m){
																									if(input[m] == 'c'){
																										for(int n=m ; n < len ; ++n){
																											if(input[n] == 'o'){
																												for(int o=n ; o < len ; ++o){
																													if(input[o] == 'd'){
																														for(int p=o ; p < len ; ++p){
																															if(input[p] == 'e'){
																																for(int q=p ; q < len ; ++q){
																																	if(input[q] == ' '){
																																		for(int r=q ; r < len ; ++r){
																																			if(input[r] == 'j'){
																																				for(int s=r ; s < len ; ++s){
																																					if(input[s] == 'a'){
																																						for(int t=s ; t < len ; ++t){
																																							if(input[t] == 'm'){
																																								++count;
																																							}
																																						}
																																					}
																																				}
																																			}
																																		}
																																	}
																																}
																															}
																														}
																													}
																												}
																											}
																										}
																									}
																								}
																							}
																						}
																					}
																				}
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
		cout << "Case #" << cases << ": ";
		if(count < 1000){
			if(count < 100){
				if(count < 10) cout << "000";
				else cout << "00";
			}
			else cout << "0";
		}
		cout << count << endl;
		++cases;
	}
	return 0;
}