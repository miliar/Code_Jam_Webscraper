#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstdlib>
#include <string>
using namespace std;

bool check(vector<string> s , int k,char c)
{
	int sz = s.size() ; 

	for(int i = 0 ; i < sz ; i++)
	{
		for(int j = 0 ; j < sz ; j++)
		{
			if(s[i][j] == c)
			{
				// right
				if(j + k < sz)
				{
					bool ok = true ; 
					for(int t = j ;t <= j+k ; t++)
					{
						if(s[i][t] != c)
						{
							ok = false ; 
							break ; 
						}
					}
					if(ok) return true ; 
				}

				// down
				if(i + k < sz)
				{
					bool ok = true ; 
					for(int t = i ; t<= i+k ;t++)
					{
						if(s[t][j] != c)
						{
							ok = false ; 
							break ; 
						}
					}
					if(ok) return true ; 
				}

				// left dig
				if( j - k >=0 && i + k < sz)
				{
					bool ok = true ;
					for(int t = 0 ; t <= k ; t++)
					{
						if(s[i+t][j-t] != c)
						{
							ok = false ; 
							break ; 
						}
					}
					if(ok) return true ; 
				}

				// right dig
				if( j + k <sz && i + k < sz)
				{
					bool ok = true ;
					for(int t = 0 ; t <= k ; t++)
					{
						if(s[i+t][j+t] != c)
						{
							ok = false ; 
							break ; 
						}
					}
					if(ok) return true ; 
				}
			}
		}
	}

	return false ; 
}

int main()
{
	int N ; 
	cin>> N ; 

	for(int cc = 1 ; cc <= N ; cc++)
	{
		int n , k ; 
		cin>> n >> k ; 

		vector<string> d ; 
		for(int i = 0 ;i < n ; i++)
		{
			string s ; 
			cin>> s ; 
			d.push_back(s) ; 
		}

		vector<string> ret;
		for(int i = 0 ; i < n ; i++)
		{
			string s ; 
			for(int j = n-1 ; j >=0 ; j--)
			{
				s += d[j][i] ; 
			}
			ret.push_back(s) ; 
			//cout<<s<<endl ; 
		}
		//cout<<endl; 
		for(int t = 0 ; t < n ; t++)
		{
			for(int i = n-1 ; i > 0 ; i--)
			{
				for(int j = 0 ; j < n ; j++)
				{
					if(ret[i][j] == '.')
					{
						ret[i][j] = ret[i-1][j] ; 
						ret[i-1][j] = '.' ; 
					}
				}
			}
		}

		/*
		for(int i = 0 ;i < n ; i++)
			cout<<ret[i]<<endl; 
			*/

		bool ba = check(ret,k-1,'R') ; 
		bool bb = check(ret,k-1,'B') ; 

		string s; 
		if(ba && bb)
			s = "Both"; 
		else if(ba && !bb)
			s = "Red";
		else if(!ba && bb)
			s = "Blue";
		else
			s = "Neither" ; 

		cout<<"Case #"<<cc<<": "<<s<<endl ; 
	}
	return 0 ; 
}