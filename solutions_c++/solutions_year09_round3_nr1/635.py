#include <iostream>
#include <cstring>
using namespace std;
#define M 100
char str[M+5];
char mid[M+5];
int hash[300];
int num;
int ckj[300];
int temp[300];

int solve(int c){
	num=0;
	int i,j;
	scanf("%s",str);
	memset(hash,-1,sizeof(hash));

	int len=strlen(str);
	for(i=0;i<len;i++){
		if(hash[str[i]]==-1){
			hash[str[i]]=i;
			mid[num++]=str[i];
		}
	}

	temp[0]=1;
	temp[1]=0;
	for(i=2;i<num;i++)
		temp[i]=i;

	memset(ckj,0,sizeof(ckj));
	int check[M+10];
	memset(check,0,sizeof(check));
	for(i=0;i<num;i++){

		int mmin=100,u;
		for(j=0;j<num;j++){
			if(hash[mid[j]]<mmin&&!check[j]){
				mmin=hash[mid[j]];
				u=j;
			}
		}
		check[u]=1;
		for(j=0;j<len;j++)
			if(mid[u]==str[j])
				ckj[j]=temp[i];
	}

	__int64 sum=0;
	if(num==1) num=2;
	for(i=0;i<len;i++){
		sum=sum*num;
		sum+=ckj[i];
	}

	printf("Case #%d: %I64d\n",c,sum);
	return 0;
}

int main(){

	freopen("A-large.in","rb",stdin);
	freopen("A-large.out","wb",stdout);
	int ca;
	int i;

	scanf("%d",&ca);
	getchar();
	for(i=1;i<=ca;i++){
		solve(i);
	}
	return 0;
}