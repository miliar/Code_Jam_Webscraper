#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main ()
{
    freopen ("A-small.in","r",stdin);
    freopen ("A-small.out","w",stdout);
int t=0;
cin >> t;
int a=1;
int out=0;

while (a<=t) {
	int n,s,p;
	cin >> n >> s >> p;
	
	int u=0;
	int q;
	out=0;
	while (u<n) {
		cin >> q;
		if (q%3==0 and q!=0) {
			if (q/3>=p) {
				out++;
			}
			else if ((q/3)+1>=p and s>0) {
			out++;
			s--;
				
			}
		}
		if (q%3==1 and q!=1) {
					if ((q/3)+1>=p) {
						out++;
					}
				}
				if (q%3==2) {
							if ((q/3)+1>=p) {
								out++;
							}
							else if ((q/3)+2>=p and s>0) {
							out++;
							s--;
								
							}
						}
						if (q==0 and p==0) {
									
												out++;
											
										}
										if (q==1 and p<2) {
																			
																						out++;
																					
																				}
																				u++;
	}
	cout << "Case #"<< a << ": "<<out<<endl;
	a++;
}
}
