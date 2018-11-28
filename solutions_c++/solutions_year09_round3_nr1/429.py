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

#define MAX 10000
class bigint
{
public:
	vector<int> num ; 

	bigint () { num.push_back(0); }

	void add(int n)
	{
		int carry =0 ; 
		for(int i = 0 ; i< num.size() ; i++)
		{
			num[i] += n + carry; 
			if(num[i] >= MAX)
			{
				carry = num[i]/MAX ; 
				num[i] = num[i]%MAX ; 
			}
			else
			{
				carry = 0 ; 
				break ; 
			}
		}
		if(carry>0)
			num.push_back(carry) ;
	}

	void multi(int n )
	{
		int carry =0 ; 
		for(int i = 0 ; i< num.size() ; i++)
		{
			num[i] *= n; 
			num[i] += carry ; 
			if(num[i] >= MAX)
			{
				carry = num[i]/MAX ; 
				num[i] = num[i]%MAX ; 
			}
			else
			{
				carry = 0 ; 
			}
		}
		if(carry>0)
			num.push_back(carry) ; 
	}

	string get()
	{
		string ret;  
		for(int i =  0 ;i < num.size() ; i++)
		{
			char t[5] ; 
			sprintf(t, "%04d", num[i]) ; 
			ret = t + ret ; 			
		}

		while(ret[0] == '0')
		{
			ret.erase(0,1); 
		}
		return ret ;
	}
};

int main()
{

	int N ; 
	cin>> N ; 

	for(int n = 1 ; n <= N ; n++)
	{
		string num  ; 
		cin>>num ; 

		map<char, int> m ; 
		for(int i = 0 ; i < num.size() ; i++)
		{
			m[num[i]] = -1 ; 				
		}

		m[num[0]] = 1 ;

		int base = m.size() ; 
		int index = 0 ; 
		for(int i = 1 ;i < num.size() ; i++)
		{
			if(m[num[i]] == -1)
			{
				if(index == 1) index++ ; 
				m[num[i]] = index ; 
				index++ ; 
			}
		}
		if(base == 1) base = 2; 
		bigint ret ; 
		for(int i = 0 ; i < num.size() ; i++)
		{
			ret.multi(base);
			ret.add((m[num[i]]));
		}
		string s = ret.get() ; 
		printf("Case #%d: %s\n", n,s.c_str()) ; 
	}
	return 0 ; 
}