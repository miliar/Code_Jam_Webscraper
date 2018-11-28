#include <stdlib.h>
#include <stdio.h>
#include <set>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int power[8] = {1,10,100,1000,10000,100000,1000000,10000000};
/*
int pow(int n){
	switch(n){
	case 0: return 1;
	case 1: return 10;
	case 2: return 100;
	case 3: return 1000;
	case 4: return 10000;
	case 5: return 100000;
	case 6: return 1000000;
	case 7: return 10000000;
	default: return 1;
	}
}
*/
int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int h=0;
	scanf("%d\n",&h);
	for(int t=0;t<h;t++){
		int a,b;
		scanf("%d %d",&a,&b);
		int result = 0;
		set<int> ccc;
		char buf[10];
		itoa(a,buf,10);
		int n = strlen(buf);
		for(int i=a;i<b;i++){
			
			//string g;
			ccc.clear();
			
			for(int j=1;j<n;j++)
			{
				
				//g.clear();
				int p1 = power[j];
				int p2 = power[n-j];

				//for(int k=0;k<strlen(buf);k++){
				//	g+=buf[(j+k)%strlen(buf)];
				//}
				//int d = atoi(g.c_str());
				int d= i/p1+(i%p1)*p2;
				if(i<d && d<=b ){//&& ccc.count(d)==0) {
					if(ccc.count(d)==0){
						//printf("%d %d\n",i,d);
						result++;
						ccc.insert(d);
					}
					else break;
				}
			}
		}
		//printf("\n");
		printf("Case #%d: %d\n",t+1,result);
	}
	return 0;
}