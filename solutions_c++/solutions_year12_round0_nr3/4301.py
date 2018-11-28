#include<iostream>
#include<conio.h>
#include<string>
using namespace std;
void main()
{
	freopen("C-small.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
	int t;
	cin>>t;
	int a,b;
	int count;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		cin>>a;
		cin>>b;
		count=0;
		if(a>=0 && a<=9)
			cout<<count<<"\n";
		else
		{
			for(int j=a;j<=b;j++)
			{
				int x=1;
				int m=1;
			   int temp=j;
			   int temp2=0;
			   do
			   {
				   temp=temp/10;
				   m=m*10;
			   }while((temp/10)!=0);
			   int l=m;
			    do
				{
					x=x*10;
					temp2=((j%x)*l)+(j/x);
					//cout<<j<<"  ";
					//cout<<((j%x)*l)<<"+"<<(j/x)<<" ";
					//cout<<temp2<<"\n";
					if ((temp2!=j)&&(temp2<=b)&&(temp2>j))
					{
						//cout<<temp2<<"\n";
                     count++;
					}
					l=l/10;
				}while(x!=m);
			}
			cout<<count<<"\n";
			
		}
	}



}