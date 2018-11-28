#include<algorithm>
#include<stdlib.h>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<string.h>
#include<time.h>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#include<iostream>
using namespace std;


int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T, n, k;  char a[51][51], s[51][51];
	scanf("%d",&T);
	for(int tt=1; tt<=T; tt++){
		scanf("%d%d",&n,&k);
		for(int i=0; i<n; i++){
			scanf("%s",a[i]);
			for(int j=0; j<n; j++) s[i][j] = '.';
			for(int j=n-1,r=n-1; j>=0; j--){
				if( a[i][j]!='.' ) s[i][r--] = a[i][j];
			}
		}
		bool red = false, black = false;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if( s[i][j]!='R' ) continue;
				int len = 0;
				while( i-len>=0 && j+len<n && s[i-len][j+len]=='R' ) len++;
				if( len>=k ) red = true;
				
				len = 0;
				while( j+len<n && s[i][j+len]=='R' ) len++;
				if( len>=k ) red = true;
				
				len = 0;
				while( i+len<n && j+len<n && s[i+len][j+len]=='R' ) len++;
				if( len>=k ) red = true;

				len = 0;
				while( i+len<n && s[i+len][j]=='R' ) len++;
				if( len>=k ) red = true;
			}
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if( s[i][j]!='B' ) continue;
				int len = 0;
				while( i-len>=0 && j+len<n && s[i-len][j+len]=='B' ) len++;
				if( len>=k ) black = true;
				
				len = 0;
				while( j+len<n && s[i][j+len]=='B' ) len++;
				if( len>=k ) black = true;
				
				len = 0;
				while( i+len<n && j+len<n && s[i+len][j+len]=='B' ) len++;
				if( len>=k ) black = true;

				len = 0;
				while( i+len<n && s[i+len][j]=='B' ) len++;
				if( len>=k ) black = true;
			}
		}
		printf("Case #%d: ",tt);
		if( red && black ) printf("Both\n");
		else if( !red && !black ) printf("Neither\n");
		else if( red ) printf("Red\n");
		else printf("Blue\n");
	}
	return 0;
}
