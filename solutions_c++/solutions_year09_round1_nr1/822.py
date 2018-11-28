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

int D[11][10000000] ;


int go(int num, int b)
{
	if(num > 10000000)
		cout<<"aaaaaaaaaaaa";
	if(D[b][num] != 0)
		return D[b][num] ; 

	D[b][num] = -1 ; 

	int temp = num ; 
	int sum = 0 ; 
	while(temp)
	{
		int r = temp%b ; 
		sum += (r*r) ; 
		temp/=b ; 
	}

	if(sum == 1)
		return D[b][num] = 1 ; 
	else
		return D[b][num] = go(sum, b) ; 
}

int main()
{
	int N ; 
	cin>>N ; 
	char c ; 
	cin.get(c) ; 

	memset(D,0,sizeof(D)) ; 

	for(int n = 1 ; n <= N ; n++)
	{
		string base; 
		getline(cin, base) ; 

		stringstream iss;
		iss<<base; 
		int temp;
		vector<int> num; 
		while(iss>> temp)
		{
			num.push_back(temp) ; 
		}

		for(int i = 2 ; ; i++)
		{
			for(int j = 0 ; j < num.size() ; j++)
				go(i, num[j]); 
			
			bool ok = true; 
			for(int j = 0 ; j < num.size() ; j++)
				if(D[num[j]][i] != 1)
					ok = false; 
			if(ok == true)
			{
				printf("Case #%d: %d\r\n", n, i) ; 
				break ; 
			}

		}
	}

	return 0 ;
}