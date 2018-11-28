#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
#define all(v) (v).begin(),(v).end()
using namespace std ;
long long toint(string s){istringstream is(s);long long t;is>>t;return t;}
string tos(long long t){stringstream st;st<<t;return st.str();}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t;
    cin>>t;
    for(int caso=0;caso<t;caso++)
    {
        string s;
        cin>>s;
        map<char,int>m;
        for(int i=0;i<26;i++)m[i+'a']=-1;
        for(int i=0;i<=9;i++)m['0'+i]=-1;
        m[s[0]]=1;
        vector<int>v(s.size(),0);
        for(int i=0;i<s.size();i++)if(s[i]==s[0])v[i]=1;
        int cont=0;
        for(int i=1;i<s.size();i++)
        {
            if(m[s[i]]==-1)
            {
                m[s[i]]=cont;
                for(int j=1;j<s.size();j++)if(s[i]==s[j])v[i]=cont;
                if(cont==0)cont=2;else cont++;    
            }
            else v[i]=m[s[i]];
        }   
        long long maxi=*max_element(all(v))+1;
        long long dev=0;
        for(int i=0;i<v.size();i++)
            dev=dev*maxi+v[i];
        cout<<"Case #"<<caso+1<<": "<<dev<<endl;  
        
    }
    
    //system("pause");
    return 0;
}


