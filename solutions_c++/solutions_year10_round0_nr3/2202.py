#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;


int main()
{
	int T,R,K,N;
	cin>>T;
	int temp;
	int ans,caseNum=1;
	
	while(T--)
	{
		queue<int> quedata,quebak;
		ans=0;
		cin>>R>>K>>N;
		while(N--)
		{
			cin>>temp;
			quedata.push(temp);
		}
		while(R--)
		{
			int kbak=0;
			int postemp;
			while(kbak<K&&!quedata.empty())
			{
				if(kbak+quedata.front()<=K)
				{
					ans+=quedata.front();
					kbak+=quedata.front();
					quebak.push(quedata.front());
					quedata.pop();
				}
				else
				{
					break;
				}
			}
			while(!quebak.empty())
			{
				quedata.push(quebak.front());
				quebak.pop();
			}
		}
		printf("Case #%d: %d\n",caseNum++,ans);
	}
	return 0;
}