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

//REMEMBER NOT TO USE THESE names as variable names
#define vi vector<int>
#define vs vector<string>
#define vii vector<vector<int> >

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

int main()
{	
	DBG(cout<<"DEBUGGING IS ON!!!"<<endl;)
	
	//Start Code here
	
	int t;
	cin >> t;
	
	FOR(i,t)
	{
		char s[23];
		cin >> s;
		
		//FOR(j,strlen(s))
			//s[0] -= '0';
			
		//reverse(s, s+strlen(s));
			
		// FORS(j, 1,strlen(s))
		// {
			// if(s[j] < s[j-1])
			// {
				// cur = s[j];
				// iter_swap(s+j, find_if(s,
			// }
		// }
		
		// bool next = false;
		
		// FOR(j ,strlen(s) - 1)
		// {
			// if(s[j] < s[j+1])
			// {
				// next = true;
				// break;
			// }
		// }
		
		if(next_permutation(s,s+strlen(s)) == false)
		{
			prev_permutation(s,s+strlen(s));
			char tmp[24];
			sprintf(tmp,"0%s",s);
			strcpy(s,tmp);
			
			while(s[0] == '0')
				next_permutation(s,s+strlen(s));
		}
			
		
		cout << "Case #" << i+1 << ": " << s << endl;
	
	}
	
}