#include <iostream>
#include <sstream>
#include <cstdlib>
#include <set>

using namespace std;

int main(int argc, char **argv) {
    
    int nbtests;
    cin >> nbtests;
  
    int A;
    int B;
    for (int test = 0; test < nbtests; test++)
    {
      cin >> A;
      cin >> B;
      int res = 0;
      
      for(int n = A; n < B; n++)
      {
	stringstream ss;
	ss << n;
	string chaine = ss.str();
	int longueur = chaine.length();
	
	set<int> liste;
	for(int pos = 1; pos < longueur; pos++)
	{  
	  string nouveau = chaine.substr(pos, longueur-pos) + chaine.substr(0, pos);
	  int m = atoi(nouveau.c_str());
	  
	  pair<set<int>::iterator,bool> ret = liste.insert(m);
	  if (ret.second == false)
	    continue;
	  
	  if(m > n && m <= B )
	    res++;
	}
	
      }
      cout << "Case #" << test+1 << ": " << res << endl;
    }

    return 0;
}
