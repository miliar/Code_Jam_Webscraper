#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int C;
int main()
{
	freopen("B-large.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
//	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	cin>>C;
	int Case;
	string N;
	for(Case = 1; Case <= C; Case++)
	{
		cin>>N;
		
		string nextN = N;
		next_permutation(nextN.begin(), nextN.end());
		string ans;
		if(nextN > N) ans = nextN;
		else 
		{
			int i; 
			for(i = 0; i < nextN.length(); i++) if(nextN[i] != '0') break;
			int t = nextN[0];
			nextN[0] = nextN[i];
			nextN[i] = t;
			ans = nextN.substr(0, 1) + "0" + nextN.substr(1);
		}
		//printf("Case #%d: \n", Case);
		cout<<"Case #"<<Case<<": ";
		cout<<ans<<endl;
	}
}