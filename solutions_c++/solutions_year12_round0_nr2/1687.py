#include<stdio.h>
int main(){
	int t,n,s,p,i,temp;
	scanf("%d",&t);
	int j=0;
	while(j++<t){
		scanf("%d %d %d",&n,&s,&p);
		int count=0,pos=0,left=0;
		int a[100][7]={0,0,0,0,0,0,0};//0-sum 1,2,3-triplet 4-suprising flag 5-best result flag 6-possibility
		for(i=0;i<n;i++){
			scanf("%d",&a[i][0]);
			if(a[i][0]%3==0){
				a[i][1]=a[i][2]=a[i][3]=a[i][0]/3;}
			else if(a[i][0]%3==1){
				a[i][1]=a[i][2]=a[i][3]=a[i][0]/3;
				a[i][3]+=1;}
			else if(a[i][0]%3==2){
				a[i][1]=a[i][2]=a[i][3]=a[i][0]/3;
				a[i][3]+=1;
				a[i][2]+=1;}
			if(a[i][1]>=p||a[i][2]>=p||a[i][3]>=p) {
				a[i][5]=1;
				count++;}
			if(a[i][0]!=0){
				if(a[i][0]%3==0&&a[i][0]/3+1>=p) {a[i][6]=1; pos++;}
				else if(a[i][0]%3==1&&a[i][0]/3+1>=p) {a[i][6]=1;pos++;}
				else if(a[i][0]%3==2&&a[i][0]/3+2>=p) {a[i][6]=1;pos++;}
			}
			if(a[i][5]==0&&a[i][6]==1) left++;
		}
		if(s!=0){
			if(left>s)
				count+=s;
			else
				count+=left;
		}
			printf("Case #%d: %d\n",j,count);
	}
return 0;
}
