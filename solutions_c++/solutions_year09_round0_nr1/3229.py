#include <iostream>
#include <vector>
#include <string>
using namespace std;

int L,D,N;
vector<string> dict;

vector<string> make_vecpat(string pat)
{
    int idx=0;
    int str_pos = 0;
    vector<string> vec_pat;

    for(;str_pos<pat.size();++idx,++str_pos)
    {
	vec_pat.push_back(string());
	if(pat[str_pos]=='(')
	{
	    for(++str_pos;pat[str_pos]!=')';++str_pos)
	    {
		vec_pat[idx] += pat.substr(str_pos,1);
	    }
	}
	else
	{
	    vec_pat[idx] = pat.substr(str_pos,1);
	}
    }

    assert(vec_pat.size()==L);
    return vec_pat;
}

bool is_have(string str)
{
    for(int i=0;i<dict.size();++i)
    {
	if(dict[i].find(str)==0)return true;
	if(str < dict[i])
	{
	    return false;
	}
    }
    return false;
}

int expand(vector<string> vec_pat,int cur,string accum)
{
    if(cur==L)
    {
	if(is_have(accum))
	    return 1;
	else
	    return 0;
    }
    else
    {
	int count = 0;
	for(int i=0;i<vec_pat[cur].size();++i)
	{
	    string next = accum + vec_pat[cur][i];
	    bool check = is_have(next);
	    if(check == false)
		continue;
	    count += expand(vec_pat,cur+1,next);
	}
	return count;
    }
}

int main()
{
    cin >> L >> D >> N;
    for(int i=0;i<D;++i)
    {
	string tmp;
	cin >> tmp;
	dict.push_back(tmp);
    }
    sort(dict.begin(),dict.end());

    for(int i=0;i<N;++i)
    {
	string pat;
	cin >> pat;

	vector<string> vec_pat = make_vecpat(pat);
	
	int result = expand(vec_pat,0,"");
	cout << "Case #" << (i+1) << ": " << result << endl;
    }
}
