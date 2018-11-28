#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<iomanip>

using namespace std;

long long nod(long a, long b)
{
	if (a<b) return nod(b, a);
	if (b==0) return a;
	return nod(b, a%b);
}

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int t;
	cin>>t;
	//cout.flags(std::ios::fixed);
	//cout<<setprecision(6);
	for(int tt=0; tt<t; tt++)
	{
		long long n;
		cin>>n;
		int pg, pd;
		cin>>pd>>pg;
		bool pos = false;
		if (pg==100)
		{
			if (pd==100) pos=true;
			else pos=false;
		}
		else
		{
			if (pd==0) pos=true;
			else
			{
				if (pg==0) pos=false;
				else
				{
					long long mind = 100/nod(100, pd);
					long long todayw = pd/nod(100, pd);
					if (mind<=n) 
					{
						pos = true;
					}

				}
			}
		}

		if (pos)
			cout<<"Case #"<<tt+1<<": "<<"Possible"<<endl;
		else
			cout<<"Case #"<<tt+1<<": "<<"Broken"<<endl;
	}
	return 0;
}