#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int N;
string welcome_to_code_jam("welcome to code jam");

bool used[500];
map<char,vector<int> > table;

int Add(int a,int b){return (a % 10000) + (b % 10000);}
int Mult(int a,int b){return (a % 10000) * (b % 10000);}

string needed(string s)
{
    string res;
    for(int i=0;i<s.size();++i)
    {
	if(welcome_to_code_jam.find(s[i])!=string::npos)
	    res += s[i];
    }
    return res;
}

void make_table(vector<pair<char,int> > d)
{
    for(int i=0;i<d.size();++i)
	table[d[i].first].push_back(i);
}

vector<pair<char,int> > grouping(string str)
{
    vector<pair<char,int> > group;
    group.push_back(make_pair(str[0],1));
    for(int i=1;i<str.size();++i)
    {
	if(str[i-1] == str[i])
	    ++group.back().second;
	else
	    group.push_back(make_pair(str[i],1));
    }
    return group;
}

vector<pair<char,int> > del(vector<pair<char,int> > g)
{
    vector<pair<char,int> > pairs;
    for(int i=0;i<g.size();++i)
    {
	if(welcome_to_code_jam.find(g[i].first) != string::npos)
	{
	    pairs.push_back(g[i]);
	}
    }
    return pairs;
}

int calc(vector<pair<char,int> > pairs,int pos,int last)
{
    int res = 0;
    if(pos == welcome_to_code_jam.size())return 1;

    for(int i=0;i<table[welcome_to_code_jam[pos]].size();++i)
    {
	int idx = table[welcome_to_code_jam[pos]][i];
	if(last <= idx && used[idx]==false)
	{
	    used[idx] = true;
	    int r = calc(pairs,pos+1,idx+1);
	    int mul = Mult(pairs[idx].second,r);
	    res = Add(res,mul);
	    used[idx] = false;
	}
    }
    return res;
}

int main()
{
    string str;
    cin >> N;
    getline(cin,str);
    for(int i=0;i<N;++i)
    {
	table.clear();
	for(int j=0;j<500;++j)used[j]=false;

	getline(cin,str);

	string needed_str = needed(str);

	vector<pair<char,int> > g = grouping(str);

	vector<pair<char,int> > d = del(g);
	make_table(d);

	int v = calc(d,0,0);
	printf("Case #%d: %04d \n",i+1,v);
    }
}
