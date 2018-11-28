#include<string>
#include<vector>
#include<iostream>
#include<utility>
#include<algorithm>
#include<set>
#include<stack>
#include<sstream>
#include<math.h>
#include<map>

using namespace std;

#define ll long long
#define PB push_back
#define VI vector<int>
#define VS vector<string>

int main(int argc, char** argv)
{
  ll T;
  cin >> T;
  for(ll i = 0; i < T; ++i)
    {
      
      ll R, K, N;
      cin >> R >> K >> N;
      ll groups[N];
      for(ll j = 0; j < N; ++j)
	{
	  cin >> groups[j];
	}

      ll index = 0;
      ll cost = 0;
      map<ll, pair<ll, ll> > values;

      for(ll j = 0; j < R; ++j)
	{
	  ll capacity = 0;
	  map<ll, pair<ll, ll> >::iterator it = values.find(index);
	  if(it != values.end())
	    {
	      cost += it->second.second;
	      index = (index + it->second.first) % N;
	    }
	  else
	    {
	      ll startIndex = index;
	      for(ll k = 0; k < N; ++k)
		{
		  if((capacity + groups[index]) <= K)
		    {
		      capacity += groups[index];
		    }
		  else
		    {
		      break;
		    }
		  index = (index + 1) % N;
		}
	      values.insert(pair<ll, pair<ll, ll> >(startIndex, pair<ll, ll>((index - startIndex), capacity)));
	      cost += capacity;
	    }
	}
      cout << "Case #" << (i+1) << ": " << cost << endl;
    }
}
