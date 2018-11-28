#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>

#include <algorithm>
#include <map>
#include <vector>

using namespace std;


int ti[101];


bool compare(int x, int y) {
	return x>y;
}

int main() {
	int T;
	
	cin>>T;
	int cas=0;
	
	int N, S, p;
	
	while (cas++<T) {
		cin>>N>>S>>p;
		
		for (int i=0;i<N;++i)
			cin>>ti[i];
		
		
//		sort(ti, ti+N, compare);
		
		int res=0;
		
		for (int i=0;i<N;++i) {
			int z= ti[i]/3;
			
			if (ti[i]==1) z++;
			if (z>=p) {res++;continue;}
			if (ti[i]<2) continue;
			
			int md;
			
			md = ti[i]%3;
			
			
			if (md==0) {

				if (S&&z+1>=p) {
					S--;
					res++;
					continue;
				}
			}
			
			if (md==1) {
				if (z+1>=p) {
					res++;
					continue;
				}
			}
			
			if (md==2) {
				if (z+1>=p) {
					res++;
					continue;
				}
				
				if (S&&z+2>=p) {
					S--;
					res++;
					continue;
				}
			}
		}
		
		cout<<"Case #"<<cas<<": "<<res<<endl;
	}
	
	
	
	return 0;
}


