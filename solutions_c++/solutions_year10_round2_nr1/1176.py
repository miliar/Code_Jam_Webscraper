// cc.cpp : Defines the entry point for the console application.
//

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

typedef vector<int> vi;

void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}

class node;
typedef map<std::string, node> chld;
typedef map<std::string, node>::iterator cit;
class node
{
public:
    node(){}
    node(string s) { val=s;}
    std::string val;

    chld chl;
};

int BuildTree(vector<std::string> &ms, vector<std::string> &ns, int N, int M)
{
    node no("/");

    // construct tree
    for(int i=0;i<ns.size();++i)
    {
	node *cur = &no;
	vector<string> tok;
	Tokenize(ns[i], tok, "/");
	for(int t=0;t<tok.size();++t)
	{
	    cit itr = cur->chl.find(tok[t]);
	    if (itr == cur->chl.end())
	    {
//		printf("C %s ", tok[t].c_str());
		// createnode
		cur->chl.insert( make_pair(tok[t], node(tok[t])) );
		cur = &cur->chl[ tok[t] ];
	    }
	    else
	    {
//		printf("G %s ", tok[t].c_str());
		cur = &itr->second;
	    }
	}
	//cout<<endl;
    }

    int res =0;
    for(int i=0;i<ms.size();++i)
    {
	node *cur = &no;
	vector<string> tok;
	Tokenize(ms[i], tok, "/");
//	printf("tokens: %s %d\n", ms[i].c_str(), tok.size());
	for(int t=0;t<tok.size();++t)
	{
	    cit itr = cur->chl.find(tok[t]);
	    if (itr == cur->chl.end())
	    {
		// createnode
//		printf("N %s ", tok[t].c_str());
		cur->chl.insert( make_pair(tok[t], node(tok[t])) );
		cur = &cur->chl[ tok[t] ];
		res++;
	    }
	    else
	    {
//		printf("G %s ", tok[t].c_str());
		cur = &itr->second;
	    }
	}
	//cout<<endl;
    }
    return res;
}
int main(int argc, char* argv[])
{
	int t=0;
	scanf("%d", &t);
	for(int i=0; i<t; ++i) // for each testcase
	{
	    vector<std::string> ms, ns;
	  int N=0; int M=0;
	  scanf("%d %d", &N, &M);
	  for(int n=0;n<N;++n)
	  {
	      char str[100]={0};
	      scanf("%s", str);
	      ns.push_back(str);
	  }

	  for(int m=0;m<M;++m)
	  {
	      char str[100]={0};
	      scanf("%s", str);
	      ms.push_back(str);
	  }
	  
	  int ret = BuildTree(ms,ns,N,M);
	  printf("Case #%d: %d\n", i+1, ret);
	}
	return 0;
}

