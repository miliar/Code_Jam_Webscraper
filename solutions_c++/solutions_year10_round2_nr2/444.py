#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int T;
	int n,k,b,t;
	int bird[100];
	int sp[100];
	double ti[100];
	ofstream fout("ans");
	cin >> T;
	for(int p=0;p<T;p++)
	{
		cin >> n >> k >> b >> t;
		for(int i=0;i<n;i++)
			cin >> bird[i];
		for(int i=0;i<n;i++)
			cin >> sp[i];
		for(int i=0;i<n;i++)
			ti[i] = (double)(b-bird[i])/sp[i];
		int exp = 0;
		int c = 0;
		for(int i=n-1;i>=0;i--)
		{
			if( ti[i] <=t)
			{
				for(int j=i+1;j<n;j++)
					if(ti[j]>t)
					{
						exp++;
					}
				c++;
			}
			if(c==k)
				break;
		}
		fout << "Case #" <<p+1 << ": ";
		if(c==k)
			fout << exp << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}
}