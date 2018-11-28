#include <deque>
#include <map>
#include <iostream>
#include <string>
#include <cassert>
using namespace std;

map<char,int> count;
map<pair<char,char>,char> rewrite;
deque<pair<char,char> > oppose_pair;
string input;

void read_input()
{
    {
	input = "";
	count.clear();
	rewrite.clear();
	oppose_pair.clear();
    }
    int n;
    cin >> n;
    for(int i=0;i<n;++i)
    {
	char c1,c2,t;
	cin >> c1 >> c2 >> t;
	rewrite[make_pair(c1,c2)] = t;
    }
    cin >> n;
    for(int i=0;i<n;++i)
    {
	char c1,c2;
	cin >> c1 >> c2;
	oppose_pair.push_back(make_pair(c1,c2));
    }
    cin >> n;
    for(int i=0;i<n;++i)
    {
	char c;cin >> c;
	input.push_back(c);
    }
}

pair<bool,char> rewritable(char c1,char c2)
{
    if(rewrite[make_pair(c1,c2)] != 0)
	return make_pair(true,rewrite[make_pair(c1,c2)]);
    else if(rewrite[make_pair(c2,c1)] != 0)
	return make_pair(true,rewrite[make_pair(c2,c1)]);
    else return make_pair(false,0);
}

bool is_opposed()
{
    for(size_t i=0;i<oppose_pair.size();++i)
    {
	pair<char,char> p = oppose_pair[i];
	if(count[p.first] && count[p.second])
	    return true;
    }
    return false;
}

void push_invoke(deque<char> &invoke,char c)
{
    invoke.push_front(c);
    ++count[c];
}

void pop_invoke(deque<char> &invoke)
{
    char c = invoke.front();
    invoke.pop_front();
    --count[c];
}

void solve(int case_num)
{
    deque<char> invoke;
    for(size_t i=0;i<input.size();++i)
    {
	char c = input[i];
	if(invoke.empty())
	    push_invoke(invoke,c);
	else
	{
	    char p = invoke.front();
	    pair<bool,char> r = rewritable(p,c);
	    if(r.first)
	    {
		pop_invoke(invoke);
		push_invoke(invoke,r.second);
	    }
	    else
	    {
		push_invoke(invoke,c);
		if(is_opposed())
		{
		    invoke.clear();
		    count.clear();
		}
	    }
	}
    }

    printf("Case #%d: [",case_num);
    if(!invoke.empty())
    {
	for(int i=invoke.size()-1;i>0;--i)
	    printf("%c, ",invoke[i]);
	printf("%c",invoke[0]);
    }
    puts("]");
}

int main()
{
    int n;cin >> n;
    for(int i=1;i<=n;++i)
    {
	read_input();
	solve(i);
    }
    return 0;
}
