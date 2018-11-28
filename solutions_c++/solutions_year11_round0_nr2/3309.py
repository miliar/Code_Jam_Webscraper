#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <string>

using namespace std;

map<string,char> combinationMap;
map<string,int> destroyMap;
string ele;
string out;

bool outchanged()
{
	if(out.size()<2)
		return false;
	char ch[3] = { out[out.size()-2], out[out.size()-1], 0};
	if(combinationMap.find(ch) != combinationMap.end())
	{
		out = out.substr(0, out.size()-1);
		out[out.size()-1] = combinationMap[ch];
		return true;
	}
	for(map<string,int>::iterator it = destroyMap.begin() ; it != destroyMap.end() ; ++it)
	{
		if(find(out.begin(),out.end(), (it->first)[0]) != out.end() &&
				find(out.begin(),out.end(), (it->first)[1]) != out.end())
		{
			out.clear();
			return true;
		}
	}
	return false;
}

void process()
{
	int C,D,sz;
	combinationMap.clear();destroyMap.clear();ele.clear();out.clear();
	cin>>C;
	for(int i=0;i<C;++i)
	{
		string tmp;
		cin>>tmp;
		string x = tmp.substr(0,2);
		combinationMap[x] = tmp[2];
		reverse(x.begin(), x.end());
		combinationMap[x] = tmp[2];
	}
	cin>>D;
	for(int i=0;i<D;++i)
	{
		string tmp;
		cin>>tmp;
		destroyMap[tmp]=1;
	}
	cin>>sz>>ele;
	string::iterator elementtobepushed=ele.begin();
	while(elementtobepushed != ele.end())
	{
		while(out.size()<2&&elementtobepushed!=ele.end())
		{
			out.push_back(*elementtobepushed);
			elementtobepushed++;
		}

		while(outchanged());
		if(elementtobepushed!=ele.end())
		{
			out.push_back(*elementtobepushed);
			elementtobepushed++;
		}
	}
	while(outchanged());
	if(out.size() > 0)
	{
		for(int x=0;x<out.size()-1;++x)
			cout<<out[x]<<", ";
		cout<<out[out.size()-1];
	}
}

int main()
{
	int tc;
	cin>>tc;
	for(int i=0;i<tc;++i)
	{
		cout<<"Case #"<<i+1<<": [";
		process();
		cout<<"]\n";
	}
	return 0;
}
