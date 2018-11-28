#include <iostream>
#include <vector>
using namespace std;

int P,Q;
bool line[1001];
vector<int> a;
int main()
{
	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{

		a.clear();
		cin>>P>>Q;
		for(int i=1;i<=Q;i++)
		{
			int tmp;
			cin>>tmp;
			a.push_back(tmp);
		}
		
		int minval=2000000000;
		
		do
		{
			memset(line,0,sizeof(line));
			int tval=0;
			
			for(int i=0;i<a.size();i++)
			{
				line[a[i]]=1;
				for(int k=a[i]-1;k>0;k--)
				{
					if(line[k]) break;
					tval++;
				}
				for(int k=a[i]+1;k<=P;k++)
				{
					if(line[k]) break;
					tval++;
				}
			}
			
			minval=min(minval,tval);
		}
		while(next_permutation(a.begin(),a.end()));
		
		cout<<"Case #"<<t<<": "<<minval<<endl;
		
		
	}
}
