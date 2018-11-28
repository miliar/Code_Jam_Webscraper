#include <vector>
#include <map>
#include <string>
#include <fstream>
#include <cstdio>
using namespace std;
int abs(int a)
{
	if(a<0) return -a; else return a;
}
int main2()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin>>T;
	for(int ti=1;ti<=T;ti++)
	{
		int L,P,C;
		int cnt=0;
		cin>>L>>P>>C;
		while(L*C<P)
		{
			L=L*C;
			//P=P/C;
			cnt++;
		}
		//cnt/=2;
		cout<<"Case #"<<ti<<": ";
		cout<<cnt;
		cout<<endl;
		printf("Test %d/%d complete! = %d\n",ti,T,cnt);
	}
	cin.close();
	cout.close();
	return 0;
}
/*#include <vector>
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
}*/