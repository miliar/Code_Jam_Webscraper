#include<set>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;



map<pair<char,char>,char> comb;
set<pair<char,char>> oppo;
map<char, int> elements;

char bse[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("outl.txt","w",stdout);
	int t,c,d,n;
	bool expo;
	char c1,c2,res;
	string elementlist;
	cin >> t;
	for(int i = 0; i!= t; i++){
		comb.clear();
		oppo.clear();
		elements.clear();
		elementlist.clear();
		cin >> c;
		for(int j=0;j!=c;j++)
		{
			cin >> c1 >> c2 >> res;
			comb.insert(make_pair(make_pair(c1,c2),res));
			comb.insert(make_pair(make_pair(c2,c1),res));
		}
		cin >> d;
		for(int j=0;j!=d;j++)
		{
			cin >> c1 >> c2 ;
			oppo.insert(make_pair(c1,c2));
			oppo.insert(make_pair(c2,c1));
		}

		cin >> n;
		
		char lastelement;
		for(int j=0;j!=n;j++)
		{
			cin >> c1;
			for(int k = 0; k<8;k++){
				if(c1==bse[k]){
					elements[c1]++;
					break;
				}
			}
			expo = false;
			if(elementlist.size()!=0){
				lastelement = elementlist[elementlist.size()-1];
				//elementlist.push_back(c1);
				if(comb.find(make_pair(c1,lastelement))!=comb.end())
				{
					elementlist[elementlist.size()-1]=comb[make_pair(c1,lastelement)];
					elements[lastelement]--;
					elements[c1]--;
					expo = true;
				}
				else 
				{
					for(map<char, int>::iterator f = elements.begin();f!=elements.end();f++)
					{
						if(f->second>0)
						{
							set<pair<char,char>>::iterator f1 = oppo.find(make_pair(f->first,c1));
							if(f1==oppo.end()) continue;
							elementlist.clear();
							elements.clear();
							expo = true;
							break;
						}
					}
				}
			}
			if(!expo) elementlist.push_back(c1);
		}
		
		cout << "Case #" << i+1 << ": " << "[" ;
		if(elementlist.size()!=0){
			int h=0;
			for(;h!=elementlist.size()-1;h++)
			{
				cout << elementlist[h] << ", ";
			}
			cout <<  elementlist[h] << "]" << endl;
		}
		else cout <<  "]" << endl;
	}
}