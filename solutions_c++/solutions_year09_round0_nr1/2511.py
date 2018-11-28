#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <set>
using namespace std;

typedef pair<int,string> PIS;
vector<string> slov;
bool prov(string word)
{
	int len=slov.size();
	for (int i=0;i<len;i++)
	{
		if (slov[i].find(word)==0)
			return true;
	}
	return false;
}

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int l,d,n;
	cin >> l >> d >> n;
	
	slov.resize(d);
	for (int i=0;i<d;i++)
	{		
		cin >> slov[i];
	}
	for (int i=0;i<n;i++)
	{
		queue<PIS> tt;
		string k;
		cin >> k;
		int j=0;
		tt.push(make_pair(0,k));
		int result=0;
		set<string> ans;
		while (!tt.empty())
		{
			int pos=tt.front().first;
			k=tt.front().second;
			j=pos;
			tt.pop();
			if (pos==l)
			{
				ans.insert(k);
				continue;
			}
			if (k[j]=='(')
			{
				string tmp;
				j++;
				while (k[j]!=')')
				{
					tmp+=k[j];
					j++;
				}
				j++;
				k.erase(pos,tmp.length()+2);
				for (int g=0;g<tmp.length();g++)
				{
					string kk=k;
					string tm;
					tm=tm+tmp[g];
					kk.insert(pos,tm);
					tm.clear();
					for (int gg=0;gg<=pos;gg++)
					{
						tm+=kk[gg];
					}
					if (prov(tm))
						tt.push(make_pair(pos+1,kk));
				}
			}else
			{
				string tm;
				for (int gg=0;gg<pos;gg++)
					{
						tm+=k[gg];
					}
				if (prov(tm))
					tt.push(make_pair(pos+1,k));
			}
		}		
		cout << "Case #" << i+1 <<": "<<ans.size()<<endl;
	}
	return 0;
}