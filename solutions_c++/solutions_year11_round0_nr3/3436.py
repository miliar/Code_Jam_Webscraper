#include "iostream"
//#include "stdio.h"

using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,id = 1,i,res,sum,min; 
	int t;
	int num[1005];
	//scanf("%d",&t);
	cin >> t;
	while(t--)
	{
		res = 0;
		cin>>n;
		//scanf("%d",&n);
		sum = 0;
		for(i = 0;i < n; i++)
		{
			//scanf("%d",num + i);
			cin >> num[i];
			res = res ^ num[i];
			sum = sum + num[i];
		}
		if(res != 0)
		{
			cout<<"Case #"<<id++<<": "<<"NO"<<endl;
			//printf("Case #%d: NO\n",id++);
		}
		else
		{
			for(i = 0,min = num[i] ; i< n; i++)
				if(min > num[i])
					min = num[i];
			cout<<"Case #"<<id++<<": "<<sum - min<<endl;
			//printf("Case #%d: %d\n",id++,sum - min);
		}

	}

	return 1;
}