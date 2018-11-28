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
	int T, N;
	cin >> T;
	for(int i = 0 ; i  < T; ++i){
		cin >> N;
		//O = 0, B= 1
		vector<int> seq[2];
		vector<int> order;
		char r;
		int b ;
		for(int k = 0; k < N; ++k){
			cin >> r;
			cin  >> b;
			seq[r == 'B'].push_back(b);
			order.push_back(r == 'B');
		}
		int ret = 0;
		int curr[2]={1,1};
		int curri[2] = {0, 0};
		int j = 0;
		//copy(seq[0].begin(), seq[0].end(), ostream_iterator<int> (cout, " "));
		//cout << order.size();
		while(j < order.size()){
			int now = order[j];
			if(seq[now][curri[now]] > curr[now]){
				curr[now]++;
			}
			else if(seq[now][curri[now]] < curr[now]){
				curr[now]--;
			}
			else{
				j++;
				curri[now]++;

			}
			
			now = (now + 1)%2;
			if(seq[now].size() > curri[now]){
				if(seq[now][curri[now]] > curr[now]){
					curr[now]++;
				}   
				else if(seq[now][curri[now]] < curr[now]){
					curr[now]--;
				}
			}
			ret ++;
		}
		cout << "Case #"<<i+1 <<": "<< ret << endl;
	}
}
