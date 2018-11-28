#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define CLR(a,x) memset((a),(x),sizeof((a)))

typedef istringstream iss; typedef ostringstream oss; typedef long long int lli;
const double TOLL=1e-9;

int main()
{
	int t; cin>>t; string s,bkup; int k; 
	int cn=0;
	while(t--)
	{
		cin>>k>>s;
		bkup=s;
		string encode=s;
		vector<int> tmp;
		for(int i=0;i<k;i++) tmp.push_back(i);
		int rv=1000000000;
		do
		{
			encode="";
			for(int st=0;st<sz(s);st+=k)
			{
				bkup=s.substr(st,k);
				string tbkup=bkup;

				for(int i=0;i<k;i++) tbkup[i]=bkup[tmp[i]];
				encode+=tbkup;
			}
			

			int tsize=0; char prev='!';
			for(int i=0;i<sz(s);i++)
			{
				if(prev==encode[i]) continue;
				tsize++; prev=encode[i];
			}
			rv=min(tsize,rv);
		}while(next_permutation(all(tmp)));
		cn++;
		cout<<"Case #"<<cn<<": ";
		cout<<rv<<endl;
		
	}

	return 0;
}
