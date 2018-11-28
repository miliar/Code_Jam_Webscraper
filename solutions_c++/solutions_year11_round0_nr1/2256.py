#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
vector< set<int> > a;
int n,sz,g,h,m,i,j,c,T,pos1,pos2,i1,i2;
vector< int> r1,r2;
vector< vector<int> > k;
vector<bool> hod;

int main(){
	freopen("input.in","r",stdin);
	freopen("input.out","w",stdout);
	char ch;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		r1.clear();
		r2.clear();
		scanf("%d",&n);
		hod.resize(n);
		for(i=0;i<n;i++){
			scanf(" %c%d",&ch,&h);
			if(ch=='O')r1.push_back(h); else r2.push_back(h);
			hod[i]=(ch=='O');
		}
		pos1=pos2=1;
		i1=i2=0;
		c=0;
		g=0;
		while(i1<r1.size() || i2<r2.size()){
			c++;
			if(!hod[g]){
				if(i1<r1.size()){
					if(r1[i1]!=pos1){					
						if(pos1<r1[i1])pos1++; else pos1--;
					}else if(hod[g]){i1++;g++;}
				}
				if(i2<r2.size()){
					if(r2[i2]!=pos2){
						if(pos2<r2[i2])pos2++; else pos2--;
					}else if(!hod[g]){i2++;g++;}
				}
			}else{
				if(i2<r2.size()){
					if(r2[i2]!=pos2){
						if(pos2<r2[i2])pos2++; else pos2--;
					}else if(!hod[g]){i2++;g++;}
				}
				if(i1<r1.size()){
					if(r1[i1]!=pos1){					
						if(pos1<r1[i1])pos1++; else pos1--;
					}else if(hod[g]){i1++;g++;}
				}
			}
			
		}
		printf("Case #%d: %d\n",t+1,c);
		
	}
	
return 0;
}

//Powered by [KawigiEdit] 2.0!