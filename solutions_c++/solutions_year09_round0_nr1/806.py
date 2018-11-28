#include<iostream>
#include<map>
#include<string>
#include<sstream>
#include<vector>
using namespace std;
vector<string> words;

int main()
{
	int l,d,n;
	cin>>l>>d>>n;
	words.clear();
	string line;
	for(int i=0;i<d;i++)
	{
		cin>>line;
		words.push_back(line);
	}
	string patt;
	int cn=0;
	while(n--)
	{
		cn++;
		cin>>patt;
		for(int i=0;i<patt.size();i++) if(patt[i]==' ')
		{
			patt.erase(i);
			i--;
		}
		map<int,string> mp;
		int cnt=0;
		for(int i=0;i<patt.size();i++)
		{
			if(patt[i]=='(')
			{
				string temp="";
				int j;
				for(j=i+1;j<patt.size();j++)
				{
					if(patt[j]==')')
					{
						i=j;
						break;
					}
					else temp=temp+patt[j];
				}
				mp[cnt++]=temp;
			}
			else
			{
				string temp="";
				temp=temp+patt[i];
				mp[cnt++]=temp;
			}

		}

		int rv=0;
		for(int i=0;i<words.size();i++)
		{
			bool ok=true;
			for(int j=0;j<words[i].size();j++) if(mp[j].find(words[i][j])==-1) 
			{
				ok=false;
			}
			if(ok) rv++;

		}
		cout<<"Case #"<<cn<<": "<<rv<<endl;
	}
}
