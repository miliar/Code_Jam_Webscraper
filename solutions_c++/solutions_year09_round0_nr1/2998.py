#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cctype>
#include <climits>

#define GI ({int t;scanf("%d",&t);t;})
#define dpkg(x) cout<< #x <<" --> " << x << endl ;
#define INF (int)1e9+1
#define PB push_back
#define MP make_pair
#define FF first
#define SS second
#define SZ size()
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i < (b);++i)
#define FORD(i,a,b) for(LET(i,a);i > (b);i--)
#define all(v) (v).begin() , (v).end()
//typedef pair <int, int>  PII;
//typedef vector <int> VI;
typedef unsigned long long LL; 
 
using namespace std;

string fun3(int &n,string str)
{
	string s = "";
	int i;
	for( i = n ; i < (int)str.length() ; i++)
	{
		if(str[i] == ')') break ;
		
		   s = s + str[i];
	}
	n = i+1;
	return s;
}

void fun1(string str,vector<string> &vs)
{
	for(int i = 0 ; i < (int)str.length() ; )
	{
		if(str[i] == '(' && str[i] != ')')
		{
			i++;
			vs.push_back( fun3( i, str ) );
		}
		 
		else
		{
			string a = "";
			a = a + str[i];
		   vs.push_back( a );
		   i++;
	     }
	}
}

int fun2(char a,string str)
{
	if ( find( all(str) ,a ) != str.end() )
	    return 1;
	else	
		return 0;
}

int main()
{
	/*
	string str;
	vector<string> v;
	cin >> str;
	fun1(str,v);
	FOR(i,0,(int)v.size())
	   cout<<v[i]<<" ";
	*/
	
	
	int l,d,n;
	
	l = GI;
	d = GI;
	n = GI;
	
	string str1[d];
	string str2[n];
		
	FOR(i,0,d)	
	   cin>>str1[i];
	   
	FOR(i,0,n)	
	   cin>>str2[i];
	
	FOR(i,0,n)
	{
		string astr = str2[i] ;
		vector<string> vs;
	
		fun1(astr,vs);
		    
	     //FOR(i,0,(int)v.size()) 
	     //cout<<v[i]<<" ";
	    
		int count = 0 ;
				
		FOR(j,0,d)
		{
			string xstr = str1[j];
			
			int flag = 1;  
	
			for(int i = 0 ; i < (int)xstr.length() ; i++ )
			{
				if( fun2(xstr[i],vs[i]) == 0)
				{
					flag = 0;
					break;
				}
			}
			
			if(flag) count++;
		}
		
		printf("Case #%d: %d\n",i+1,count);
	} 	
	return 0;
}
