#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int t;
	cin>>t;
	for(int tt=0; tt<t; tt++)
	{
		int n;
		cin>>n;
		int sum=0;
		int xor=0;
		int mi=1000000000;
		for(int i=0; i<n; i++)
		{
			int p;
			cin>>p;
			sum+=p;
			if (p<mi) mi=p;
			xor^=p;
		}
		cout<<"Case #"<<tt+1<<": ";
		if (xor==0) cout<<sum-mi;
		else cout<<"NO";
		cout<<endl;
	}
	return 0;
}