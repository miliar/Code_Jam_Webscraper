#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main(){
	int T,n;
	int i,j,k,x,y,t1,t2,t;
	char c;
	
	j = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		
		x = 1; y = 1;
		t1 = t2 = t = 0;
		for(i=0;i<n;i++){
			cin>>c>>k;
			if(c == 'O'){
				t = max(t,t1 + abs(k-x));
				t++;
				x = k; t1 = t;
			}
			else{
				t = max(t,t2 + abs(k-y));
				t++;
				y = k; t2 = t;			
			}
		}
		printf("Case #%d: %d\n",j,t);
		j++;
	}
	return 0;
}
			
