using namespace std;
#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#define vi vector<int>
#define sz size()
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int n;
		scanf("%d\n",&n);
		int O = 1,B=1,ltime = 0,rtime = 0; 
		int time=0;
		for(int i=0;i<n;i++){
			int num;
			char take;
			scanf("%c %d ",&take,&num);
			if(take=='O'){
				ltime +=abs(O-num);
				if(ltime<rtime) ltime=rtime;
				ltime++;
				O=num;
				time=ltime;
			}else{
				rtime+=abs(B-num);
				if(rtime<ltime) rtime=ltime;
				rtime++;
				B=num;
				time=rtime;
			}
		}
		printf("Case #%d: %d\n",caseno,time);
		caseno++;
	}
	return 0;
}
