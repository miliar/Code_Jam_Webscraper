#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <cctype>
#include <math.h>
using namespace std;

int n,e,q;
string engine[150];
int dp[1011][111];
map<string,int> m;
int BIG=1000000000;

int main(){
	int i,j,k;
	string temp;
	char temps[10000],dumi;
	
	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%d%c",&e,&dumi);
		for (j=0;j<e;j++){
			gets(temps);
			engine[j]=temps;
			m[engine[j]]=j;
		}
		scanf("%d%c",&q,&dumi);
		int use=0,minim=0,idmin=BIG;
		for (j=1;j<=q;j++){
			gets(temps);
			temp=temps;
			
			int minimnext=BIG;
			for (k=0;k<e;k++){
				if (engine[k]==temp){
					dp[j][k]=BIG;	
				} else {
					if (dp[j-1][k]==minim) dp[j][k]=minim; else
									   dp[j][k]=minim+1;
				}
				minimnext=min(minimnext,dp[j][k]);
			}
			minim=minimnext;
		}	
		printf("Case #%d: %d\n",i+1,minim);
	}
	return 0;	
}
