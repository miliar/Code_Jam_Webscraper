/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/14/2012 10:17:52 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


int main(){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		int n,s,p;
		int ans=0;
		int a;
		cin >> n >> s >> p;
		for(int j=0;j<n;j++){
			cin >> a;
			if(2*max(p-1,0)+p<=a)
				ans++;
			else if(s && 2*max(0,p-2)+p<=a){
				ans++;
				s--;
			}
		}
		cout << "Case #" << t+1 << ": "<< ans << endl;
	}
}
