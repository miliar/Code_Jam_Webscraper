#include <iostream>
#include <fstream>
#include <cstdio>
#include <queue>
using namespace std;

int main()
{
	int t,tt;
	cin >>t;
	ofstream output;
	output.open("D:\\res.txt");
	for(int tt=1;tt<=t;tt++)
	{
		int ans,n;
		cin >>n;
		queue<int> o,b,turn;
		char rb[5];
		int bt;
		for(int i=0;i<n;i++)
		{
			cin >>rb>>bt;
			if(rb[0]=='O')
			{
				o.push(bt);
				turn.push(0);
			}
			else
			{
				b.push(bt);
				turn.push(1);
			}		
		}
		ans=0;
		int bp=1,op=1;
		while(!turn.empty())
		{
			int cur=turn.front();
			turn.pop();
			int onext,bnext;
			int add=0;
			if(cur==0)
			{
				onext=o.front();
				if(onext>op) add=onext-op+1;
				else add=op-onext+1;
				op=onext;
				if(!b.empty())
				{
					bnext=b.front();
					if(bnext>bp)
					{
						bp+=add;
						if(bp>bnext) bp=bnext;
					}
					else if(bnext<bp)
					{
						bp-=add;
						if(bp<bnext) bp=bnext;
					}
				}
				o.pop();		
			}
			else
			{
				bnext=b.front();
				if(bnext>bp) add=bnext-bp+1;
				else add=bp-bnext+1;
				bp=bnext;
				if(!o.empty())
				{
					onext=o.front();
					if(onext>op)
					{
						op+=add;
						if(op>onext) op=onext;
					}
					else if(onext<op)
					{
						op-=add;
						if(op<onext) op=onext;
					}
				}
				b.pop();
			}
			ans+=add;
		}
	//	printf("Case #%d: %d\n",tt,ans);
	//	cout <<"Case #"<<tt<<": "<<ans<<endl;
		output <<"Case #"<<tt<<": "<<ans<<endl;
	}
	output.close();
	return 0;
}
