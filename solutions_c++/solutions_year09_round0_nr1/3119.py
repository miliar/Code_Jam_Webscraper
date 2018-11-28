#include<iostream>
#include<vector>
#include<string>
#include<cctype>
#include<cstdio>
#include<algorithm>
using namespace std;
#define ll unsigned long long int
FILE* fp=freopen("a.in","r",stdin);
FILE* fp1=freopen("a.out","w",stdout);
int main()
{
    ll l,d,n;
    cin>>l>>d>>n;
    vector<string>data;
    for(int i=0;i<d;i++)
    {
            string s;
            cin>>s;
            data.push_back(s);
    }
    string s1;
    getline(cin,s1);
    vector<string>pa;
    for(int i=0;i<n;i++)
    {
            string s;
            getline(cin,s);
            pa.push_back(s);
                    
    }
    for(int i=0;i<n;i++)
    {
            ll count=0;
            vector<string>v(l);
            int l1=0;
            for(int j=0;j<pa[i].size();)
            {
                    if(pa[i][j]=='(')
                    {
                                     j++;
                                     string temp="";
                                     while(pa[i][j]!=')')
                                     {
                                     if(isalpha(pa[i][j]))
                                     {
                                     temp+=pa[i][j];
                                     j++;
                                     }
                                     else j++;
                                     }
                                     j++;
                                     //cout<<l1<<temp<<endl;
                                     v[l1++]=temp;
                                     
                                     
                    }
                    if(isalpha(pa[i][j]))
                    {
                     string temp="";
                     temp+=pa[i][j];
                     //cout<<l1<<temp<<endl;
                     v[l1++]=temp;
                     j++;
                    }
                   
                    
            }
           for(int k=0;k<d;k++)
            {
                    string d1=data[k];
                    int j1;
                    for(j1=0;j1<l;j1++)
                    {
                            string c=v[j1];
                            //cout<<c<<endl;
                            if(find(c.begin(),c.end(),data[k][j1])==c.end())break;
                    }
                    if(j1==l)count++;
            }
            cout<<"Case #"<<i+1<<": "<<count<<endl;
            
    }
    
    return 0;
}
