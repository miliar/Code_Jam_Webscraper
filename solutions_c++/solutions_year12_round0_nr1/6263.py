#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std;
class hoo
{
public:
string transform(string arg)
{
	string ret;
	for(int i=0;i<arg.length();i++)
	{
	if(arg.compare(i,1," ") == 0)
		ret.push_back(' ');
	else if(arg.compare(i,1,"a") == 0)
		ret.push_back('y');
	else if(arg.compare(i,1,"b") == 0)
                ret.push_back('h');
	else if(arg.compare(i,1,"c") == 0)
                ret.push_back('e');
	else if(arg.compare(i,1,"d") == 0)
                ret.push_back('s');
	else if(arg.compare(i,1,"e") == 0)
                ret.push_back('o');
 	else if(arg.compare(i,1,"f") == 0)
                ret.push_back('c');
 	else if(arg.compare(i,1,"g") == 0)
                ret.push_back('v');
 	else if(arg.compare(i,1,"h") == 0)
                ret.push_back('x');
 	else if(arg.compare(i,1,"i") == 0)
                ret.push_back('d');
 	else if(arg.compare(i,1,"j") == 0)
                ret.push_back('u');
 	else if(arg.compare(i,1,"k")== 0)
                ret.push_back('i');
 	else if(arg.compare(i,1,"l") == 0)
                ret.push_back('g');
 	else if(arg.compare(i,1,"m") == 0)
                ret.push_back('l');
 	else if(arg.compare(i,1,"n") == 0)
                ret.push_back('b');
 	else if(arg.compare(i,1,"o") == 0)
                ret.push_back('k');
 	else if(arg.compare(i,1,"p") == 0)
                ret.push_back('r');
 	else if(arg.compare(i,1,"q") == 0)
                ret.push_back('z');
 	else if(arg.compare(i,1,"r") == 0)
                ret.push_back('t');
 	else if(arg.compare(i,1,"s") == 0)
                ret.push_back('n');
 	else if(arg.compare(i,1,"t") == 0)
                ret.push_back('w');
 	else if(arg.compare(i,1,"u") == 0)
                ret.push_back('j');
 	else if(arg.compare(i,1,"v") == 0)
                ret.push_back('p');
	else if(arg.compare(i,1,"w") == 0)
                ret.push_back('f');
	else if(arg.compare(i,1,"x") == 0)
                ret.push_back('m');
 	else if(arg.compare(i,1,"y") == 0)
                ret.push_back('a');
 	else if(arg.compare(i,1,"z") == 0)
                ret.push_back('q');
	} 	
	return ret;
}
};	
int main()
{
	hoo ob;
	int T,i;
	string G;
	cin>>T;	
	getchar();	
	i=T;
	int j=1;	
	do
	{
	getline(cin,G);
	cout<<"Case #"<<j<<": "<<ob.transform(G)<<endl;	
	i--;
	j++;
	}while(i>0);
	return 0;
}
