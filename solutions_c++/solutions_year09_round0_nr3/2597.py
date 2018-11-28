#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
	string pat="welcome to code jam";
	string t;
	int N;
	cin>>N;
	getline(cin, t);
	for(int q=1; q<=N; q++)
	{
		getline(cin, t);
		int m=pat.length(), n=t.length();
		vector<vector<long long> > v(m+1, n+1);
		for(int j=0; j<=m; j++) v[j][0]=0;
		for(int i=0; i<=n; i++) v[0][i]=1;
		for(int i=1; i<=m; i++) for(int j=1; j<=n; j++)
			if(pat[i-1]==t[j-1])
				{
					v[i][j]=(v[i][j-1]+v[i-1][j-1])%10000;
				}
			else
				v[i][j]=v[i][j-1];

		cout<<"Case #"<<q<<": "<<setw(4)<<setfill('0')<<v[m][n]<<endl;
	}
	return 0;

}
