#include <stdio.h>
#include <iostream>
#include <memory.h>
#define N 55

using namespace std;
char f[N][N];
char temp[N];

int main(int argc, char **argv)
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	int index = 1;
	scanf("%d", &t);
	while(t--) {
		int n, k;
		bool R=0, B=0;
		memset(f, 0, sizeof(f));
		memset(temp, 0, sizeof(temp));
		scanf("%d%d", &n, &k);
		int i, j;
		for(i = 0; i < n; i++) {
			scanf("%s", f[i]);
			getchar();
		}
		//Rotate it
		for(i = 0; i < n; i++) {
			int ip = n-1;
			for(j = n-1; j >=0; j--) {
				if(f[i][j] != '.') {
					f[i][ip--] = f[i][j];
				}
				if(j != ip+1) {
					f[i][j] = '.';
				}
			}
		}
//		for(i=0;i<n;i++) {
//			clog<<f[i]<<endl;
//		}
		//judge heng
		for(i=0;i<k;i++) {
			temp[i]='R';
		}
		for(i = 0; i < n;i++) {
			if(strstr(f[i], temp)!=NULL) {
				R=1;
				break;
			}
		}
		for(i=0;i<n;i++) {
			char temp2[N];
			for(j=0;j<n;j++) {
				temp2[j]=f[j][i];
			}
			temp2[j]=0;
		//	clog<<temp2<<"  "<<temp<<endl;
			if(strstr(temp2,temp)!=NULL) {
				R=1;
				break;
			}
		}
		for(i=k-1;i<n;i++) {
			char temp2[N];
			int it=0;
			for(j=0;1;j++) {
				if(i-j<0) break;
				temp2[it++]=f[j][i-j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				R=1;
				break;
			}
		}
		for(i=n+1-k;i>=0;i--) {
			char temp2[N];
			int it=0;
			for(j=n-1;1;j--) {
				if(i-j>k) break;
				temp2[it++]=f[j][i+n-1-j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				R=1;
				break;
			}
		}
		for(i=n+1-k;i>=0;i--) {
			char temp2[N];
			int it=0;
			for(j=0;1;j++) {
				if(i+j>n) break;
				temp2[it++]=f[j][i+j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				R=1;
				break;
			}
		}
		for(i=k-1;i<n;i++) {
			char temp2[N];
			int it=0;
			for(j=n-1;1;j--) {//////////////
				if(i-n+1+j<0) break;
				temp2[it++]=f[j][i-n+1+j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				R=1;
				break;
			}
		}
		//here
		for(i=0;i<k;i++) {
			temp[i]='B';
		}
		for(i = 0; i < n;i++) {
			if(strstr(f[i], temp)!=NULL) {
				B=1;
				break;
			}
		}
		for(i=0;i<n;i++) {
			char temp2[N];
			for(j=0;j<n;j++) {
				temp2[j]=f[j][i];
			}
			temp2[j]=0;
			if(strstr(temp2,temp)!=NULL) {
				B=1;
				break;
			}
		}
		for(i=k-1;i<n;i++) { ///////////
			char temp2[N];
			int it=0;
			for(j=0;1;j++) {
				if(i-j<0) break;
				temp2[it++]=f[j][i-j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				B=1;
				break;
			}
		}
		for(i=n+1-k;i>=0;i--) {
			char temp2[N];
			int it=0;
			for(j=n-1;1;j--) {
				if(i-j>k) break;
				temp2[it++]=f[j][i+n-1-j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				B=1;
				break;
			}
		}
		for(i=n+1-k;i>=0;i--) {
			char temp2[N];
			int it=0;
			for(j=0;1;j++) {
				if(i+j>n) break;
				temp2[it++]=f[j][i+j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				B=1;
				break;
			}
		}
		for(i=k-1;i<n;i++) {
			char temp2[N];
			int it=0;
			for(j=n-1;1;j--) {//////////////
				if(i-n+1+j<0) break;
				temp2[it++]=f[j][i-n+1+j];
			}
			temp2[it]=0;
//			clog<<temp2<<endl;
			if(strstr(temp2,temp)!=NULL) {
				B=1;
				break;
			}
		}
		printf("Case #%d: ", index++);
		if(R) {
			if(B) {
				puts("Both");
			}
			else {
				puts("Red");
			}
		}
		else {
			if(B) {
				puts("Blue");
			}
			else {
				puts("Neither");
			}
		}
	}
	return 0;
}
