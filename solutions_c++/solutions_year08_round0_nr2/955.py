#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int cases, t, na, nb;

int main(){	   
	priority_queue<int, vector<int>, greater<int> > Q;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &cases);
	for(int i=0; i<cases; ++i){
		scanf("%d%d%d", &t, &na, &nb);
		//Get NAs
		for(int j=0; j<na; ++j){
			int a,b,c,d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			Q.push(4*(a*60+b)+2);
			Q.push(4*(c*60+d+t));
		}
		// Get NBs	  	  
		for(int j=0; j<nb; ++j){
			int a,b,c,d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			Q.push(4*(a*60+b)+3);
			Q.push(4*(c*60+d+t)+1);
		}
		int a=0; int b=0;
		int cura=0; int curb=0;
		while(!Q.empty()){
			int x=Q.top();
			//dep from a
			if(x%4==2){
				if(cura==0){ a++; }
				else cura--;
			}	 	 
			//dep from b	
			if(x%4==3){
				if(curb==0){ b++; }
				else curb--;
			}
			//arrive at A
			if(x%4==1){
				cura++;
			}
			//arrive at B
			if(x%4==0){
				curb++;
			}
			Q.pop();
		}
		printf("Case #%d: %d %d\n", i+1, a, b);
	}
	return 0;
}

