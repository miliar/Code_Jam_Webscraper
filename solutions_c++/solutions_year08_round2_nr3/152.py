#include <iostream>
#include <vector>

using namespace std;

int main()
{
  unsigned int T;
  cin >> T;
  unsigned int n,K;
  vector<unsigned int> v;

  for (int t=0; t<T; t++)
    {
      cin >> K >> n;
      v.clear();
      unsigned int deck[K];
      unsigned int d;
      unsigned int placed;
      unsigned int count;
      for (int i=0; i<n; i++)
	{
	  cin >> d;
	  v.push_back(d);
	}

      for (int i=0; i<K; i++)
	deck[i]=0;
      placed=0;

      unsigned int j=0;
      count=1;
      while (placed<K)
	{
	  //	  cout << count << " | " << placed+1 << endl;
	  if (count==placed+1 && deck[j]==0)
	    {
	      //	      cout << "placing " << placed+1 << "at " << j << endl;
	      deck[j]=placed+1;
	      count=1;
	      placed++;
	    }
	  if (deck[j]==0)
	    count++;
	  j=(j+1)%K;
	  //	  cout << "::" << placed << endl;
	}

      cout << "Case #" << t+1 << ": ";
      for (int i=0; i<n; i++)
	{
	  cout << deck[v[i]-1];
	  if (i<n-1)
	    cout << " ";
	}
      cout << endl;
    }

  return 0;
}
