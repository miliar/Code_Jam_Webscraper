#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;


void opens(){
	freopen("Asmall.in","r",stdin);
	freopen("Asmall.out","w",stdout);
}

void openb(){
	freopen("Alarge.in","r",stdin);
	freopen("Alarge.out","w",stdout);
}

#define MAXN 101
int n,k,t;
char s[MAXN][MAXN],s2[MAXN][MAXN];

int main(){
	opens();
	//openb();
	scanf("%d",&t);
	int xx=1;
	while (t--){
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++){
			scanf("%s",&s[i]);
		}
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				s2[i][j]=s[n-j-1][i];
				//printf("%c",s2[i][j]);
			}
			//printf("\n");
		}
		for (int i=0;i<n;i++){
			for (int j=n-1;j>=0;j--){
				if (s2[j][i]!='.' && s2[j+1][i]=='.'){
					int now,next;
					now=j;
					next=j+1;
					while (next<n && s2[next][i]=='.'){
						char tmp=s2[next][i];
						s2[next][i]=s2[now][i];
						s2[now][i]=tmp;
						now++;
						next++;
					}
				}
			}
		}
		/*printf("\n");
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				printf("%c",s2[i][j]);
			}
			printf("\n");
		}*/
		bool red,blue;
		red=0;blue=0;
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				//datar
				bool validr,validb;
				validr=1;validb=1;
				for (int r=0;r<k;r++){
					if (j+r>=n || s2[i][j+r]!='R'){
						validr=0;
						break;
					}
				}
				for (int r=0;r<k;r++){
					if (j+r>=n || s2[i][j+r]!='B'){
						validb=0;
						break;
					}
				}
				if (validr) red=1;
				if (validb) blue=1;
				//bawah
				validr=1;validb=1;
				for (int r=0;r<k;r++){
					if (i+r>=n || s2[i+r][j]!='R'){
						validr=0;
						break;
					}
				}
				for (int r=0;r<k;r++){
					if (i+r>=n || s2[i+r][j]!='B'){
						validb=0;
						break;
					}
				}
				if (validr) red=1;
				if (validb) blue=1;
				//d1
				validr=1;validb=1;
				for (int r=0;r<k;r++){
					if (i+r>=n || j+r>=n || s2[i+r][j+r]!='R'){
						validr=0;
						break;
					}
				}
				for (int r=0;r<k;r++){
					if (i+r>=n || j+r>=n || s2[i+r][j+r]!='B'){
						validb=0;
						break;
					}
				}
				if (validr) red=1;
				if (validb) blue=1;
				//d2
				validr=1;validb=1;
				for (int r=0;r<k;r++){
					if (i-r<0 || j-r<0 || s2[i-r][j-r]!='R'){
						validr=0;
						break;
					}
				}
				for (int r=0;r<k;r++){
					if (i-r<0 || j-r<0 || s2[i-r][j-r]!='B'){
						validb=0;
						break;
					}
				}
			}
		}
		printf("Case #%d: ",xx++);
		if (!red && !blue) printf("Neither\n");
		else if (red && blue) printf("Both\n");
		else if (red) printf("Red\n");
		else printf("Blue\n");
	}
	return 0;
}
