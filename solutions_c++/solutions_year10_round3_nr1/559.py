#include <fstream>
#include <vector>
#include <set>
#include <map>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{
	int T;
	cin>>T;
	for(int tn=1;tn<=T;tn++)
	{
		int n;
		cin>>n;
		vector<int> a(n), b(n);
		for(int i=0;i<n;i++)
		{
			cin>>a[i]>>b[i];
		}
		int res=0;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if((a[i]<a[j])^(b[i]<b[j]))res++;
			}
		}
		cout<<"Case #"<<tn<<": "<<res<<endl;
	}
	
}