#include<cstdio>
int a[200],x[200][300];
inline int dif(int p,int q){
  if(p>q){return p-q;}
  else{return q-p;}
}
inline int lez(int p,int q){
  if(p<q){return p;}
  else{return q;}
}
int main(){
  int t,tt,n,i,j,k,dcost,icost,m,y,z,ans;
  scanf("%d",&t);
  for(tt=1;tt<=t;tt++){
    scanf("%d",&dcost);
    scanf("%d",&icost);
    scanf("%d",&m);
    scanf("%d",&n);
    for(i=0;i<n;i++){
      scanf("%d",&a[i]);
    }
    //i=0
    for(j=0;j<256;j++){
      x[0][j]=dif(a[0],j);
    }
    //i>0
    for(i=1;i<n;i++){
      for(j=0;j<256;j++){
	x[i][j] = i*dcost+dif(a[i],j);
	//if(x[i][j]<0){printf("EEE%d-%d ",i,j);}
	x[i][j] = lez(x[i][j],x[i-1][j]+dcost);
	//if(x[i][j]<0){printf("GGG%d-%d ",i,j);}
	if(m==0){
	  x[i][j] = lez(x[i][j],x[i-1][j]+dif(a[i],j));
	}else{
	  for(k=0;k<256;k++){
	    y = dif(j,k);
	    if(y==0){
	      z=0;
	    }else{
	      z=((y-1)/m)*icost;
	    }
	    x[i][j] = lez(x[i][j],x[i-1][k]+dif(a[i],j)+z);
	    //if(x[i][j]<0){printf("VVV%d-%d-%d ",i,j,k);}
	  }
	}
      }
    }
    /*for(j=0;j<256;j++){
      printf("%3d ",j);
    }printf("\n");
    for(i=0;i<n;i++){
      for(j=0;j<256;j++){
	printf("%3d ",x[i][j]);
      }printf("\n");
    }*/
    ans = dcost*n;
    for(j=0;j<256;j++){
      ans = lez(ans,x[n-1][j]);
    }
    printf("Case #%d: %d\n",tt,ans);
    //fflush(stdout);
  }
  return 0;
}