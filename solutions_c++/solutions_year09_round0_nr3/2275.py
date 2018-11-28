#include <iostream>
#include <string>

using namespace  std;

const int nmax = 1000;
const int mmax = 50;

string word = "welcome to code jam";
int x[nmax][mmax];

int main ()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int n;
	cin >> n;
	cin.ignore(1);
	for (int i=0; i<n; i++)
	{
		string tmp;
		getline(cin, tmp);
		for (int j=0; j<nmax; j++)
			for (int k=0; k<mmax; k++)
				x[j][k] = 0;
		for (int j=0; j<tmp.length(); j++)
			if (tmp[j] == 'w')
			{
				x[j][1] = 1;
			}
		for (int j=1; j<word.length(); j++)
			for (int ii=0; ii<tmp.length(); ii++)
				for (int iii=0; iii<ii; iii++)
					if (word[j-1] == tmp[iii] && word[j] == tmp[ii])
					{
						x[ii][j+1] = (x[ii][j+1] + x[iii][j-1+1]) % 10000;
					}
		int ans = 0;
		for (int j=0; j<tmp.length(); j++)
			ans = (ans + x[j][word.length()]) % 10000;
		cout << "Case #" << i+1 << ": ";
		if (ans == 0)
		{
			cout << "0000";
		}
		else if (ans<10)
		{
			cout << "000";
			cout << ans;
		}
		else if (ans<100)
		{
			cout << "00";
			cout << ans;
		}
		else if (ans<1000)
		{
			cout << "0";
			cout << ans;
		}
		else
		{
			cout << ans;
		}
		cout << '\n';
	}
    return 0;
}
