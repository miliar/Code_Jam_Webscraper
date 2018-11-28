#include<iostream>
using namespace std;

long n,f,r,c,ans;
char map[11][7];

void do1(long x,long y,long d){
	long i,j,k;
	if(x==f && ans<d)ans=d;
	for(i=y-1;i>=0;i--){
		if(map[x][i]==0){
			for(j=x+2;j<=f;j++)
				if(map[j][i]==1)break;
				if(map[x+1][i]==1){
					if(j-1-x<=c)do1(j-1,i,d+1);
				}
				else {
					if(j-1-x<=c)do1(j-1,i,d);
										break;
				}
		}else break;
	}
	if(map[x][y-1]==0 || map[x][y+1]==0){
			for(j=x+2;j<=f;j++)
				if(map[j][y]==1)break;
				if(map[x+1][y]==1){
					if(j-1-x<=c)do1(j-1,y,d+1);
				}else if(j-1-x<=c)do1(j-1,y,d);
	}
	for(i=y+1;i<r;i++){
		if(map[x][i]==0){
			for(j=x+2;j<=f;j++)
				if(map[j][i]==1)break;
				if(map[x+1][i]==1){
					if(j-1-x<=c)do1(j-1,i,d+1);
				}else{
					if(j-1-x<=c)do1(j-1,i,d);break;
				}
		}else break;
	}
}

int main(){
	long h,i,j,k;
	scanf("%ld",&n);
	for(h=1;h<=n;h++){
		scanf("%ld%ld%ld",&f,&r,&c);
		ans=1000000;
		for(i=1;i<=f;i++)
			scanf("%s",map[i]);
		for(j=1;j<=f;j++)
			if(map[j+1][0]==1)break;
		do1(j,0,0);
		if(ans==1000000)printf("Case #%ld: No\n",h);
		else printf("Case #%ld: Yes %ld\n",h,ans);
	}
	return 0;
}
