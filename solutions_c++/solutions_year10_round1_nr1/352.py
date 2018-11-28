#include<cstdio>
#include<cstring>
char a[52][52],b[52][52],d[8][2]={{-1,0},{1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
int t,n,m=0,k;
int check(int x,int y,char c){
	return x>=0&&y>=0&&x<n&&y<n&&b[x][y]==c;
}
int check(int x,int y){
	int p=k-1;
	for(int i=0;i<8;i++)
	  if(check(x+p*d[i][0],y+p*d[i][1],b[x][y])){
		 int mark=1;
 	    for(int j=0;j<p;j++)
 	     if(b[x+j*d[i][0]][y+j*d[i][1]]!=b[x][y]){
 	       mark=0;
 	       break;
		   }
         	  if(mark)
   	    return 1;
   }
   return 0;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
	   scanf("%d%d",&n,&k);
	   getchar();
	   for(int i=0;i<n;i++){
	     scanf("%s",&a[i]);
  	   	 getchar();
	   }
	   for(int i=0;i<n;i++)
	     for(int j=0;j<n;j++)
	       b[i][j]=a[n-1-j][i];
      for(int i=0;i<n;i++){
  	    int pp=n-1,pp1=n-1;
        while(pp>=0){
		  while(pp1>=0&&b[pp1][i]!='.')
		    pp1--;
          pp=pp1;
          while(pp>=0&&b[pp][i]=='.')
            pp--;
          while(pp>=0&&b[pp][i]!='.'){
		    b[pp1--][i]=b[pp][i];
		    b[pp--][i]='.';
		  }
		}
     }
     int k1=0,k2=0;
     for(int i=0;i<n;i++)
       for(int j=0;j<n;j++)
         if(b[i][j]!='.'&&check(i,j)){
  		   if(b[i][j]=='R')
  		     k1=1;
    		 else k2=1;
		   }
    printf("Case #%d: ",++m);
    if(!k1&&!k2)
      printf("Neither\n");
    if(k1&&k2)
      printf("Both\n");
    if(k1&&!k2)
      printf("Red\n");
    if(!k1&&k2)
      printf("Blue\n");
    }
    return 0;
}
