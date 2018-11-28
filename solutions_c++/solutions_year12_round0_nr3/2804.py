#include<iostream>

using namespace std;

int main()
{
	unsigned long long int n,k,j=0,a,b,cnt=0,rem,num,out,i,mult;
	cin>>n;
	while(j++<n)
	{
		cin>>a>>b;
		out=0;
		for(i=a;i<b;i++)
		{
	//		cout<<"\n i = "<<i;
			if(i<10)
				continue;
			k=i;
			do
			{
				rem=k%10;
				if(rem==0)
				{
					num=k;
					mult=1;
					cnt=1;
					do
					{
						num/=10;
						cnt*=10;
						rem=num%10;
	//					cout<<"\n\tnum = "<<num<<" cnt = "<<cnt<<" rem = "<<rem;	
	//					system("Pause");
					}while(rem==0);
					num/=10;
					while(mult<=num)mult*=10;
					num+=(rem*cnt*mult);
				}	
				else
				{
					num=k/10;
					mult=10;
					while(mult<=num)
					mult*=10;
					num+=(rem*mult);
	//				cout<<"\n second loop num = "<<num;
				}
				if(num<=b && num>i)
				{
//					cout<<i<<"\t"<<num<<"\n";
					out++;
				}
				k=num;
	//		cout<<"num = "<<num<<" i = "<<i;
			}while(num!=i);
		}
		cout<<"Case #"<<j<<": "<<out<<"\n";
	}
//	system("Pause");
	return 0;
}