#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip.h>
#include <string>
using namespace std;

int power10(int digi){
		if (digi==0) return 1;
		if (digi==1) return 10;
		if (digi==2) return 100;
		if (digi==3) return 1000;
		if (digi==4) return 10000;
		if (digi==5) return 100000;
		return 1;
}

int digi(int number){
		if (number<10) return 1;
		if (number<100) return 2;
		if (number<1000) return 3;
		if (number<10000) return 4;
		if (number<100000) return 5;
}
int main(int argc, char *argv[]){
		ifstream ins;
		ins.open(argv[1]);
		int Ncase;
		ins>>Ncase;
		int the_case = 0;
		while (the_case++ < Ncase){
				int A, B;
				ins>>A>>B;   
				int counter = 0 ;
				for (int n=A; n<B; ++n){
						for (int m=n+1; m<=B; ++m){
								if (digi(n)!=digi(m))
										continue;
								int digit = digi(n);
								int new_n = n;
								int old_n[digit];
								int counter_m = 0;
								for (int k=0; k<digit; ++k){
										new_n = new_n/10 + new_n%10*power10(digit-1);
										old_n[k]=new_n;
										int bad = false;
										for (int j = 0; j<k; ++j){
												if (new_n==old_n[j]) 
														bad = true;
										}
										if (!bad && new_n == m){ counter++;
												counter_m ++;
												//cout<< n<<" "<<new_n <<" "<<m<<endl;
												//if (counter_m>1) cout<<"------------------------------"<<endl;
										}
								}
						}
				}
				cout<<"Case #"<<the_case<<": "<<counter<<endl;
		}
		ins.close();
		return 0;
}


