/*
 * ThemePark.cpp
 *
 *  Created on: May 8, 2010
 *      Author: akshay
 */

#include <iostream>

using namespace std;

int main() {
	int T;
	unsigned long R, k;
	int N, g[1000];
	int start;
	int curr;
	unsigned long sum;
	unsigned long long earn;
	bool circle;
	
	cin>>T;
		
	for(int t=0; t<T; t++) {
		cin>>R>>k>>N;
		for(int i=0; i<N; i++)
			cin>>g[i];
		
		start = 0;
		earn = 0;
		
		for(unsigned long r=0; r<R; r++) {
			sum = 0;
			curr = start;
			circle = false;
			
			while(sum + g[curr] <= k) {
				sum += g[curr];
				curr++;
				
				if(curr == N)
					curr = 0;
				
				if(curr == start)
					break;
			}
			
			earn += sum;
			start = curr;
		}
		
		cout<<"Case #"<<(t+1)<<": "<<earn<<endl;
	}
}
