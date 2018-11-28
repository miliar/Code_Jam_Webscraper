#include<stdio.h>
#include<string.h>
struct node{
	char yy;
}s[105];
int main(){
	int cas,i,j,n,t,f,k,t1,t2;
	int to,tb,flage,time,b;
	char a,m;
	int k1,k2,k3;
	int O[105];
	int B[105];
	int arr1[105],arr2[105];
	freopen("C:\\Documents and Settings\\海鹏\\桌面\\A-small-attempt1.in","r",stdin);
	freopen("C:\\Documents and Settings\\海鹏\\桌面\\stdout.txt","w",stdout);
	scanf("%d",&cas);
	f=1;
	while(cas--){
		k1=k2=k3=0;
		memset(arr1,0,sizeof(arr1));
		memset(arr2,0,sizeof(arr2));
		scanf("%d",&n);
		flage=0;
		time=0;
		for(i=1;i<=n;i++){
				scanf(" %c %d",&a,&b);
				if(a=='O'){
					s[++k3].yy='O';
					O[++k1]=b;
				}
				else{
					s[++k3].yy='B';
					B[++k2]=b;
				}
		}
		i=1,j=1,k=1;
		t1=1,t2=1;
		int step=0;
		flage=1;
		while(n){
			flage=1;
			if(i<O[t1]){
				i++;
			}
			else if(i==O[t1]&&s[k].yy=='O'){
				n--;
				t1++;
				k++;
				flage=0;
			}
			else if(i>O[t1]){
				if(i>1)i--;
			}
			
			
			if(j<B[t2]){
				j++;
			}
			else if(j==B[t2]&&s[k].yy=='B'&&flage){
				n--;
				t2++;
				k++;
			}
			else if(j>B[t2]){
				if(j>1)j--;
			}
			time++;
			step++;
		}
		printf("Case #%d: %d\n",f++,time);
	}
	return 0;
}
			
	
			
	
			

				
			
