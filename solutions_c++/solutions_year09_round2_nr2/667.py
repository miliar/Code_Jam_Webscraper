#include<iostream> 
#include<cmath> 
#include<vector> 
#include<algorithm> 
#include<cstdio> 
#include<cstdlib> 
#include<string> 
#include<sstream> 
#include<map> 
#include<queue> 
#include<set> 
#define vi vector<int> 
#define vs vector<string> 

#define REP(i,n) for(int i=0;i<(int) n;i++) 
#define LL long long 
#define INF (2<<29) 

using namespace std;

string str;
int main()
{
	
	int kases;
	cin >> kases;
	
	for(int kase = 1; kase <=kases; ++kase)
	{
		cin >> str;
		string old_str = str;
		if(!next_permutation(str.begin(), str.end()))
		{
			str = old_str;
			string temp;
			int zeros = 1;
			REP(i, str.size())
			{
				if(str[i] == '0') ++zeros;
				else temp+=str[i];
			}
			
			sort(temp.begin(), temp.end());
			str = temp[0];
			REP(i,zeros) str += "0";
			if(temp.size() >= 2)
			{
				str += temp.substr(1);
			}
			cout << "Case #" << kase << ": " << str << endl;
		}
		else
		{
			cout << "Case #" << kase << ": " << str << endl;
		}
		
		
	}
}
