#include <iostream>

using namespace std;

int m[256];
int mcnt;

int main()
{
	int TestCases;
	cin >> TestCases;
	for(int ti=0;ti<TestCases;ti++)
	{
		long long ret=0;
		string a;
		cin >> a;
		int an=a.length();
		
		for(int i=0;i<256;i++)
			m[i]=-1;
		
		m[(int)a[0]]=1;
		mcnt=1;
		for(int i=1;i<an;i++)
		{
			if(m[(int)a[i]]==-1)
			{
				if(mcnt==1)
					m[(int)a[i]]=0;
				else
					m[(int)a[i]]=mcnt;
				mcnt++;
			}
		}

		if(mcnt==1)
			mcnt=2;
		{
			long long k=1;
			for(int i=an-1;i>=0;i--)
			{
				ret += m[(int)a[i]]*k;
				k=k*mcnt;
			}
		}
		
		cout << "Case #"<<ti+1<<": " << ret << endl;

	}
}

