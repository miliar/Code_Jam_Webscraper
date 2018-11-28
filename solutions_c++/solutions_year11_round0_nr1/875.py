#include<fstream>
#include<string>
#include<algorithm>

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
		int tO = 0;
		int tB = 0;
		int sO = 1;
		int sB = 1;
		int time = 0;
		for (int i=0; i<n; i++)
		{
			string type;
			cin>>type;
			int p;
			cin>>p;
			if (type=="O")
			{
				int need = max(1, abs(p-sO) + 1- time + tO);
				time+=need;
				sO = p;
				tO = time;
			}
			if (type=="B")
			{
				int need = max(1, abs(p-sB) + 1- time + tB);
				time+=need;
				sB = p;
				tB = time;
			}
		}
		cout<<"Case #"<<tt+1<<": "<<time<<endl;
	}
	return 0;
}