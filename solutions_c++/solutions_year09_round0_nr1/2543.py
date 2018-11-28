#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <deque>
#include <string>
using namespace std;
vector<string> pos;
void getAll(vector<string>& w,vector<vector<char> >& t,int L,string str="")
{
	if(str.size()==L)
	{
		pos.push_back(str);
		return;
	}
	for(int i=0;i<w.size();i++)
	{
		if(str==w[i].substr(0,str.size())||str.size()==0)
		{
			for(int i=0;i<t[str.size()].size();i++)
			{
				getAll(w,t,L,str+t[str.size()][i]);
			}
			return;
		}
	}
}
int main()
{
	int L,D,N;
//#ifndef LOCAL
	ifstream cin("A-small.in");
	ofstream cout("A-small.out");
//#endif
	cin>>L>>D>>N;
	vector<string> words(D);
	cin.get();
	for(int i=0;i<D;i++)
	{
		cin>>words[i];
	}
	sort(words.begin(),words.end());
	int cur=0;
	for(int i=1;i<=N;i++)
	{
		vector<vector<char> > test(L);
		for(int j=0;j<L;j++)
		{
			char c;
			cin>>c;
			if(c!='(')
			{
				test[j].push_back(c);
			}
			else
			{
				while(c!=')')
				{
					cin>>c;
					test[j].push_back(c);
				}
				test[j].pop_back();
			}
			sort(test[j].begin(),test[j].end());
		}
		int cnt=0;
		pos.clear();
		getAll(words,test,L);
		vector<string> temp(min(words.size(),words.size()));
		set_intersection(words.begin(),words.end(),pos.begin(),pos.end(),temp.begin());
		temp.erase(remove(temp.begin(),temp.end(),""),temp.end());
		cout<<"Case #"<<i<<": "<<temp.size()<<endl;
	}
	return 0;
}