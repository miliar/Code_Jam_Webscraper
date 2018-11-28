#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;


int main()
{
fstream In("b-large.in", ios::in);
fstream Out("b-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{

vector<string> transform, destroy;
string s;

int N;
In >> N;

for(int i=0; i<N; i++)
{	In >> s;
	transform.push_back(s);
}
In >> N;

for(int i=0; i<N; i++)
{	In >> s;
	destroy.push_back(s);
}

In >> N >> s;
string cur = "";
for(int i=0; i<N; i++)
{
	char c = s[i];
	
	if(cur=="")
		cur += c;
	else
	{
		char prev = cur[cur.size()-1];
		int j;
		for(j=0; j<transform.size(); j++)
			if(transform[j][0]==c && transform[j][1] == prev) break;
			else if(transform[j][1] == c && transform[j][0] == prev) break;
		if(j < transform.size() )
			cur = cur.substr(0, cur.size()-1) + transform[j][2];
		else
			cur += c;
	}

	for(int j=0; j<cur.size(); j++)
	for(int k=j+1; k<cur.size(); k++)
	for(int l=0; l<destroy.size(); l++)
		if(destroy[l][0]==cur[j] && destroy[l][1]==cur[k]) cur = "";
		else if(destroy[l][1]==cur[j] && destroy[l][0]==cur[k]) cur = "";
	//cout << cur << endl;
}
//cout << endl;

Out << "Case #" << h+1 << ": " << "[";
for(int i=0; i<cur.size(); i++) Out << (i==0 ? "" : ", " ) << cur[i] ;

Out << "]" << endl;


}

In.close();

Out.close();

return 0;

}
 
