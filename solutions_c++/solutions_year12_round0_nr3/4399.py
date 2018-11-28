#include<fstream>
#include<sstream>

using namespace std;

int work(int x,int a,int b)
{
	int cnt=0;

	int t1,t2;
	string s1,s2;
	stringstream stream;
	for(int i=10;i<x;i*=10)
	{
		t1=x%i;
		t2=x/i;
		stream<<t1;
		stream>>s1;
		stream.clear();
		stream<<t2;
		stream>>s2;
		stream.clear();
		s1+=s2;
		stream<<s1;
		stream>>t1;
		stream.clear();
		
		if(t1<=b&&t1>=a&&t1!=x)
			cnt++;
	}

	return cnt;
}

int main()
{
	ifstream ip("C-small-attempt0.in");
	ofstream op("C-small-attempt0.out");

	int t;
	ip>>t;
	for(int tt=0;tt<t;tt++)
	{
		int a,b;
		ip>>a>>b;
		
		int ans=0;
		for(int i=a;i<=b;i++)
		{
			ans+=work(i,a,b);
		}

		op<<"Case #"<<tt+1<<": "<<ans/2<<endl;
	}


	return 0;
}

