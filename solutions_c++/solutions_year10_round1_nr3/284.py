#include<cstdio>
int t,a1,a2,b1,b2,k=0;
int gcd(int x,int y){
	if(x<y){
			x=x+y;
			y=x-y;
			x=x-y;
			}
	if(x%y==0)
	  if(x!=y)
  	    return 1;
 		else return 0;
	int x1=x/y;
	int temp=gcd(x%y,y);
	if(temp==0)
	  return 1;
    if(x1>1)
      return 1;
    return 0;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
      int sum=0;
      scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
      for(int i=a1;i<=a2;i++)
        for(int j=b1;j<=b2;j++)
          if(gcd(i,j))
            sum++;
      printf("Case #%d: %d\n",++k,sum);
	 }
	 return 0;
 }
