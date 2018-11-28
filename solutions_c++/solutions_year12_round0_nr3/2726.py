#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
void split(int *arr,int toSplit,int size)
{
	for(int i=size-1 ; i>=0 ; i--)
	{
		arr[i]=toSplit%10;
		toSplit/=10;
	}
}
void join(int *arr,int & toJoin,int size)
{
	toJoin=0;
	int temp=1;
	for(int i=1 ; i<size ; i++)
		temp*=10;
	for(int i=0 ; i<size ; i++)
	{
		toJoin+=arr[i]*temp;
		temp/=10;
	}
}
int calc(int start,int end)
{
	int ans=0;
	int temp=end;
	int digit=0;
	while(temp)
	{
		temp/=10;
		digit++;
	}
	int *arr=new int[digit];
	for(int i=start ; i<end ; i++)
	{
		int *t=new int[digit];
		split(arr,i,digit);
		for(int j=0 ; j<digit ; j++)
		{
			if(digit==1)
				continue;
			temp=arr[digit-1];
			for(int k=digit ; k>0 ; k--)
				arr[k]=arr[k-1];
			arr[0]=temp;
			join(arr,temp,digit);
			t[j]=temp;
			
			if( temp<=end && i<temp && arr[0]!=0)
			{
				int check=0;
				for(int k=0 ; k<j ; k++)
				if(t[k]==temp)
					check=1;
				if(check==0)
					ans++;
			}
		}
	}
	return ans;
}
void main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int caseNumber;
	cin>>caseNumber;
	for(int a=0 ; a<caseNumber ; a++)
	{
		int st,end;
		cin>>st>>end;
		int ans=calc(st,end);
		cout<<"Case #"<<a+1<<": "<<ans<<endl;
	}
}