#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int arr[513][513];
bool tsst(int a,int b,int c, int d)
{
	int i,j;
	if(a==c && b==d)
	{
		if(arr[a][b]!=2)
		return true;
		return false;
	}
	for(i=a;i<=c;i++)
	{
		for(j=b;j<=d;j++)
		{
			if(arr[i][j]==2)
			return false;
			if(i!=c)
			{
				if(arr[i+1][j]==arr[i][j])
				return false;
			}
			if(j!=d)
			{
				if(arr[i][j+1]==arr[i][j])
				return false;
			}
		}
	}
	return true;
}
void cut(int a,int b,int c, int d)
{
	int i,j;
	for(i=a;i<=c;i++)
	{
		for(j=b;j<=d;j++)
		arr[i][j]=2;
	}
}			
main()
{
	int test,i,j,k,n,m;
	string str;
	cin>>test;
	for(i=1;i<=test;i++)
	{
		cin>>m>>n;
		for(j=0;j<m;j++)
		{
			cin>>str;
			int num,cnt=0;
			for(k=0;k<str.size();k++)
			{
				if(str[k]>='0' && str[k]<='9')
				num=str[k]-'0';
				else
				num=10 + str[k]-'A';
				arr[j][cnt+3]=num%2;
				num/=2;
				arr[j][cnt+2]=num%2;
				num/=2;
				arr[j][cnt+1]=num%2;
				num/=2;
				arr[j][cnt]=num%2;
				num/=2;
				cnt+=4;
			}
		}
	//	for(j=0;j<m;j++)
	//	{
	//		for(k=0;k<n;k++)
	//		cout<<arr[j][k];
	//		cout<<endl;
	//	}
		int p,q;
		int size[513],count=0;
		memset(&size,0,sizeof(size));
		for(j=min(m,n);j>=1;j--)
		{
			for(p=0;p<=m-j;p++)
			{
				for(q=0;q<=n-j;q++)
				{
					if(tsst(p,q,p+j-1,q+j-1)==true)
					{
						cut(p,q,p+j-1,q+j-1);
						size[j]++;
						if(size[j]==1)
						count++;
					}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
		for(j=512;j>=1;j--)
		{
			if(size[j]!=0)
			cout<<j<<" "<<size[j]<<endl;
		}
	}
}
			
