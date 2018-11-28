#include<iostream>
using namespace std;

inline int gcd(int a,int b){
	return b?gcd(b,a%b):a;
}

int main()
{

    int T,n,a,b,cases,t;
    scanf("%d",&T);
    cases=0;
    while(T--)
	{
		scanf("%lld %d %d",&n,&a,&b);
		t = 100/gcd(a,100);
		if(t<=n){
			if((a!=0 && b==0) || (a!=100 && b==100))	
			printf("Case #%d: Broken\n",++cases);
			else 
				printf("Case #%d: Possible\n",++cases);
		}
		else {
				printf("Case #%d: Broken\n",++cases);
		}
	}
	
	
    return 0;
}



