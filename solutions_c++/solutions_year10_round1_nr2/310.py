#include<cstdio>
#include<cstring>
int abs(int x){
	if(x<0)
	  return -x;
   return x;
}
int t,d,i0,m,n,a[101],b[256],c[256],k=0;
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
      scanf("%d%d%d%d",&d,&i0,&m,&n);
      for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
      memset(b,0,sizeof(b));
      for(int i=0;i<n;i++){
  		  for(int j=0;j<256;j++)
  		    c[j]=b[j]+d;
  		    if(m>0)
 		  for(int j1=0;j1<256;j1++)
		    for(int j2=0;j2<256;j2++){
	 		int temp1=0,temp2=0;
					if(a[i]!=j1)
					 temp1=i0*((abs(a[i]-j1)-1)/m);
			  		  if(a[i]!=j2)
					  temp2=i0*((abs(a[i]-j2)-1)/m+1);
 		    if(b[j1]+temp1+temp2<c[j2])
 		      c[j2]=temp1+temp2+b[j1];
		   }
	  		   for(int j=0;j<256;j++)	{
  		  int k1=j-m;
  		  if(k1<0)
  		    k1=0;
	      int k2=j+m;
	      if(k2>255)
	        k2=255;
          for(int j1=k1;j1<=k2;j1++)
            if(b[j]+abs(j1-a[i])<c[j1])
              c[j1]=b[j]+abs(j1-a[i]);
		  }
		  memcpy(b,c,sizeof(c));
		  }	
	  int mm=0x7fffffff;
	  for(int i=0;i<256;i++)
	    if(mm>b[i])
	      mm=b[i];
     printf("Case #%d: %d\n",++k,mm);
	}
	return 0;
}
