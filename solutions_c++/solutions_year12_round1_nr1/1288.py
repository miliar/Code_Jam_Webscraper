/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/28/2012 06:27:08 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <iomanip>
using namespace std;

double p[1000000];
int main(){
	int a,b,T;
	cin >> T;
	for(int t=0;t<T;t++){
		cin >> a >> b;
		for(int i=0;i<a;i++)
			cin >> p[i];
		double best=b+2;
		double cp=1;
		for(int i=1;i<=a;i++){
			cp*=p[i-1];
			double newAns=cp*(a-i+b-i+1)+(1-cp)*(a-i+b-i+1+b+1);
			if(newAns<best)
				best=newAns;
		}
		cout << "Case #"<<t+1<<": " << fixed << setprecision(6) << best << endl;
	}

}
