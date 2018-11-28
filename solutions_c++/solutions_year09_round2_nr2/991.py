#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define M 50

char sou[M+5];
char res[M+5];
int mid[M+5];

int cmp(const void *a,const void *b){
	return (*(int *)b)-(*(int *)a);
}

int solve(){
	int i,j;

	gets(sou);
	int len=strlen(sou);

	for(i=0;i<len;i++){
		mid[i]=sou[len-i-1]-'0';
	}

	mid[len++]=0;

	for(i=0;i<len;i++){
		int u,mmin=20;
		for(j=0;j<i;j++){
			if(mid[j]>mid[i]&&mid[j]<mmin){
				mmin=mid[j];
				u=j;
			}
		}

		if(mmin==20) continue;
		int t=mid[i];
		mid[i]=mid[u];
		mid[u]=t;
		break;
	}

	qsort(mid,i,sizeof(mid[0]),cmp);

	if(mid[len-1]==0)
		len--;

	for(i=0;i<len;i++)
		res[i]='0'+mid[len-i-1];
	res[len]=0;

	return 0;
}

int main(){

	freopen("D:/Users/Passion/Desktop/B-large.in","rb",stdin);
	freopen("D:/Users/Passion/Desktop/B-large.out","wb",stdout);
	int ca;
	int c;
	scanf("%d",&ca);
	getchar();
	for(c=1;c<=ca;c++){
		solve();
		printf("Case #%d: %s\n",c,res); 
	}
	return 0;
}