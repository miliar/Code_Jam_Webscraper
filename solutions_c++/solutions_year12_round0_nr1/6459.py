#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <sstream>
#include <math.h>
#include <stdlib.h>
using namespace std;
typedef long long ll;
int main()
{
	int t;
	string g;
	getline(cin,g);
	stringstream(g) >> t;
	map <int,char> chan;
	chan.insert(make_pair(97,'y'));
	chan.insert(make_pair(98,'h'));
	chan.insert(make_pair(99,'e'));
	chan.insert(make_pair(100,'s'));
	chan.insert(make_pair(101,'o'));
	chan.insert(make_pair(102,'c'));
	chan.insert(make_pair(103,'v'));
	chan.insert(make_pair(104,'x'));
	chan.insert(make_pair(105,'d'));
	chan.insert(make_pair(106,'u'));
	chan.insert(make_pair(107,'i'));
	chan.insert(make_pair(108,'g'));
	chan.insert(make_pair(109,'l'));
	chan.insert(make_pair(110,'b'));
	chan.insert(make_pair(111,'k'));
	chan.insert(make_pair(112,'r'));
	chan.insert(make_pair(113,'z'));
	chan.insert(make_pair(114,'t'));
	chan.insert(make_pair(115,'n'));
	chan.insert(make_pair(116,'w'));
	chan.insert(make_pair(117,'j'));
	chan.insert(make_pair(118,'p'));
	chan.insert(make_pair(119,'f'));
	chan.insert(make_pair(120,'m'));
	chan.insert(make_pair(121,'a'));
	chan.insert(make_pair(122,'q'));
	chan.insert(make_pair(32,' '));
	  int ab=1;
	
	while(t--)
	{
	  string s="";
	  getline (cin,s);
	  string ans="";
	  for(int i=0;i<s.length();i++)
	  {
	    int a=s.at(i);
	    ans+= chan.find(a)->second;
	  }
	  cout<<"Case #"<<ab<<": "<<ans<<endl;
	  ab++;

	}
	return 0;
}
	
