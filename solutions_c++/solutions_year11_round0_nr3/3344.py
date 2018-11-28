/*
 * =====================================================================================
 *
 *       Filename:  c.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/07/2011 10:56:10 AM
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
#include <iterator>
#include <algorithm>

using namespace std;
unsigned long long for15(vector<unsigned int> &all, int N, unsigned long long  sum, unsigned int total);
int main(){
	int T,N;
	cin >> T;
	for(int t =0 ; t < T; ++t){
		cin >> N;
		vector<unsigned int> all;
		unsigned long long sum;
		unsigned int total;
		cin >> total;
		all.push_back(total);
		sum = total;
		for(int i =1 ; i < N; ++i){
			unsigned int n;
			cin >> n;
			all.push_back(n);
			total ^= n;
			sum += n;
		}
		//cout << total <<endl;
		cout << "Case #"<<t + 1<<": ";
		if(total != 0){
			cout << "NO";
		}
		else{
			sort(all.begin(), all.end());
			unsigned long ret = 0;
			if( N <= 15){
				cout << for15(all, N, sum, total);
			}
		}
		cout << endl;
	}
}

unsigned long long for15(vector<unsigned int> &all, int N, unsigned long long  sum, unsigned int total){
	int sz = 1 << N;
	unsigned long long ret = 0;
	for( int i = 1; i < sz -1; i++){
		unsigned long long tempsum = 0;
		unsigned int temp = 0;
		for( int j = 0 ; j < all.size(); j++){
			if( (i & (1 << j)) > 0 ){
				tempsum +=  all[j];
				temp ^= all[j];
			}
		}
		if(temp == (total^temp) ) {
			if(ret < tempsum) ret = tempsum;
		}
	}
	return ret;
}

