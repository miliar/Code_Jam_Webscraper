/*
 * Google Code Jam template :-)
 */

#include <iostream>
#include <string>
//#include <sstream>
//#include <algorithm>
#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
#include <map>

using namespace std;

typedef unsigned idx;
typedef unsigned num;

class Node
{
    public:
	string name;
	map<string,Node> cld;
	Node(){}
	Node(const char *p):name(p){}
	bool contains(const string & what)
	{
	    return ! (cld.find(what)==cld.end());
	}
};


int insert(const string & path, Node *p)
    //warning -- path mus have the last / added
{
    size_t last=0,i;
    string temp;
    int tot=0;

    i=path.find('/',last+1);
    while (i!=string::npos)
    {
	temp = path.substr(last+1,i-last-1);

	if(! (p->contains(temp)))
	{
	    ++tot;
	    p->cld[temp] = Node(temp.c_str());
	}
	p = &(p->cld[temp]);

	last = i;
	i = path.find('/',last+1);
    }
    return tot;
}

void solve(const num t)
{
    Node root("");
    num M, N;
    num i;
    int tot=0;
    string line;

    cin >> N >> M;
    for(i=0; i<N; ++i)
    {
	cin >> line;
	line += '/';
	(void) insert(line,&root);
    }
    for(i=0; i<M; ++i)
    {
	cin >> line;
	line += '/';
	tot += insert(line,&root);
    }
    cout << "Case #" << t << ": " << tot << endl;
}

int main(void)
{
    num T;

    cin >> T;
    for(num t=1; t<=T; ++t) solve(t);

    return 0;
}
