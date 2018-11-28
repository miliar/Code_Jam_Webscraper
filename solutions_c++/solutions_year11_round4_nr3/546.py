#include <iostream>
#include <algorithm>
#include<cmath>
using namespace std;
bool fun(int k)
{
	int i;
	for(i=2;i*i<=k; ++i){
		if(k%i == 0) return false;
	}
	return true;
}
int main()
{
	int ca,n,x,i,mi,ma,tmp;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("cc.out","w",stdout);
	cin>>ca;
	for(x=1;x<=ca;++x)
	{
		cin>>n;
		mi=0,ma=1;
		for(i=2;i<=n;++i)
		{
			if(fun(i)==true){
				mi+=1;
				tmp=i;
				while(tmp<=n){
					ma+=1;
					tmp*=i;
				}
			}
		}
		if(n==1) mi=1;
		int ans=ma-mi;
		printf("Case #%d: %d\n",x,ans);
	}
	return 0;
}
