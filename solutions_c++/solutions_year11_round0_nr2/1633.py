#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

string extract(string s)
{
    int l = s.length();
    string r="";
    
    for (int i=0;i<l-1;i++)
    r = r + s[i];
    
    return r;
}

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
	//freopen("output.txt","w",stdout);
	
	int t;
	cin>>t;
	for (int cas=1;cas<=t;cas++)
	{
        int C;
        map<pair<char,char>,char> m;
        cin>>C;
        for (int i=0;i<C;i++)
        {
            string s;
            cin>>s;
            m[make_pair(s[0],s[1])] = s[2];
            m[make_pair(s[1],s[0])] = s[2];
        }
        
        int D;
        cin>>D;
        map<pair<char,char>,int> mv;
        for (int i=0;i<D;i++)
        {
            string tt;
            cin>>tt;
            mv[make_pair(tt[0],tt[1])]=1;
            mv[make_pair(tt[1],tt[0])]=1;
        }
            
        
        int N;
        string str;
        cin>>N;
        cin>>str;
        
        string p_s = "";
        p_s += str[0];
        
        for (int i=1;i<str.length();i++)
        {

            if (m[make_pair(str[i],p_s[p_s.length()-1])]!=0)
            {
                p_s = extract(p_s) + m[make_pair(str[i],p_s[p_s.length()-1])];
            }
            else
            {
                p_s = p_s + str[i];
            
                for (int j=0; j<p_s.length()-1; j++)
                {
                    if (mv[make_pair(p_s[j],str[i])])
                    {
                    p_s = "";
                    break;
                    }
                }
            }
        }
        cout<<"Case #"<<cas<<": [";
        if (p_s.length() > 0)
        {
            for (int i=0;i<p_s.length()-1;i++)
            cout<<p_s[i]<<", ";
            cout<<p_s[p_s.length()-1];
        }
        cout<<"]"<<endl;
    }
    
	
	return 0;
}
