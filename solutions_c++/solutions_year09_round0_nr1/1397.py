// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <string.h>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

//string split given string a and delimiters
vs strsp(string a, string delim=" ")
{
  vs ret;
  string cr = "";
  for(int i = 0; i < a.size(); i++)
  {
    if(delim.find(a[i])==string::npos) cr += a[i];
    else { if(cr.size()) ret.push_back(cr); cr = ""; }
  }
  if(cr.size()) ret.push_back(cr);
  return ret;
}

int main()
{
  int len, words, tcase;
  cin >> len >> words >> tcase;
  string dict[words];
  int dictnum[words][len];
  
  for(int i = 0; i < words; i++)
  {
  	cin >> dict[i];
  	for(int j = 0; j < len; j++)
  	{
  		dictnum[i][j] = (int)(dict[i][j]-'a');
  	}
  }
  
  
  for(int i = 0; i < tcase; i++)
  {
  	string miss = "";
  	cin >> miss;
  	bool posb[len][26];
  	memset(posb,false,sizeof(posb));
  	
  	int spot = 0;
  	int place = 0;
  	int inside = 0;
  	string acc = "";
  	
  	while(place < miss.size())
  	{
  		if( miss[place] == '(')
  		{
  			if(inside == 1)
  			{
  				deb("ERRRRRRROR1");
  				return 0;
  			}
  			inside = 1;
  		}
  		else if ( miss[place] == ')')
  		{
  			if(inside == 0)
  			{
  				deb("ERRRRROR2");
  				return 0;
  			}
  			for(int j = 0; j < acc.size(); j++)
  			{
  				posb[spot][ (int)(acc[j]-'a') ] = true;
  			}
  			acc = "";
  			spot++;
  			inside = 0;
  		}
  		else 
  		{
  			if(inside == 0)
  			{
  				posb[spot][ (int)(miss[place]-'a') ] = true;
  				spot++;
  			}
  			else if(inside = 1)
  			{
  				acc += miss[place];
  			}
  		}
  		place++;
  	}
  	
  	if(spot != len)
  	{
  		deb("ERRORR3");
  		return 0;
  	}
  	
  	int wordmatches = 0;
  	
  	for(int j = 0; j < words; j++)
  	{
  		int ok = 1;
  		for(int k = 0; k < len; k++)
  		{
  			if( !posb[ k ][ dictnum[j][k] ] )
  			{
  				ok = 0;
  				break;
  			}
  		}
  		if(ok) wordmatches++;
  	}
  	
  	printf("Case #%d: %d\n",i+1,wordmatches);
  }

  return 0;
}















