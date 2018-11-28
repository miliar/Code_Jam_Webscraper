#include<iostream>
#include<map>
#include<limits>
#include<vector>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

const UL inv=numeric_limits<UL>::max();

int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL S;
		cin>>S;
		{string z; getline(cin, z);}
		typedef map<string, UL> eng_t;
		eng_t eng;
		for(UL i=0; i<S; ++i)
		{
			string tmp;
			getline(cin, tmp);
			eng[tmp]=i;
		}
		UL Q;
		cin>>Q;
		{string z; getline(cin, z);}
		if(Q==0 || Q==1)
		{
			cout<<"Case #"<<tt<<": 0\n";
			if(Q==1)
				{string z; getline(cin, z);}
			continue;
		}
		vector<UL> cur(S), prev(S);
		string p;
		getline(cin, p);
		fill(cur.begin(), cur.end(), 0);
		eng_t::iterator it=eng.find(p);
		if(it != eng.end())
			cur[it->second]=inv;
		for(UL i=1; i<Q; ++i)
		{
			swap(cur, prev);
			getline(cin,p);
			for(UL j=0; j<S; ++j)
			{
				cur[j]=inv;
				for(UL k=0; k<S; ++k)
					if(prev[k]!=inv)
						cur[j]=min(cur[j], prev[k] + (j==k?0:1));
			}
			eng_t::iterator it=eng.find(p);
			if(it != eng.end())
				cur[it->second]=inv;
		}
		cout<<"Case #"<<tt<<": "<<(*min_element(cur.begin(), cur.end()))<<'\n';
	}
}
