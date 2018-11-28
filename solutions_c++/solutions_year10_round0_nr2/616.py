#include <iostream>
#include <fstream>
#include <iomanip>
#include "zzn.h"

using namespace std;

#ifndef MR_NOFULLWIDTH
Miracl precision(50,0);
#else
Miracl precision(50,MAXBASE);
#endif

Big time[1000];
Big dif[1000000];
int n;

Big process(){
	Big sol=0;
	Big gre=0;
	int i,j,flag = 0;
	int cnt = 0;
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			if(time[i] - time[j] == 0) continue;
			if(abs(time[i]-time[j]) == 1) flag = 1;
			dif[cnt++] = abs(time[i]-time[j]);
		}
	}
	if(flag) sol = 0;
	else{
		if(n == 2) gre = dif[0];
		else{
			gre = gcd(dif[0],dif[1]);
			for(i=2;i<cnt;i++){
				gre = gcd(gre,dif[i]);
			}
		}
		Big Rem = time[0] % gre;
		if(Rem != 0) sol = gre - Rem;
	}
	return sol;
}

int main(){
	int i,j,T;
	Big ans;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in >> T;
	for(i=1;i<=T;i++){
		in >> n;
		for(j=0;j<n;j++){
			in >> time[j];
		}
		ans = process();
		out << "Case #" << i << ": " << ans << endl;
	}
	fcloseall();
	return 0;
}