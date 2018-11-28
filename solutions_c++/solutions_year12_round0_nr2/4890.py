/*
 * cj10q1b.cpp
 *
 *  Created on: Mar 19, 2012
 *      Author: rickyjeremiah
 */

#include <iostream>
#include <string>

using namespace std;
int main(){
	int n,s,p,t;
	cin>>t;
	for(int a=1; a<=t; a++){
		int sup = 0;
		int res = 0;
		cin >> n >> s >> p;
		for(int i=0 ;i<n ; i++){
			int temp;
			cin>>temp;
			if((temp == (p-1)*3) || (temp == (p-1)*3-1)){
				if(temp>=p){
					sup++;
				}
			}else if(temp > (p-1)*3){
				res++;
			}

		}

		if(sup>=s) res+=s;
		else res+=sup;
		cout << "Case #" << a <<": "<<res<< endl;
	}
	return 0;
}


