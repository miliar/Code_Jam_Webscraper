#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

char str[50];
int len;
__int64 count;
int flag[50];
__int64 num[50];
int p;
int flag1[50];


void cal1(int i){
	
	if(i>=p){
		__int64 total=0;
		for(int j=0;j<p;j++){
			if(flag1[j]==0)	total+=(num[j]*(-1));
			else total+=num[j];
		}
		if(abs(total)==0 || abs(total)%2==0 || abs(total)%3==0 || abs(total)%5==0 || abs(total)%7==0){
			/*for(int j=0;j<p;j++){
				printf("%d ",num[j]*(flag1[j]==0 ? -1 : 1));
			}
			printf("\n");*/
			count++;
		}
		return;
	}
	for(int j=0;j<=1;j++){
		if(i==0 && j==0)	continue;
		flag1[i]=j;
		cal1(i+1);
	}
}

void cal(){
	p=0;
	__int64 tmp=str[0]-'0';
	for(int i=0;i<len-1;i++){
		if(flag[i]==1){
			num[p]=tmp;
			p++;
			tmp=str[i+1]-'0';
		}
		else{
			tmp=tmp*10+(str[i+1]-'0');
		}
	}
	num[p]=tmp;
	p++;
	cal1(0);

}

void solve(int i){
	
	if(i>=len-1){
		cal();
		return;
	}
	for(int j=0;j<=1;j++){
		flag[i]=j;
		solve(i+1);
	}
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int caseID =1; caseID<=n;caseID++){
		scanf("%s",&str);
		len = strlen(str);
		count=0;
		solve(0);

		printf("Case #%d: %I64d\n",caseID,count);
	}
	

}
