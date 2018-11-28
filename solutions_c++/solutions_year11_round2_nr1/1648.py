#include<stdio.h>
#include<string.h>
void print(char *qqq){
	int  l=strlen(qqq),i;
	i=l-1;
	while(qqq[i]=='0')i--;
	qqq[i+1] = 0;
	puts(qqq);
}
int main(){
	int i,j,n;
	int T,tt=0;
	char a[108][108];
	double wp0[108],wp1[108],wp2[108],RPI[108];
	int wt[108];
	int ContestTime[108];
	char temp[100];
	freopen("A-large.in","r",stdin);
	freopen("a1.out","w",stdout); 
	scanf("%d",&T);
	while(tt++<T){
	printf("Case #%d:\n",tt);
	scanf("%d",&n);
	for(i=0;i<n;i++)scanf("%s",a[i]); 
	for(i=0;i<n;i++){
	wt[i]=0;
	ContestTime[i] = 0;
	for(j=0;j<n;j++)
	if(a[i][j]!='.'){
	if(a[i][j]=='1')wt[i]++;
	ContestTime[i]++;
	}
	wp0[i] = wt[i]*1.0/ContestTime[i];
	}
	for(i=0;i<n;i++){
	double sum = 0;
	for(j=0;j<n;j++)if(a[i][j]!='.'){
	sum+=(wt[j]-(a[i][j]=='0'))*1.0/(ContestTime[j]-1);
	}
	wp1[i]=sum/ContestTime[i];
	}
	
	for(i=0;i<n;i++){
	double sum = 0;
	for(j=0;j<n;j++)if(a[i][j]!='.'){
	sum += wp1[j];
	}
	wp2[i] = sum/ContestTime[i];
	}
	for(i=0;i<n;i++){
	RPI[i] = 0.25*wp0[i]+0.50*wp1[i]+0.25*wp2[i];
	sprintf(temp,"%.12lf",RPI[i]);
	print(temp);
	}
  } 
return 0;
}
