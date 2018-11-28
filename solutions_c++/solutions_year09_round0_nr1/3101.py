#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

vector<string > a;
vector<string > b;
queue<string> list;

void solve()
{
	ifstream f("A-small.in", ios::in);
	ofstream g("A-small.out", ios::out);
	int l, d, n;
	f>>l>>d>>n;

	string aux;

	a.push_back("");
	for (int i=1; i<=d; ++i)
	{
		f>>aux;
		a.push_back(aux);
	}
	b.push_back("");
	for (int i=1; i<=n; ++i)
	{
		f>>aux;
		b.push_back(aux);
	}	
	//end of file

	//insert in queue
	for (int i=1; i<=n; ++i)	//try to translate
	{
		int poz=0;
		int ch=0;
		if (b[i][ch]=='(')
		{
			for (ch=ch+1; b[i][ch]!=')'; ++ch)
			{
				for (int j=1; j<=d; ++j)
					if ( b[i][ch] == a[j][0])
					{
						list.push(a[j]);
						//cout<<a[j]<<" ";
					}
			}
		}
		else
		{
			for (int j=1; j<=d; ++j)
				if ( b[i][ch] == a[j][0] )
				{
					list.push(a[j]);
					//cout<<a[j]<<" ";
				}
		}
		++ch;
		++poz;
		
		while ( ch < (int)b[i].size() && !list.empty() )
		{
			string temp;
			if ( b[i][ch] != '(')
				for (int itlst=1; itlst<=(int)list.size(); ++itlst)
				{
					//caracter ch
					//pozition in string poz
					temp=list.front();
					list.pop();
					if ( temp[poz] == b[i][ch])
						list.push(temp);
				}
			else
			{
				int ch2;
				int NrElLst=list.size();
				for (int itlst=1; itlst<=NrElLst; ++itlst)
				{
					temp=list.front();
					list.pop();
					for (ch2=ch+1; b[i][ch2]!=')'; ++ch2)
						if (temp[poz] == b[i][ch2])
						{
							//cout<<"Serban!";
							list.push(temp);
							//cout<<"Serban!";
						}
				}
				ch=ch2;
			}
			++ch;
			++poz;
		}
		g<<"Case #"<<i<<": "<<list.size()<<"\n";

		while (!list.empty())
		{
			list.pop(); 
		}
	}
	f.close();
	g.close();
}

int main()
{
	solve();
	return 0;
}