#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 105;
const int nnnn = 500;
const char b[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

char a[nmax];
char comb[nnnn][nnnn];
int opposed[nnnn][nnnn];
int base[nnnn];

int check(char q)
{
	for (int i = 0;i < 8; ++i)
		if (b[i]== q) return false;
	return true;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){

		memset(comb,0,sizeof(comb));
		memset(opposed,0,sizeof(opposed));
		memset(base,0,sizeof(base));

		int c;
		cin >> c;

		for (int i = 0;i < c; ++i)
		{
			string s;
			cin >> s;
			comb[s[0]][s[1]] = s[2];
			comb[s[1]][s[0]] = s[2];
			//if (check(s[0]) || check(s[1]) || !check(s[2])) while (true) cout << 1;
		}
		int d;
		cin >> d;

		for (int i = 0;i < d; ++i)
		{
			string s;
			cin >> s;
			opposed[s[0]][s[1]] = 1;
			opposed[s[1]][s[0]] = 1;
			//if (check(s[0]) || check(s[1])) while (true) cout << 1;
		}

		int n;

		cin >> n;

		string s;

		cin >> s;

		int num = 0;

		for (int i = 0;i < s.size(); ++i)
		{
			a[num++] = s[i];

			base[s[i]]++;

			if (num > 1)
			{
				if (comb[a[num-2]][a[num-1]] != 0)
				{
					base[a[num-2]]--;
					base[a[num-1]]--;
					a[num-2] = comb[a[num-2]][a[num-1]];					
					num--;
				}
				else
				{
					for (int i = 0;i < 300; ++i)
						if (base[b[i]] > 0 && opposed[b[i]][a[num-1]])
						{
							num = 0;
							memset(base,0,sizeof(base));
							break;
						}
				}
				
			}
		}		
		printf("Case #%i: ",test);		

		cout << "[";

		if (num > 0) 
		{
			cout << a[0];

			for (int i = 1;i < num; ++i) cout << ", " << a[i];
		}
		
		cout << "]" << endl;

	}
	
	return 0;
}