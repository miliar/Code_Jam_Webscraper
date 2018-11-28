#include<iostream>
#define pos(x) ((x)<0)?(-(x)):((x))
using namespace std;
int main()
{
	int t,tbc;
	cin>>t;
	tbc = t;
	while(t--)
	{
		int n;
		cin>>n;
		int arr[n][2],op=1,bp=1,temp;
		for(int i=0;i<n;i++)
		{	
			char ch;
			int but;
			cin>>ch;
			if(ch=='O')
			{
				arr[i][0] = 0;
				cin>>temp;
				arr[i][1] = pos(temp-op);
				op = temp;
			}
			else
			{
				arr[i][0] = 1;
				cin>>temp;
				arr[i][1] = pos(temp-bp);
				bp = temp;
			}
		}

		unsigned long long sec = 0;
		for(int i=0;i<n;i++)
		{
			int j=i+1;
			while(j<n && arr[j][0]==arr[i][0])j++;
			if(j<n)
			{
				int diff = arr[j][1] - arr[i][1] - 1;
				if(diff<0)arr[j][1] = 0;
				else arr[j][1] = diff;
			}
			sec += arr[i][1] + 1;
		}
		
		cout<<"Case #"<<tbc-t<<": "<<sec<<endl;
	}
	return 0;
}
