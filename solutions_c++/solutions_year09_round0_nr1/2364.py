#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

const int nmax = 10000;

string dict[nmax];
int logic[nmax];

set<char> setc;

int main ()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int l,d,n;
	cin >> l >> d >> n;
	
	for (int i=0; i<d; i++)
	{
		cin >> dict[i];
	}
	
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<d; j++)
			logic[j] = 1;
		
		string word;
		cin >> word;
		
		
		int ii=0;
		
		for (int j=0; j<word.length(); j++)
		{
			setc.clear();
			
			if (word[j]=='(')
			{
				while (true)
				{
					j++;
					if (word[j]==')') break;
					else
					{
						setc.insert(word[j]);
					}

				}
			}
			else
			{
				setc.insert(word[j]);
			}
			
			for (int k=0; k<d; k++)
				logic[k] *= (setc.count(dict[k][ii])>0);
			
			ii++;
		}
		
		int ans = 0;
		
		for (int j=0; j<d; j++)
			ans += logic[j];
		
		cout << "Case #" << i+1 << ": " << ans << endl;
		
	}
    return 0;
}
