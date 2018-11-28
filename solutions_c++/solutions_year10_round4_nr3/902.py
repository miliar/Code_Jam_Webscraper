#include<iostream>
using namespace std;
int main()
{
	int sun;
	cin>>sun;
	for(int pra=0;pra<sun;pra++)
	{
	int R;
	cin>>R;
	int arr[102][102];
	int x1,y1,x2,y2;
	for(int i=0;i<102;i++)
		for(int j=0;j<102;j++)
			arr[i][j]=0;
	int lx=0,ly=0;

	for(int i=0;i<R;i++)
	{
		cin>>x1>>y1>>x2>>y2;

		if(max(x1,x2)>lx)
			lx=max(x1,x2);

		if(max(y1,y2)>ly)
			ly=max(y1,y2);


		for(int j=x1;j<=x2;j++)
			for(int k=y1;k<=y2;k++)
				arr[j][k]=1;
	}

	int itemp=0;
	for(int i=1;i<=lx;i++)
		for(int j=1;j<=ly;j++)
			if(arr[i][j]==1)
			{
				itemp=1;
				break;
			}
	int ans=0;
	int brr[102][102];
		for(int i=0;i<102;i++)
			for(int j=0;j<102;j++)
				brr[i][j]=0;
	while(itemp)
	{
		ans+=1;
		int temp=0;
		for(int i=1;i<=lx+1;i++)
		{
			
			for(int j=1;j<=ly+1;j++)
			{
				//cout<<arr[i][j];

				if(arr[i][j]==1 && (arr[i-1][j]!=0 || arr[i][j-1]!=0))
				{
					brr[i][j]=1;
					temp=1;
				}

				if(arr[i][j]==0 && (arr[i-1][j]==1 &&  arr[i][j-1]==1))
				{
					brr[i][j]=1;
					temp=1;
				}

			}
			//cout<<endl;
		}
		//cout<<endl;
		if(temp==0)
			break;

		for(int i=0;i<102;i++)
		{
			for(int j=0;j<102;j++)
			{
				arr[i][j]=brr[i][j];
				brr[i][j]=0;
			}
		}
	}
	cout<<"Case #"<<pra+1<<": "<<ans<<endl;
	}
}
