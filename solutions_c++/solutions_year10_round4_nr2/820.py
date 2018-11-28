#include<cstdio>
#include<cstring>
int a[5000],n,m,k,t,p,b[2000],d[]={1,2,4,8,16,32,64,128,256,512,1024},w=1;
int check(){
  for(int i=0;i<d[p];i++)
    if(b[i]>0)
      return 1;
  return 0;
}
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
 	  memset(a,0,sizeof(a));
 	  scanf("%d",&p);
 	  for(int i=0;i<d[p];i++){
		  scanf("%d",&b[i]);
		  b[i]=p-b[i];
		  }
      for(int i=0;i<d[p]-1;i++)
        scanf("%d",&k);
      n=0;
      m=0;
    //  printf("1");
      int mark=1;
      while(check()){
	   if(m==0){
	     for(int i=0;i<d[p];i++)
	       b[i]--;
	       n++;
		 }else
        for(int i=0;i<d[m];i++){
	      mark=0;
	      for(int j=d[p-m]*i;j<d[p-m]*(i+1);j++)
	        if(b[j]>0)
	          mark=1;
		if(mark){
		   for(int j=d[p-m]*i;j<d[p-m]*(i+1);j++)
		    b[j]--;
		    n++;
			}
		 
		}
		m++;
	  }//while
	  printf("Case #%d: %d\n",w++,n);
	 }
	 return 0;
 }
