#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#define f(x,y) for(int x=0;x<y;x++)
#define pb push_back
#define All(x) x.begin(),x.end()
using namespace std;

int main()
{
	ifstream fin("b.in");
	ofstream fout("b.out");
	
	int n;
	fin>>n;
	f(i,n)
	{
        string s;
        fin>>s;
        
        string r=s;
        bool flag=true;
        
        for(int j=s.size()-2;j>=0;j--)
        {
            for(int k=s.size()-1;k>j;k--)
            {
                if(s[j]<s[k])
                {
                    flag=false;
                    
                    r[j]=s[k];
                    r[k]=s[j];
                    
                    vector<char> v;
                    
                    for(int x=j+1;x<=s.size()-1;x++)v.pb(r[x]);
                    sort(All(v));
                    for(int x=j+1;x<=s.size()-1;x++)r[x]=v[x-j-1];
                    
                    break;
                }
            }
            if(!flag)break;
        }
        
        if(flag)//!!!
        {
            //vector<char> v;
            string t;
            
            f(k,s.size())t.pb(s[s.size()-k-1]);
            
            f(k,t.size())if(t[k]!='0')
            {
                char tmp=t[k];
                t[k]='0';
                t.insert(t.begin(),tmp);
                break;
            }
            
            r=t;
        }
        cout<<s<<endl;
        cout<<"Case #"<<i+1<<": "<<r<<endl;
        fout<<"Case #"<<i+1<<": "<<r<<endl;
    }
	
	cout<<"End."<<endl;
	cin.get();
	return 0;
}
