#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	int T;
	int i=1;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin>>T;
	while(T--){
		int N,S,p,t,sThres,nsThres;
		int found=0;
		cin>>N>>S>>p;
		sThres = 3*p-4;
		nsThres = 3*p-2;		
		while(N--){
			cin>>t;
			if(t<p)
				continue;
			if(t>=nsThres)
				found++;
			else if(t>=sThres){
				if(S>0){
					found++;
					S--;
				}
			}
			else;
		}
		cout<<"Case #"<<i++<<": "<<found<<endl;
	}
	
	return 0;
}
