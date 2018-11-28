#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main ()
{
    freopen ("A-small.in","r",stdin);
    freopen ("A-small.out","w",stdout);
int n=0;
cin >> n;
int a=1;
string s;
	getline(cin, s);
while (a<=n) {
	getline(cin, s);
	int l=s.size();
	int u=0;
	cout << "Case #"<< a << ": ";
	while (u<l) {
		char c =s[u];
		if (c=='a') {
			cout << "y";
		}
		if (c=='b') {
					cout << "h";
				}
		if (c=='c') {
					cout << "e";
				}		
		if (c=='d') {
				cout << "s";
			}
		if (c=='e') {
					cout << "o";
				}	
				if (c=='f') {
							cout << "c";
						}
						if (c=='g') {
									cout << "v";
								}
						if (c=='h') {
									cout << "x";
								}		
						if (c=='i') {
								cout << "d";
							}
						if (c=='j') {
									cout << "u";
								}
		if (c=='k') {
					cout << "i";
				}
				if (c=='l') {
							cout << "g";
						}
				if (c=='m') {
							cout << "l";
						}		
				if (c=='n') {
						cout << "b";
					}
				if (c=='o') {
							cout << "k";
						}	
						if (c=='p') {
									cout << "r";
								}
								if (c=='q') {
											cout << "z";
										}
								if (c=='r') {
											cout << "t";
										}		
								if (c=='s') {
										cout << "n";
									}
								if (c=='t') {
											cout << "w";
										}		
										if (c=='u') {
															cout << "j";
														}
														if (c=='v') {
																	cout << "p";
																}
														if (c=='w') {
																	cout << "f";
																}		
														if (c=='x') {
																cout << "m";
															}
														if (c=='y') {
																	cout << "a";
																}	
																if (c=='z') {
																			cout << "q";
																		}
																		if (c==' ') {
																																					cout << " ";
																																				}
																																				u++;				
	}
	
	cout << endl; 
	a++;
}
}
