#include <iostream>
#include <fstream>

using namespace std;

int group[1000];

void clear() {
	for(int i=0; i<1000; ++i) group[i] = 0;
}

inline long solve(int r, int k, int n) {
	int iHead = 0;
	long rslt = 0;
	
	for(int i=0; i<r; ++i) {
		int curr = 0;
		
		int tmpHead = iHead;
		while(curr <= k) {
			curr += group[tmpHead];
			if(tmpHead < n-1) ++tmpHead;
			else tmpHead = 0;
			
			if(iHead == tmpHead) break;
		}
		
		if(curr > k) {
			if(tmpHead > 0) {
				curr -= group[tmpHead-1];
				--tmpHead;
			} else {
				tmpHead = n-1;
				curr -= group[tmpHead];
			}
		}
		
		iHead = tmpHead;
		
		rslt += curr;
	}
	return rslt;
}

int main() {
	int r, k, n, t;
	
	ifstream file("C-large.in");
	ofstream ofile("C-small.out");
	
	file>>t;
	for(int i=0; i<t; ++i) {
		file>>r;
		file>>k;
		file>>n;
		
		clear(); 
		
		for(int j=0; j<n; ++j) file>>group[j];
		
		long sum = 0;
		for(int j=0; j<n; ++j) sum += group[j];
		
		if(k > sum) ofile<<"Case #"<<i+1<<": "<<r*sum<<endl;
		else ofile<<"Case #"<<i+1<<": "<<solve(r, k, n)<<endl;
		
		cout<<i<<endl;
	}
	
	file.close();
	ofile.close();
}