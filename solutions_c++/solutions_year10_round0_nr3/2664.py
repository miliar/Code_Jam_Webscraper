#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<stack>
#include<math.h>
#include<queue>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	long test_cases=0,N=0,K=0,R=0;
	cin>>test_cases;
	for(int i=0; i<test_cases;i++)
	{
		cin>>R;
		cin>>K;
		cin>>N;
		queue<int> q;
		int revenue=0;
		for(int j=0;j<N;j++)
		{
			int temp=0;
			cin>>temp;
			q.push(temp);
		}
		for(int o=0;o<R;o++)
		{
			int sum=0;
				for(int j=0; j<q.size();j++)
				{
					int temp=q.front();
					if((sum+temp)>K)break;
					sum+=temp;
					q.push(temp);
					q.pop();
				}
				revenue+=sum;
		}
		cout<<"Case #"<<(i+1)<<": "<<revenue<<endl;
	}
	
	return 0;
}
