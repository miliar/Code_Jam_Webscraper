#include <iostream>
#include <cstring>
using namespace std;
int a1,a2,b1,b2,ans;

bool win(int x,int y)
{
 if (x>y) return win(y,x);	
 if (x==y) return false;
 if (x*2<=y) return true;	 	
 return !win(y-x,x); 
}

int main()
{
 int i,j,k,t;
 freopen("03.txt","w",stdout);
  scanf("%d",&t);
 for (k=1;k<=t;k++)
  {
   scanf("%d%d%d%d",&a1,&a2,&b1,&b2);		
   ans=0;
   for (i=a1;i<=a2;i++)
    for (j=b1;j<=b2;j++)
	 if (win(i,j))
	 ans++;
   printf("Case #%d: %d\n",k,ans);	 		
  }	
 return 0;	
}
