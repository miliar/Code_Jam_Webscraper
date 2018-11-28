#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm>


using namespace std;



int main() {
	
	int T, N, tmp;
	double res;
	vector<int> l, copy;
	
	cin >> T;
	
	for(int x = 1; x <= T; x++) {
		l.clear();
		cin >> N;
		res = 0;
		for(int i = 0; i < N; i++) {
			cin >> tmp;
			l.push_back( tmp );
		}
		
		copy = l;
		
		sort(copy.begin(), copy.end());
		
		/*
		bool swapped = true;
		
		while(swapped) {
			swapped = false;
			for(int i = 1; i < N; i++) {
				if(l[i-1] > l[i]) {
					swap(l[i-1], l[i]);
					res += 2;
				
					swapped = 1;
				}
			
			}
		}*/
		
		
		
		for(int i = 0; i < N; i++) {
			if(l[i] != copy[i]) res++;
		}
		
		printf("Case #%d: %0.6f\n", x, res);
		
		
	
	
	} 
	
		
	
return 0;
}









