#include <fstream>

using namespace std;

ifstream cin("A.in");
ofstream cout("A.out");

int main()
{
	int n;
	cin>>n;
	for (int i=0;i<n;i++)
	{
		int m;
		unsigned long long k;
		cin>>m>>k;
		bool on=true;
		for (int j=0;j<m;j++)
		{
			if (!(k&1))
			{
				on=false;
				break;
			}
			k>>=1;
		}
		if (on)
		{
			cout<<"Case #"<<i+1<<": ON"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": OFF"<<endl;
		}
	}
}
