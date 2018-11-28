#include<cstdio>
#include<cstring>
int a[101][101],m,n,t,k,x1,x2,y1,y2,l1,l2,l3,l4,w=1;
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
    scanf("%d",&m);
    memset(a,0,sizeof(a));
    l1=100;l2=0;l3=100;l4=0;
    for(int i=0;i<m;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x1<l1)
			  l1=x1;
	  		  if(x2>l2)
	  		   l2=x2;
	  		   if(y1<l3)
	  		    l3=y1;
	  		    if(y2>l4)
	  		    l4=y2;
			for(int j1=x1;j1<=x2;j1++)
			for(int j2=y1;j2<=y2;j2++)
			 a[j1][j2]=1;
			}
			n=0;
			int mark=1;
			while(mark){
						mark=0;
			  for(int j1=l2;j1>=l1;j1--){
			  for(int j2=l4;j2>=l3;j2--){
			    if(a[j1][j2]==1){	
				 if((j1==l1||(j1!=l1&&a[j1-1][j2]==0))&&(j2==l3||(j2!=l3&&a[j1][j2-1]==0)))
				  a[j1][j2]=0;
				  else mark=1;
				  }else if((j1!=l1&&a[j1-1][j2]==1)&&(j2!=l3&&a[j1][j2-1]==1)){
				  		mark=1;
				  		a[j1][j2]=1;
						}
						//	printf("%d ",a[j1][j2]);
							}//	printf("\n");
						
						}	n++;
					
			}
			printf("Case #%d: %d\n",w++,n);
 }
 return 0;
}
 
