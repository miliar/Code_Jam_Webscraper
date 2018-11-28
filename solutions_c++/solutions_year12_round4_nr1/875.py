#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <map>
#include <bitset>
#include <numeric> //accumulate



using namespace std;

int main()
{
  int totCase;
  cin >> totCase;
  for(int i = 0; i < totCase; ++i)
    {
      cout << "Case #" << (i+1) << ": ";
      int num;
      cin >> num;
      vector<long int> table;
      vector<long int> pos;
      vector<long int> len;
      long int dis;
      for(int j = 0; j < num; ++j)
	{
	  long int p, l;
	  cin >> p >> l;
	  pos.push_back(p);
	  len.push_back(l);
	  table.push_back(0);
	}
      cin >> dis;
      table[0] = 2*pos[0];
      for(int j = 1; j < pos.size(); ++j)
	{
	  for(int k = 0; k < j; ++k)
	    {
	      if(table[k] >= pos[j])
		{
		  long int ll = pos[j]-pos[k];
		  if(ll > len[j])
		    {ll = len[j];}
		  if(table[j] < pos[j] + ll)
		    {table[j] = pos[j] + ll;}
		}
	    }
	}
      int j = 0;
      for(; j < table.size(); ++j)
	{
	  if(table[j] >= dis)
	    {cout << "YES" << endl; break;}
	}
      if(j == table.size())
	{cout << "NO " << endl;}
    }
}
