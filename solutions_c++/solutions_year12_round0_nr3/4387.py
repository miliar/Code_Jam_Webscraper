#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int main()
{
	int rise =0,i,j,k,l,m,n,r,s,arr[10],arr2[10],a,b,count=0;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		rise=0;
		cin>>a;
		cin>>b;
	/*	for(j=a;j<=b;j++)
		{
			r=j;
			s=0;
			int ind=0;
			memset(arr,0,4*10);
			while(r!=0)
			{
				s=r%10;
				arr[ind]=s;
				ind++;
				r=r/10;
			}
			for(k=j+1;k<=b;k++)
			{
				r=k;
				int check=0;
				memset(arr2,0,4*10);
				while(r!=0)
				{
					s=r%10;
					arr2[check]=s;
					check++;
					r=r/10;
				}
				if(ind==check)
				{
					for(l=0;l<check;l++)
					{	
						if(arr[l]==arr2[0])
							break;
					}
					count=0;
					for(m=0;m<check;m++)
					{
						if(arr[(l+m)%check]==arr2[m])
							count++;
					}
					if(count==check)
						rise++;
				}


			}
		}*/
		for(j=a;j<=b;j++)
		{
			r=j;
			int ind=0;
			memset(arr,0,4*10);
			while(r!=0)
			{
				s=r%10;
				arr[ind]=s;
				ind++;
				r=r/10;
			}
			for(k=j+1;k<=b;k++)
			{
				r=k;
				int check=0;
				memset(arr2,0,4*10);
				while(r!=0)
				{
					s=r%10;
					arr2[check]=s;
					check++;
					r=r/10;
				}
				if(ind==check)
				{
					if(ind==2 )
					{
						if(arr[0]==arr2[1] &&arr[1]==arr2[0])
							rise++;
					}
					else if(ind==3)
					{
						if(arr[0]==arr2[1] && arr[1]==arr2[2] && arr[2]==arr2[0])
							rise++;
						else if(arr2[0]==arr[1] && arr2[1]==arr[2] && arr2[2]==arr[0])
							rise++;
						else if(arr[0]==arr2[2]&& arr[1]==arr2[0] && arr[2]==arr2[1])
							rise++;
						else if(arr2[0]==arr[2]&& arr2[1]==arr[0] && arr2[2]==arr[1])
							rise++;
					}
				}
			}
		}

		cout<<"Case #"<<i<<": "<<rise<<endl;
	}
		return 0;
}
					
		
