#include<stdio.h>
#include<conio.h>
#include<algorithm>

using namespace std;

int main(){
	//freopen("ini.txt","r",stdin);
	int tc;
	scanf("%d",&tc);
for(int z=1;z<=tc;z++){
    int total,status,temp;
	int trainA[4][101],trainB[4][101],sA[101],sB[101];
	int aw,awt,ak,akt,ta,tb,a,b,time;
	ta = tb = 0;
	scanf("%d",&time);
	scanf("%d %d",&a,&b);
	memset(trainA,-2,sizeof(trainA));
	memset(trainB,-2,sizeof(trainB));
	for(int i=0;i<a;i++){
		scanf("%d:%d %d:%d",&aw,&awt,&ak,&akt);
		trainA[0][i] = (aw*60)+awt;
		trainA[1][i] = (ak*60)+akt;
		trainA[2][i] = -2;				
	}
	for(int i=0;i<b;i++){
		scanf("%d:%d %d:%d",&aw,&awt,&ak,&akt);
		trainB[0][i] = (aw*60)+awt;
		trainB[1][i] = (ak*60)+akt;
		trainB[2][i] = -2;				
	}
	sort(trainA[0],trainA[0]+a);
	//sort(trainA[1],trainA[1]+a);
	sort(trainB[0],trainB[0]+b);
	//sort(trainB[1],trainB[1]+b);
	for(int i=0;i<a;i++){
	   status = 1;
	   for(int x=0;x<b;x++){
	   		   //printf("%d %d , %d %d = %d--yes\n",i,x,trainB[i][0],trainA[x][1]+time,sA[x]);
	   		if(trainA[0][i]>=(trainB[1][x]+time)){
			  
			  if(trainB[2][x]==-2)
			  {//printf("%d %d ,yes\n",i,x);
			    status = 0;
			    trainB[2][x]=-1;
				x=b;
			  }		
			  //status=0;			  
		    }
       }
	   if(status==1){
		  ta++;}   		
	}
	for(int i=0;i<b;i++){
	   status = 1;
	   for(int x=0;x<a;x++){
	   		if(trainB[0][i]>=trainA[1][x]+time){
			 //printf("%d %d , %d %d = %d--yes\n",i,x,trainB[i][0],trainA[x][1]+time,sA[x]);
			  if(trainA[2][x]==-2){
			  				//printf("%d %d ,yes\n",i,x);
			    status = 0;
			    trainA[2][x]=-1;
				x=a;
				temp = x;			
			  }					  
		    //status=0;
			}
	      
       }
	   if(status==1){
	   				 tb++;
						}  		
	}
	printf("Case #%d: %d %d\n",z,ta,tb);		  
}
//getch();
return 0;	
}
