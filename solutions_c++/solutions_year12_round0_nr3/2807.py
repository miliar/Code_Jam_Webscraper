#include <iostream>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <set>

using namespace std;



// More intelligent, it is not just a bruteforce algorithme.
// It is more efficient but not very good (quick coding) ...
int nbRecyclable(int n, const string& mStr)
{
	set<string> nbrFound;
	int nb = 0;
	
	ostringstream os;
	os << n;
	string nStr = os.str();
	
	// Variation de taille
	for(int i=1 ; i<nStr.size() ; i++)
	{
		string str = nStr.substr(nStr.size()-i, i) + nStr.substr(0, nStr.size()-i);
		
		if(str[0] != '0' && nStr < str && str <= mStr)
			nbrFound.insert(str);
	}
	
	return nbrFound.size();
}



int findRecycle(int min, int max)
{
	int nbRecycled = 0;
	
	ostringstream os;
	os << max;
	const string mStr = os.str();
	
	for(int i=min ; i<max ; i++)
		nbRecycled += nbRecyclable(i, mStr);
	
	return nbRecycled;
}



int main()
{
	int nbCases;
	cin >> nbCases;
	
	for(int i=0 ; i<nbCases ; i++)
	{
		int min, max;
		cin >> min;
		cin >> max;
		
		int nbr = findRecycle(min, max);
		cout << "Case #" << (i+1) << ": " << nbr << endl;
	}
	
	return 0;
}



