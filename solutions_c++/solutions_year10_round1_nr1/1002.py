#include<iostream>
using namespace std;

int main(){
	freopen("D:\\A-large.in","r",stdin);	//////
	freopen("D:\\A-large.out","w",stdout);	//////
	int t,n,k,i,j,u,r,b;
	char start[55][55],rotate[55][55];
	bool red,blue;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d%d",&n,&k);
		for(j=0;j<n;j++)
			scanf("%s",start[j]);
		for(j=0;j<n;j++){
			for(u=0;u<n;u++){
				rotate[u][n-1-j]=start[j][u];
			}
		}
		for(j=0;j<n;j++){
			int sz=n-1;
			for(u=n-1;u>=0;u--){
				if(rotate[u][j]!='.'){
					char c=rotate[u][j];
					rotate[u][j]=rotate[sz][j];
					rotate[sz][j]=c;
					sz--;
				}
			}
		}
		red=blue=false;
		for(j=0;j<n;j++){
			r=b=0;
			for(u=0;u<n;u++){
				if(rotate[j][u]=='R'){
					b=0;
					r++;
					if(r>=k) red=true;
				}
				else if(rotate[j][u]=='B'){
					r=0;
					b++;
					if(b>=k) blue=true;
				}
				else{
					r=b=0;
				}
			}
		}
		for(j=0;j<n;j++){
			r=b=0;
			for(u=0;u<n;u++){
				if(rotate[u][j]=='R'){
					b=0;
					r++;
					if(r>=k) red=true;
				}
				else if(rotate[u][j]=='B'){
					r=0;
					b++;
					if(b>=k) blue=true;
				}
				else{
					r=b=0;
				}
			}
		}
		for(j=0;j<n*2-1;j++){
			r=b=0;
			for(u = j>=n? j%n+1:0;u<n && j-u>=0 && j-u<n;u++){
				if(rotate[u][j-u]=='R'){
					b=0;
					r++;
					if(r>=k) red=true;
				}
				else if(rotate[u][j-u]=='B'){
					r=0;
					b++;
					if(b>=k) blue=true;
				}
				else{
					r=b=0;
				}
			}
		}
		for(j=-n+1;j<n;j++){
			r=b=0;
			for(u=j<0? -j:0;u<n && j+u>=0 && j+u<n;u++){
				if(rotate[u][j+u]=='R'){
					b=0;
					r++;
					if(r>=k) red=true;
				}
				else if(rotate[u][j+u]=='B'){
					r=0;
					b++;
					if(b>=k) blue=true;
				}
				else{
					r=b=0;
				}
			}
		}
/*		printf("%d\n",k);
		for(j=0;j<n;j++){
			for(u=0;u<n;u++){
				putchar(rotate[j][u]);
			}
			putchar('\n');
		}*/
		if(red && blue)printf("Case #%d: Both\n",i);
		if(red && !blue)printf("Case #%d: Red\n",i);
		if(!red && blue)printf("Case #%d: Blue\n",i);
		if(!red && !blue)printf("Case #%d: Neither\n",i);
	}
	return 0;
}