#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
	//freopen("recycled.in","r",stdin);
	//freopen("recycled.out","w",stdout);
	int num,f[100];
	cin>>num;
	for (int tt=1;tt<=num;++tt)
		{
			int a,b,ans=0;
			cin>>a>>b;
			int p=0;
			for (int i=a;i<=b;++i)
				{
					memset(f,0,sizeof(f));
					int p=0,t=i,plus=0;
					while (t>0)
						{
							f[p++]=t%10;
							t/=10;
						}
					plus=0;
					for (int s=1;s<p;++s)
						{
							int po=1,x=0;
							for (int j=0;j<p;++j)
								{
								 x+=po*f[(j+s)%p];
								 po*=10;
								}
							if (x!=i&&a<=x&&x<=b&&i<x) ++plus;
						}
					if (plus>0)
								{
									int k=2;
									while (k+1<p)
										{
										 bool flag=0;
										 if (p%k==0)
										 	for (int x=1;x<p/k;++x)
										 		{
													if (flag) break;
													for (int y=0;y<k;++y)
														if (f[y]!=f[x*k+y]) {flag=1;break;}
												}
										 if (!flag) {plus/=k;break;}
										 ++k;
										}
								}
					ans+=plus;
				}
			cout<<"Case #"<<tt<<": "<<ans<<endl;
		}
}
