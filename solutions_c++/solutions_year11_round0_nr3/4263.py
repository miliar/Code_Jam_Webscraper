#include<iostream>
#include<vector>

using namespace std;

	
int main()
{
	freopen ("prog.in", "r", stdin);
	freopen ("prog.out", "w", stdout);
	int T;
	cin>>T;
	vector<int> res;
	for(int i=0;i<T;i++)
	{
		int N,j,sum=0,minim=1000000000,xor=0;
		cin>>N;
		for(j=0;j<N;j++)
		{
			int temp;
			cin>>temp;
			minim=min(minim,temp);
			sum+=temp;
			xor=xor^temp;
		}
		if(xor==0)
			res.push_back(sum-minim);
		else
			res.push_back(-1);

	}
	for(int j=0;j<T;j++)
	{
		if(res[j]!=-1)
			printf ("Case #%d: %d\n", j+1, res[j]);
		else
			printf ("Case #%d: NO\n", j+1);
	}
}