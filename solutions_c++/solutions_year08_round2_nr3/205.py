#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int num=0;num<t;num++) {
		int h(0);
		vector<int> data;
		int k,n,tab[5010],x,track[5010];
		memset(track,-1,sizeof(track));
		cin >> k >> n;
		for(int i=0;i<n;i++) {cin >> x; data.push_back(x);}
		memset(tab,0,sizeof(tab));
		
		int p(0),a(1),c(1);
		while(a<=k) {
			h++;
			if(h%1000==0) {
				//printf("ECHO");
				bool ok(false);
				int pos;
				for(int i=0;i<k;i++) {
					if(tab[i] && !ok) ok = true,pos=i;
					if(!tab[i] && ok) ok = false,track[pos] = i;
				}
			}
			if(tab[p]==0 && c==a) tab[p] = a,a++,c=0;
			if(track[p]!=-1) p = track[p]; else p = (p+1) %k;
			if(tab[p]==0) c++;
		}
		
		printf("Case #%d:",num+1);
		for(int i=0;i<data.size();i++) printf(" %d", tab[ data[i]-1 ]);
		printf("\n");
	}
	return 0;
}
