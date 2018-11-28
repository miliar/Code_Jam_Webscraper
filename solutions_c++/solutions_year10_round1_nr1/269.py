#include <stdio.h>
#include <iostream.h>
#include <string.h>

char s[51][51];

int red, blue ,k;

int search(int i, int j, int ii, int ij, int len){
	int t;
	for (t=1; t<len && s[i+ii*t][j+ij*t]==s[i][j]; t++);
	if (t>=k){
		if (s[i][j]=='R') red=1;
		else if (s[i][j]=='B') blue=1;
	}
	return t;
}

int main(){
	int t,u,i,j,n,l,a;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>n>>k;
		red=blue=0;
		for (i=0; i<n; i++) cin>>s[i];
		for (i=0; i<n; i++){
			for (j=l=n-1; j>=0; j--,l--){
				while(s[i][j]=='.' && j>=0) j--;
				if (j<0) break;
				s[i][l]=s[i][j];
			}
			while(l>=0) s[i][l--]='.';
		}
		//H
		for (i=0; i<n; i++){
			for (j=0; j<n; j+=a){
				a=search(i,j,0,1,n-j);
			}
		}
		//V
		for (i=0; i<n; i++){
			for (j=0; j<n; j+=a){
				a=search(j,i,1,0,n-j);
			}
		}
		//D
		for (i=0; i<n; i++){
			for (j=0; j<n-i; j+=a){
				a=search(i+j,j,1,1,n-i-j);
			}
			for (j=0; j<n-i; j+=a){
				a=search(j,i+j,1,1,n-i-j);
			}
		}
		//E
		for (i=0; i<n; i++){
			for (j=0; j<n-i; j+=a){
				a=search(n-1-(i+j),j,-1,1,n-i-j);
			}
			for (j=0; j<n-i; j+=a){
				a=search(n-1-j,i+j,-1,1,n-i-j);
			}
		}
		printf("Case #%d: ",u+1);
		if (red&&blue) printf("Both\n");
		else if (red) printf("Red\n");
		else if (blue) printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}
