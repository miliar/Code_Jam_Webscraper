//poj 

#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
#include<set>
#include<queue>

using namespace std;
typedef long long llt;

#define maxv 5010

#define LEN 17
#define myAbs(x) ((x)>=0?(x):-(x))
#define Max(x,y) ((x)>(y)?(x):(y))
#define Min(x,y) ((x)<(y)?(x):(y))
#define inf 1999999999
#define MOD 200039
#define eps 1e-8
#define EPS 1e-8
#define M_PI 3.14159265358979323846



int l,d,n;
char dic[maxv][LEN];
char str[1000000];
char str2[maxv][100];
int len[maxv];

int slen;


void solve(){
	int i,j,k;
	int t;
	int cnt;
	int flag;
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;++i){
		scanf("%s",dic[i]);
	}
	for(t=0;t<n;++t){
		scanf("%s",str);
		slen=strlen(str);
		j=0;
		for(i=0;i<slen;++i){
			if(str[i]=='('){
				len[j]=0;
				while(str[i]!=')'){
					str2[j][len[j]++]=str[i];
					++i;
				}
			}else{
				len[j]=1;
				str2[j][0]=str[i];
			}
			++j;
		}/*
		printf("j= %d\n",j);
		for(i=0;i<j;++i){
			printf("%d ",len[i]);
		}
		printf("\n");*/
		cnt=0;
		for(i=0;i<d;++i){
			for(j=0;j<l;++j){
				flag=0;
				for(k=0;k<len[j];++k){
					if(str2[j][k]==dic[i][j]){
						flag=1;
						break;
					}
				}
				if(flag==0){
					break;
				}
			}
			if(flag){
				++cnt;
			}
		}
		printf("Case #%d: %d\n",t+1,cnt);
	}
}
int main(){
	//freopen("out.txt","w",stdout);
	solve();
	//system("PAUSE");
	return 0;
}

