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

bool check(string s, int n)
{
	for(int i = n+1 ; i< s.size() ;i++)
		if(s[i] == '1') 
			return false; 
	return true; 
}

int main()
{
	int N ; 
	cin>>N ; 

	for(int t = 1 ; t <= N ; t++)
	{				
		int ret = 0 ; 
		int k ; cin>> k ; 

		vector<string> s(k) ; 
		for(int i = 0 ;i < k ; i++)
			cin>>s[i]; 

		for(int i = 0 ; i < k ; i++)
		{
			int index = i ; 
			for(; !check(s[index] , i) ; index++ )
			{
			}

			for(int j = index ; j >= i+1 ; j--)
			{
				swap(s[j],s[j-1]) ; 
				ret++  ; 
			}

		}

		printf("Case #%d: %d\r\n", t,ret ) ; 
	}

	return 0 ;
}