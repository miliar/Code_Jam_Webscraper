#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std ;

#define S_LIMIT 100
#define N_LIMIT 20
#define Q_LIMIT 1000

map<string, int> mapn ;
set<int> setn ;

unsigned int ncase, neng, nsch ;

int mapeng(string &s)
{
  int k ;
  if (mapn.count(s))
    k = mapn[s];
  else
  {
      k = mapn.size();
      mapn[s] = k;
  }
  return k;
}

int main()
{
    string buff ;
    
    unsigned int i, j, k, sw ;
    
    cin >> ncase ;
    //    cout << "---" << ncase ;
    
    for (i = 0 ; i < ncase ; ++i)
    {
	cin >> neng ;
	//	cout << "---" << neng ;
	cin.ignore() ;
	mapn.clear() ;
	for (j = 0 ; j < neng; ++j)
	{
	    getline(cin, buff) ;
	    //cout << "---" << buff ;
	    mapeng(buff) ; 
	}
	cin >> nsch ;
	cin.ignore() ;
	//cout << "---" << nsch << "---\n";

	sw = 0 ;
	setn.clear() ;
	for (j = 0 ; j < nsch ; ++j)
	{
	    getline(cin, buff) ;
	    //cout << "---" << buff ;
	    k = mapeng(buff) ;
	    setn.insert(k) ;
	    if (setn.size() == neng)
	    {
		setn.clear() ;
		setn.insert(k) ;
		++sw ;
	    }
	}
	printf("Case #%d: %d\n", i + 1, sw) ;
    }
}
