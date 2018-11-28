#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int T;
	cin >> T;
	bool poss;
	for(int t=1;t<=T;t++)
	{
		poss=0;
		int n,pd,pg;
		cin >> n >> pd >>pg;
		for(int i=1;i<=n;i++)
		{
			if(pg==0 && pd==0)
			{
				poss=1; break;
				}
			if(pg==0 && pd!=0)
			{
				break;
			}
			if(100%i!=0)
				continue;
			if(pd%(100/i))
				continue;
			if(pg==100 && pd!=100)
				continue;
			if(pd==100&&pg==100)
			{
				poss=1;
				break;
			}	
			int w=i*pd/100;
			int x=(100*w+pg*i)/(100-pg);
			if(x>0){
				poss=1;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if(poss)
			cout << "Possible";
		else
			cout << "Broken";
		cout << endl;
	}
}
