#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>


using namespace std;

map <string, bool> tab;
string s;
int t,i,j,n,m;
int licz;

string obetnij(string s)
{
	int found=s.find_last_of("/");
	return s.substr(0,found);
}


int main(int argc, char *argv[])
{
    cin >> t;
    for(i=0;i<t;++i)
    {
		licz=0;
		tab.clear();
		tab[""]=1;
		cin >> n >> m;
	    for(j=0;j<n;++j)
	    {
			cin >> s;
			while(s!="")
			{
				tab[s]=1;
				s=obetnij(s);
			}
		}
	    for(j=0;j<m;++j)
	    {
			cin >> s;
			while(s!="")
			{
				if(tab.find(s)!=tab.end())
					break;
				licz++;
				tab[s]=1;
				s=obetnij(s);
			}
		}
		printf("Case #%d: %d\n",i+1,licz);
	}
	//system("PAUSE");
    return EXIT_SUCCESS;
}
