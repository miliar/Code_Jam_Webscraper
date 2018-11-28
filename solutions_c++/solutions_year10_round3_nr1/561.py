#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <fstream>
#include <cstdio>
using namespace std;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin>>T;
	for(int ti=1;ti<=T;ti++)
	{
		int n;
		cin>>n;
		vector<int> a(n),b(n);
		for(int i=0;i<n;i++)
		{
			cin>>a[i]>>b[i];
		}
		int cnt=0;
		for(int i=1;i<n;i++)
			for(int j=0;j<i;j++)
				if((a[i] - a[j]) * (b[i] - b[j])<0) cnt++;
		cout<<"Case #"<<ti<<": ";
		cout<<cnt;
		cout<<endl;
		printf("Test %d/%d complete! = %d\n",ti,T,cnt);
	}
	cin.close();
	cout.close();
	return 0;
}