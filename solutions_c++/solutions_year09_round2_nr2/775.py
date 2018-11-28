#include <algorithm> 
#include <string> 
#include <vector> 
#include <cmath> 
#include <sstream> 
#include <iostream> 
#include <cstdio> 
#include <set> 
#include <map> 
#include <utility> 
#include <cstdlib> 
#include <locale> 
#include <bitset> 
#include <numeric> 
using namespace std; 

#define all(x) (x).begin(),(x).end() 
#define rall(x) (x).rbegin(),(x).rend() 
#define clear(x,v) memset((x),v,(x).size()) 
#define pb push_back 

#define UNI(x) do{ sort(all(x)) ; (x).erase(unique(all(x)),(x).end()); } while(0) 

typedef stringstream ss; 
typedef vector<int> vi ;  
typedef vector<string> vs ;

int main()
{
	int N ; 
	cin>>N ; 

	for(int n = 1 ; n <= N ; n++)
	{
		string s ;
		cin >> s ;

		if(!next_permutation(all(s)))
		{
			if(s[0] == '0')
			{
				for(int i = 1 ; i < s.size() ; i++)
				{
					if(s[i] != '0')
					{
						swap(s[0],s[i]) ; 
						break ; 
					}
				}
			}
			s.insert(1,"0") ; 
		}

		printf("Case #%d: %s\r\n", n, s.c_str()) ; 
	}

	return 0 ;
}