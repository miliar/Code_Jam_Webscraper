#include <iostream>
#include <cstdio>
#include <map>
#include <utility>
#include <string>
#include <vector>

using namespace std;

multimap<char, char> opp;
multimap<char, char>::iterator oit, oit2;
pair<multimap<char, char>::iterator, multimap<char, char>::iterator> poit;
multimap<char, pair<char, char> > comb;
multimap<char, pair<char, char> >::iterator cit, cit2;
pair< multimap<char, pair<char, char> >::iterator, multimap<char, pair<char, char> >::iterator> pcit;

vector<char> list;

int main()
{
	//ios_base::sync_with_stdio(0);

	int t, n, c, d;
	pair<char, char> p;
	char z;
	string s;
	bool combined, opposite;
	scanf("%d", &t);

	for(int i=1;i<=t;i++)
	{
		list.clear();
		opp.clear();
		comb.clear();
		
		cin>>c;
		//cout<<"c == "<<c<<endl;	
		
		for(int j=0;j<c;j++)
		{
			cin>>s;
			//cout<<"Dodaje "<<s<<endl;
			p = make_pair(s[1], s[2]);
			comb.insert(pair<char, pair<char, char> > (s[0], p));
			p = make_pair(s[0], s[2]);
			comb.insert(pair<char, pair<char, char> > (s[1], p));
		}

		cin>>d;

		for(int j=0;j<d;j++)
		{
			cin>>s;
			//cout<<"Dodaje "<<s<<endl;
			opp.insert(pair<char, char> (s[0], s[1]));
			opp.insert(pair<char, char> (s[1], s[0]));
		}
		
		cin>>c;
		/*
		cout << "opp contains:\n";
		for (oit = opp.begin(); oit != opp.end(); ++oit)
		{
			cout << oit->first << " =>";
			poit = opp.equal_range(oit->first);
			for (oit2 = poit.first; oit2 != poit.second; ++oit)
				cout << " " << oit->second;
			cout << endl;
		}
		*/
		scanf("%c", &z);
		for(int j=0;j<c;j++)
		{
			scanf("%c", &z);
			
			//printf("aktualny znak: %c\n", z);

			combined = false;
			opposite = false;
			
			if(list.size() > 0)
			{
				//printf("komibinacje...\n");
				//comb
				pcit = comb.equal_range(list[list.size()-1]);
				for(cit = pcit.first; cit != pcit.second; ++cit)
				{
					//printf("cit = (%c, (%c, %c))\n", cit->first, (*cit).second.first, (*cit).second.second);
					if((*cit).second.first == z)
					{
						//printf("pasi\n");
						combined = true;
						list[list.size()-1] = (*cit).second.second;
						break;
					}
				}
			}	
			
			if(!combined)
			{
				poit = opp.equal_range(z);
				for(oit = poit.first; oit != poit.second; ++oit)
				{
					for(int k=0;k<list.size();k++)
					{
						if(list[k] == oit->second)
						{
							opposite = true;
							list.clear();
							break;
						}
			
					}
					if(opposite)
						break;

				}
			}


			if(!combined && !opposite)
				list.push_back(z);
		}

		cout<<"Case #"<<i<<": [";
		for(int j=0;j<list.size();j++)
		{
			cout<<list[j];
			if(j+1 < list.size())
				cout<<", ";
		}
		cout<<"]"<<endl;
	}
	


}
