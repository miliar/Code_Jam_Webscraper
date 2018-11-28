#include <iostream>
#include <set>
#include <map>
#include <string>

using namespace std;

map<string, char> C;
set<string> D;
char Seq[105];

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    C.clear();
    D.clear();
		int c, d, n;
		cin >> c;
		for (int i = 0; i < c; i++)
		{
			string s;
			char x, y, z;
			cin >> x >> y >> z;
			C[s + x + y] = z;
			C[s + y + x] = z;
		}
		cin >> d;
		for (int i = 0; i < d; i++)
		{
			string s;
			char x, y;
			cin >> x >> y;
			D.insert(s + x + y);
			D.insert(s + y + x);
		}
		int l = 0;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> Seq[l++];
			string t;
			t += Seq[l-2];
			t += Seq[l-1];
			if (l <= 1) continue;
			if (C.find(t)!= C.end())
			{
				Seq[l-2] = C[t];
				l--;
			}
			else 
			{
				t = "";
				t += Seq[l-1];
				for (int j = 0; j < l - 1; j++)
				{
					if (D.find(t + Seq[j]) != D.end())
					{
						l = 0;
						break;	
					}
				}
			}
		}
    cout << "[";
    for (int i = 0; i < l; i++)
    {
    	cout << Seq[i];
    	if (i != l-1)
    		cout << ", ";
    }
		cout << "]";
    cout << endl;
  }
  return 0;
}