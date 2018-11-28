#include <iostream>
#include <cstdio>
          
using namespace std;
        
int main()
{
	int T,j=0;
	int a[1001];
	a[0]=0;
	for (int i=1;i<=1000;i++)a[i]=i;
	scanf("%d",&T);
	while(j++ < T)
	{
		int A,B;
		int s=0;
		scanf("%d %d",&A,&B);
		while(B>A)
		{
			if(B==1000 && A==1)s++;
			else if(B>99){
				int t1=(B%10)*100+(B/10);
				int t2=(B%100)*10+(B/100);
				if(t1<B && t1>=A)s++;
				if(t2<B && t2>=A)s++;
			}	
			else if(B>9){
				int t1=(B%10)*10+(B/10);
				if(t1<B && t1>=A)s++;
			}
			B--;
		}
		printf("Case #%d: %d\n",j,s);
	}	
}
