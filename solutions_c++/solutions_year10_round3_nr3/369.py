#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <cstring>
using namespace std;

#define out(a) for (int j = 0; j < a.size(); j++) cout << a[j] << "\n";

map < char , int > val;

long long toDecimal (string h)
{
  long long res = 0;
  int p = 0;
  for (int i = h.size()-1; i >= 0; i--,p++)
  {
    res += (long long)pow(16.0,(double)p)*val[h[i]];
  }
  return res;
}

string toBinary (string h)
{
  long long d = toDecimal(h);
  string ret;
  if (d == 0) return "0";
  while (d)
  {
    ret += (d%2)+48;
    d /= 2;
  }
  reverse(ret.begin(),ret.end());
  return ret;
}

bool chess (vector <string> c)
{
  for (int i = 1; i < c.size(); i++)
  {
    for (int j = 0; j < c[i].size(); j++)
    {
      int k1 = c[i][j]-'0';
      int k2 = c[i-1][j]-'0';
      if (k1 + k2 != 1) return false;
    }
  }
  
  for (int i = 1; i < c[0].size(); i++)
  {
    for (int j = 0; j < c.size(); j++)
    {
      int k1 = c[j][i]-'0';
      int k2 = c[j][i-1]-'0';
      if (k1 + k2 != 1) return false;
    }
  }
  return true;
}
  
int main ()
{
	for (char a = '0'; a <= '9'; a++) val[a] = a-'0';
	val['A'] = 10;
	val['B'] = 11;
	val['C'] = 12;
	val['D'] = 13;
	val['E'] = 14;
	val['F'] = 15;
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		cout << "Case #" << T << ": ";
		int m,n;
		cin >> m >> n;
		vector < string > arr(m);
		for (int i = 0; i < m; i++) cin >> arr[i];
		
		vector < string > board(m);
		for (int i = 0; i < m; i++)
		{
		  board[i] = toBinary(arr[i]);
		  int d = n-board[i].size();
		  while (d--) board[i] = "0" + board[i];
		}
		//cout << "\n"; out(board); cout << "\n";
		int sel[m][n];
		memset(sel,0,sizeof(sel));
		map <int,int> fr;
		for (int k = n; k >= 1; k--)
		{
		  for (int i = 0; i < m; i++)
		  {
		    for (int j = 0; j < n; j++)
		    {
		      if (sel[i][j]) continue;
		      if (j + k-1 >= n || i + k-1 >= m) continue;
		      vector <string> temp;
		      bool poss = true;
		      for (int a = i; a <= i+k-1; a++)
		      {
			for (int b = j; b <= j+k-1; b++)
			{
			  if (sel[a][b]) { poss = false; break; }
			}
			if (!poss) break;
		      }
		      if (!poss) continue;
		      for (int a = i; a <= i+k-1; a++)
		      {
			temp.push_back(board[a].substr(j,k));
		      }
		      if (chess(temp)) 
		      { 
			fr[k]++; 
			//cout << i << " " << j << " " << k << "\n";
			for (int a = i; a <= i+k-1; a++)
			{
			  for (int b = j; b <= j+k-1; b++) sel[a][b] = 1;
			}
		      }
		    }
		  }
		}
		//cout << "\n";
		cout << fr.size() << "\n";
		map <int,int> :: iterator it;
		vector < pair <int,int> > ans;
		for (it = fr.begin(); it != fr.end(); it++)
		{
		  pair <int,int> p((*it).first,(*it).second);
		  ans.push_back(p);
		}
		sort(ans.rbegin(),ans.rend());
		for (int i = 0; i < ans.size(); i++) cout << ans[i].first << " " << ans[i].second << "\n";
	}
	return 0;
}
