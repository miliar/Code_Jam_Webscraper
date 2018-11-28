#include<iostream>
#include<cstdio>
#include<vector>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<string>
#include<algorithm>
char a[60][60];
int r,c;
bool work(void){
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(a[i][j]=='#'){
				if(i+1<r&&j+1<c&&a[i+1][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j+1]=='#'){
					a[i][j]=a[i+1][j+1]='/';
					a[i][j+1]=a[i+1][j]='\\';
				}
				else return false;
			}
		}
	}
	return true;
}
int main(void){
	freopen("in.in","r",stdin);
	freopen("out.in","w",stdout);
	int t,k;
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		printf("Case #%d:\n",k);
		scanf("%d%d",&r,&c);
		for(int i=0;i<r;i++)
			scanf("%s",&a[i]);
		if(work()){
			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					printf("%c",a[i][j]);
				}
				printf("\n");
			}
		}
		else printf("Impossible\n");
	}
	return 0;
}