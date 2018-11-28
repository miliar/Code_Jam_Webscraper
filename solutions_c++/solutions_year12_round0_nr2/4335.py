#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;




int main()
{

	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n,s,p;
		cin>>n>>s>>p;
		vector<int> v(n);
		int cnt=0;
		for(int j=0;j<n;j++)
		{
			int x;
			cin>>x;
			v[j]=x;
			if(v[j]>=3*p-2)
			{
				cnt++;
			}

			if((v[j]==3*p-3 || v[j]==3*p-4) && s>0 && v[j]!=0)
			{
				s--;
				cnt++;
			}
		}
		printf("Case #%d: %d\n",i+1,cnt);


			

	}
	return 0;
}
