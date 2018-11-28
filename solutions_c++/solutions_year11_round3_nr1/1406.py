#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
int main()
{
freopen("out.txt","w",stdout);
freopen("in.txt","r",stdin);
int t;
char a[51][51];
scanf("%d",&t);
int n,m;

for(int z=1; z<=t; z++){
memset(a, 0, 51*51);
scanf("%d %d",&n,&m);
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
		cin>>a[i][j];
		}
	}
bool f=true;
for(int i=0; i<n-1; i++){
		for(int j=0; j<m-1; j++){
			if(a[i][j]=='#'&&a[i+1][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j+1]=='#')
			{
				a[i][j]='/';
				a[i+1][j]='\\';
				a[i][j+1]='\\';
				a[i+1][j+1]='/';
				j++;
			}
		}
		
	}

for(int i=0; i<n; i++){
	for(int j=0; j<m; j++){	
			if(a[i][j]=='#') f=false;
	}
}
printf("Case #%d:\n",z);
if(!f) printf("Impossible\n");
else
for(int i=0; i<n; i++){
		for(int j=0; j<m-1; j++)
		printf("%c", a[i][j]);	
	printf("%c\n", a[i][m-1]);
}
}
return 0;}
