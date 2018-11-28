#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <algorithm>
#include <utility>
#include <map>

//REMEMBER NOT TO USE THESE names as variable names
#define vi vector<int>
#define vs vector<string>
#define vii vector<vector<int> >
#define ll long long

#define dbg false	//Debugging usage
#define DBG(x) if(dbg) {x}

#define FOR(x,y) for(int x=0; x<(y); ++x)
#define FORS(x,z,y) for(int x=z; x<(y); ++x)
#define FORI(x,y,z) for(int x=0; x<(y); x+=(z))
#define FORSI(x,z,y,w) for(int x=z; x<(y); x+=(w))
#define DFOR(x,y,z,w) for(int x=0; x<(y); ++x) for(int z=0; z<(w); ++z)
#define TFOR(x,y,z,w,u,v) for(int x=0; x<(y); ++x) for(int z=0; z<(w); ++z) for(int u=0; u<(v); ++u)

#define FORC(c,type,itt) for(c<type>::iterator itt = c.begin(); itt != c.end(); ++itt)



using namespace std;

//Global Variables below (make all the required variables global)
int cur;


// bool swappable(char i)
// {
	// return (i>cur);
// }

ll power(int a, int b)
{
	if(b==0)
		return 1;

	ll ans=a;
	
	FOR(i,b-1)
		ans *=a;
		
	return ans;
}

int main()
{	
	DBG(cout<<"DEBUGGING IS ON!!!"<<endl;)
	
	//Start Code here
	
	int t;
	cin >> t;
	
	FOR(i,t)
	{
		ll ans=0;
		
		string s;
		cin >> s;
		int max=1;
		
		bool zeroused = false;
		
		map<char,int> m;
		
		FOR(j,s.length())
		{
			if(m.find(s[j]) == m.end())
			{
				if(!zeroused && max==2)
				{
					m[s[j]] = 0;
					zeroused = true;
				}
				else
				{
					m[s[j]]=max;
					max++;				
				}
				
			}
		}
		
		//for(map<char,int>::iterator it = m.begin(); it != m.end(); it++)
			//cout<<it->first << " " << it -> second << endl;
		
		//cout << ans <<endl;
		
		FOR(j,s.length())
		{
			ans += m[s[j]] * power(max, s.length() - (j+1));
		}
		
		cout << "Case #" << i+1 << ": " << ans << endl;
	
	}
	
}