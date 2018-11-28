#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<iomanip>

using namespace std;


int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int t;
	cin>>t;
	for(int tt=0; tt<t; tt++)
	{
		int a, b;
		cin>>a>>b;
		int count = 0;
		for(int k = a; k<=b; k++)
		{
			int d = 0;
			int kk = k;
			while(kk>0) {kk/=10; d++;}
			kk=k;
			for(int i = 1; i<d; i++)
			{
				int l  = kk%10;
				kk/=10;
				for(int j = 1; j<d; j++) l*=10;
				kk+=l;
				if(kk>k && kk<=b) count++;
			}
		}
		cout<<"Case #"<<tt+1<<": "<<count<<endl;
	}
	return 0;
}