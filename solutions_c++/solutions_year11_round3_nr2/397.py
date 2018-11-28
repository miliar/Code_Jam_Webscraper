/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/07/2011 09:33:17 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main(){
	unsigned int T, L, C, N;
	long t, ot;
	unsigned int a[1000];
	cin >> T;
	for(int i = 0 ; i  < T; ++i){
		cout << "Case #"<<i+1 <<": ";
		
		cin >> L >> t >> N >> C;
		ot = t;
		unsigned int max = -1;
	        int maxid = -1;
		for(int j = 0; j < C; ++j){
			cin >> a[j];
			if(a[j] > max) max = a[j];
			maxid = j;
		}
		vector<unsigned int> vals;
		for(int j = 0; j < N; ++j){
			unsigned int val = a[j%C];
			if(t < val*2){
				vals.push_back(val - t/2);
				t = 0;
			}
			else{
				t -= val*2;
			}
		}
		sort(vals.begin(), vals.end());
		long ret = 0;
		if(t > 0) ret = ot - t;
		else{
			ret += ot;
			for(int j = vals.size() - 1; j >= 0; --j){
				//cout << vals[j] << endl;
				if(L > 0){
					ret += vals[j];
					--L;
				}
				else{
					ret += vals[j] * 2;
				}
			}
		}
		cout << ret << endl;
	}
}
