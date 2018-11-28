#include <iostream>
#include <cmath>
#include <vector>
#include <iterator>
#include <numeric>
#include <cstdio>
#include <string>
#include <algorithm>
#include <list>
#include <map>
#include <set>

template <class T>
T abs (T a)
{
    if (a<0)
        return -a;
    return a;
}

using namespace std;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int test,q=0;
	cin>>test;
	while(test--)
	{
		q++;
		string s,st="";
		int c,d,n;
		cin>>c;
		//map<int,char> change;
		vector< set<char> > erase('Z'-'A'+1);//, changing('Z'-'A'+1);
		vector<char> change('Z'*20+27, '*');
		//map <char,int> lable,lcopy;
		set<char> lable;
		for (int i=0;i<c;++i)
		{
			cin>>s;
			change[(int)s[0]*10+s[1]]=s[2];
			change[(int)s[1]*10+s[0]]=s[2];
		}
		cin>>d;
		for (int i=0;i<d;++i)
		{
			cin>>s;
			erase[s[0]-'A'].insert(s[1]);
			erase[s[1]-'A'].insert(s[0]);
		}
		cin>>n;
		cin>>s;
		bool cont=true;
		while (cont)
		{
			cont=false;
			lable.clear();
			for (int i=0;i<s.size();++i)
			{
				if (st.empty())
				{
					if (i!=s.size()-1)
						if (change[(int)s[i]*10+s[i+1]]!='*')
						{
							st+=change[s[i]*10+s[i+1]],i++;
							continue;
						}
						else
						{
							st+=s[i];
							if (!erase[s[i]-'A'].empty())
							{
								for (auto it=erase[s[i]-'A'].begin();it!=erase[s[i]-'A'].end();++it)
								{
									lable.insert(*it);
								}
							}
						}
					else
						st+=s[i];
				}
				else
				{
					if(change[(int)s[i]*10+st.back()]!='*')
						st.back()=change[(int)s[i]*10+st.back()];
					else if (lable.find(s[i])!=lable.end())
					{
						st.clear();
						lable.clear();
					}
					else 
					{
						if (i!=s.size()-1)
						
							if (change[(int)s[i]*10+s[i+1]]!='*')
							{
								st+=change[s[i]*10+s[i+1]],i++;
								continue;
							}
							else
								st+=s[i];
						else
							st+=s[i];
						if (!erase[s[i]-'A'].empty())
						{
							for (auto it=erase[s[i]-'A'].begin();it!=erase[s[i]-'A'].end();++it)
							{
								lable.insert(*it);
							}
						}
					}
				}
			}
			if (s!=st)
			{
				cont=true;
				s=st;
				st="";
			}
			if (s.empty())
				break;
		}
		if(s.empty())
			cout<<"Case #"<<q<<": []"<<endl;
		else
		{
			cout<<"Case #"<<q<<": [";
			copy(s.begin(),s.end()-1,ostream_iterator<char>(cout,", "));
			cout<<s.back()<<"]"<<endl;
		}
	}
	return 0;
}
