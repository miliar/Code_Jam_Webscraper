#include <iostream>
int n,i,ans;

int solve(void)
{
	int f[20],f0[20];
	char g[]="welcome to code jam";
	char x;
	for(int i=0;i<=19;i++)
		f[i]=0;
	f[0]=1;
	for (;(x=getchar())!='\n';)
	{
		for(int i=0;i<=19;i++)
			f0[i]=f[i];
		for(int i=0;i<19;i++)
			f0[i+1]=(f0[i+1]+(x==g[i]?1:0)*f[i])%10000;
		for(int i=0;i<=19;i++)
			f[i]=f0[i];
	}return f[19];
}

int main(void)
{
	scanf("%d",&n);
	for(;getchar()!='\n';);
	for(i=0;i<n;i++){
		ans=solve();
		std::cout<<"Case #" <<i+1<<": ";
		if (ans<10)
			std::cout<<"000";
		else if (ans<100)
			std::cout<<"00";
		else if (ans<1000)
			std::cout<<"0";
		std::cout<<ans<<std::endl;
	}
}
