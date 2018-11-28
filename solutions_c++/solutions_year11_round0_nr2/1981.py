#include<iostream>
#include<set>
#include<map>
#include<vector>
using namespace std;

int main()
{
	int T,C,D,N;
	cin >> T;
	char combiner[26][26];
	vector<set<char> > Destructor(26); 
	for(int i=0;i<T;++i)
	{
		vector<char> elemlist;
		for(int j=0;j<26;++j)
			for(int k=0;k<26;++k)
				combiner[j][k] = 0;
		for(int j=0;j<26;++j)
			Destructor[j].clear();

		cin >> C;
		for(int j=0;j<C;++j)
		{
			char b1,b2,r;
			cin >> b1; cin >> b2; cin >> r;
			combiner[b1-'A'][b2-'A'] = r;
			combiner[b2-'A'][b1-'A'] = r;
		}
		cin >> D;
		for(int j=0;j<D;++j)
		{
			char d1,d2;
			cin >> d1;  cin >> d2;
			Destructor[d1-'A'].insert(d2);
			Destructor[d2-'A'].insert(d1);
		}

		cin >> N;
		for(int j=0;j<N;++j)
		{
			char next;
			cin >>next;
			if(elemlist.size() >= 1 &&  combiner[next-'A'][elemlist[elemlist.size()-1]-'A'] != 0)
			{
				char last_ele = elemlist[elemlist.size()-1]; 
				elemlist.pop_back();
				elemlist.push_back(combiner[next-'A'][last_ele -'A']);

				continue;
			}
			vector<char>::iterator it1,it2;
			bool flag = false;
			for(it1 = elemlist.begin();it1!=elemlist.end();++it1)
			{
				if(!Destructor[next-'A'].empty() && Destructor[next-'A'].find(*it1)!=Destructor[next-'A'].end())
				{
					flag = true;
					break;
				}
			}
			if(flag)
			{
				elemlist.clear();
				continue;
			}
			elemlist.push_back(next);
		}
		int size = elemlist.size();
		cout << "Case #"<<i+1<<": [";
		for(int t=0;t<size;++t)
		{
			cout<<elemlist[t];
			if(t < size-1)
				cout<<", ";
		}
		cout<<"]\n";
	}
	return 0;
}
