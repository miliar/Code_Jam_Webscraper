//prob4
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<sstream>
#define vi vector<int>
#define vvi vector<vector<int> >
#define pii pair<int,int> 
#define vs vector<string> 
using namespace std;

int main()
{
    int tes;
    cin>>tes;
    int count=1;
    while(tes--)
    {
        int k;
        string s;
        cin>>k>>s;
        int mini=1000000000;
        vector<int> v;
        int i,j;
        for(i=0;i<k;i++)
        v.push_back(i);
        do
        {
            string t;
            string s1;
            int st=0;
            for(st=0;st<s.size();st+=k)
            {
                s1=s.substr(st,k);
                string s2;
                for(i=0;i<k;i++)
                {
                    s2.push_back(s1[v[i]]);
                }
                t+=s2;
            }
            int val=0;
            int last=0;
            for(i=0;i<t.size();i++)
            {
                if(t[i]!=last)
                {
                    last=t[i];
                    val++;
                }
            }
            mini=min(val,mini);
        }while(next_permutation(v.begin(),v.end()));
        cout<<"Case #"<<count<<": "<<mini<<endl;
        count++;
    }
    return 0;
}
        
        
                    
