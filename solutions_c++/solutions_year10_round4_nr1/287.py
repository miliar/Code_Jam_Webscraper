#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
using namespace std;

int i,j,k,l,m,n,ri,repeat,v,flag;
char s[400][400];

int main(){
	freopen("A-large.in","r",stdin);freopen("w.txt","w",stdout);
	scanf("%d",&repeat);
	for(ri=1;ri<=repeat;ri++){
		printf("Case #%d: ",ri);
		memset(s,0,sizeof(s));
		scanf("%d",&k);
		getchar();
		for(i=0;i<2*k-1;i++){
			gets(s[i]);
		}
		for(l=k-1;l<=2*(k-1);l++){
			flag=0;
			for(i=0;i<2*k-1;i++){
				for(j=1;j<k;j++)
					if(s[i][l-j]!=s[i][l+j]&&isdigit(s[i][l-j])&&isdigit(s[i][l+j])){
						flag=1;
						goto found3;
					}
			}
			found3:
			if(flag==0)break;
			
			flag=0;
			int x=2*(k-1)-l;
			for(i=0;i<2*k-1;i++){
				for(j=1;j<k;j++)
					if(x-j>=0&&s[i][x-j]!=s[i][x+j]&&isdigit(s[i][x-j])&&isdigit(s[i][x+j])){
						flag=1;
						goto found;
					}
			}
			found:
			if(flag==0)break;
		}
		m=l-k+1;
		for(l=k-1;l<=2*(k-1);l++){
			flag=0;
			for(i=0;i<2*k-1;i++){
				for(j=1;j<k;j++)
					if(s[l-j][i]!=s[l+j][i]&&isdigit(s[l-j][i])&&isdigit(s[l+j][i])){
						flag=1;
						goto found2;
					}
			}
			found2:
			if(flag==0)break;
			
			flag=0;
			int x=2*(k-1)-l;
			for(i=0;i<2*k-1;i++){
				for(j=1;j<k;j++)
					if(x-j>=0&&s[x-j][i]!=s[x+j][i]&&isdigit(s[x-j][i])&&isdigit(s[x+j][i])){
						flag=1;
						goto found4;
					}
			}
			found4:
			if(flag==0)break;
		}
		l=l-k+1;
		int res=(k+l+m)*(k+l+m)-k*k;
		printf("%d\n",res);
	}
}
