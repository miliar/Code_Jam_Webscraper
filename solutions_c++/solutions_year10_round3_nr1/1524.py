#include <iostream.h>
#include <conio.h>
#include <stdlib.h>
int main()
{
	int a[10000],b[10000];
	int t,i,j,k,n;
	cin>>t;
	for (i=1;i<=t;i++)
		{
			cin>>n;
				
					for (k=1;k<=n;k++)
						{cin>>a[k]>>b[k];}
					if (n==1) cout<<"Case #"<<i<<": 0\n";
					else if (n==2)
						{
							if (((a[1]<a[2])&(b[1]<b[2]))||((a[1]>a[2])&(b[1]>b[2])))
								cout<<"Case #"<<i<<": 0\n";
							else cout<<"Case #"<<i<<": 1\n";
						}
				
			a[1]=0;a[2]=0;b[1]=0;b[2]=0;
		}
	return 0;
	
}