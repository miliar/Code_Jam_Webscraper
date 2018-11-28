#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<cmath>
using namespace std;

int main()
{

	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for (int curt=1;curt<=test;curt++)
	{
		int n;
		cin>>n;
		int res=0;
		for (int i=0;i<n;i++)
		{
			int a;
			cin>>a;
			if (a!=i+1)
				res++;
		}
		cout<<"Case #"<<curt<<": ";
		printf("%.6lf",double(res));
		cout<<endl;
	}

	


	 

	return 0;
}