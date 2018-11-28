#include <stdio.h>
#include <string.h>
int map[110][110];
int h,w;
int nextstep(int i,int j,int &y,int &x){
    y=i;x=j;
    int found=0;
    if (i>1&&(map[i-1][j]<map[y][x])){ y=i-1; x=j; found=1;}
    if (j>1&&(map[i][j-1]<map[y][x])){ y=i; x=j-1; found=1;}
    if (j<w&&(map[i][j+1]<map[y][x])){ y=i; x=j+1; found=1;}
    if (i<h&&(map[i+1][j]<map[y][x])){ y=i+1; x=j; found=1;}
    return found;
}
int main(){
    freopen("bb.in","r",stdin);
    freopen("out1.txt","w",stdout); 
    int i,j,T,t,color,y,x,found;
    int data[110][110];
	scanf("%d",&T);
	for (t=1;t<=T;t++){
        memset(map,0,sizeof(map));
		scanf("%d%d",&h,&w);
		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
				scanf("%d",&map[i][j]);
		memset(data,0,sizeof(data));
		color=0;
		while (1){
			  found=0;
			  for (i=1;i<=h && !found;i++)
			  	  for (j=1;j<=w && !found;j++)
			  	  	  if (data[i][j]==0){found=1; y=i;x=j;}
			  if (found==0) break;
			  i=y; j=x;
			  
			  data[i][j]=++color; 
			  while (1){
			  		if (nextstep(i,j,y,x)){
				   	   if (data[y][x]==0){
  	  				   	  data[y][x]=color;
  	  				   	  i=y; j=x;
	                     }else{
                               data[i][j]=data[y][x];
 			                   while (1){
						  		     if (data[i+1][j]==color){ data[i+1][j]=data[y][x]; i++;}else 
						  		     if (data[i-1][j]==color){ data[i-1][j]=data[y][x]; i--;}else
						  		     if (data[i][j+1]==color){ data[i][j+1]=data[y][x]; j++;}else 
						  		     if (data[i][j-1]==color){ data[i][j-1]=data[y][x]; j--;}else
						  		     break;
                                  }
                               color--;
                               break;
						  }
                   }else break;
  			  }
       }
       printf("Case #%d:\n",t);
       for (i=1;i<=h;i++){
           for (j=1;j<=w;j++)
               printf("%c%c",'a'-1+data[i][j],j<w?' ':'\n');
       }
     }
     return 0;
}
