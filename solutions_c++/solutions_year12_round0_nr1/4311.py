#include <algorithm>
#include <vector>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <set>
#include <utility>
using namespace std;

vector <pair<char,char> > per;
bool veca[301];
        //        {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
char vecroradev[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	char a[100],b[100];
	ifstream in("in.in");
	ofstream out("out.out");
	int _n;
	in>>_n;
	in.getline(a,301,'\n');
	for(int _i=1;_i<=_n;_i++)
	{
	    out<<"Case #"<<_i<<": ";
		in.getline(a,301,'\n');
		int lung=strlen(a);
		for(int i=0;i<lung;i++)
		{
		    if(a[i]>='a' && a[i]<='z')
		    {
		        out<<vecroradev[a[i]-'a'];
		    }
		    else
                out<<" ";
		}
		out<<'\n';
	}
	sort(per.begin(),per.end());
	char aux='a';
	for(vector <pair<char,char> >::iterator it=per.begin();it!=per.end();it++)
	{
	    //out<<it->first<<"-"<<it->second<<"\n";
	    out<<"'"<<it->second<<"',";
	}
	return 0;




}
