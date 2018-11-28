#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define all(v) (v).begin(),(v).end()
//long long toint(string s){long long t;istringstream is(s);is>>t;return t;}
//string tos(long long t){stringstream st;st<<t;return st.str();}
using namespace std;
int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
    	  
    int N=0;
    cin>>N;
    for(int caso=0;caso<N;caso++)
    {
        int t;
        cin>>t;
        vector<string>s(t);
        for(int i=0;i<t;i++)
            cin>>s[i];
        //for(int i=0;i<s.size();i++)cout<<s[i]<<endl;cout<<endl;
                
        map<vector<string>,bool >m;
        queue<pair<vector<string>,int> >Q;
        Q.push(make_pair(s,0));
        short dev=0;
        m[s]=1;
        while(!Q.empty())
        {
            
            pair<vector<string>,int>P=Q.front();
            Q.pop();
            
            vector<string>ind=P.first;
            int cost=P.second;
           bool ok=0;
            for(int i=0;i<t;i++)
                for(int j=i+1;j<t;j++)
                    if(ind[i][j]=='1'){ok=1;break;}
            if(!ok){dev=cost;break;}
            
            for(int i=0;i+1<ind.size();i++)
            {
                swap(ind[i],ind[i+1]);
                if(m[ind]==0)
                {
                    m[ind]=1;
                    Q.push(make_pair(ind,cost+1));
                }
                swap(ind[i],ind[i+1]);    
            }        
        }
       
        cout<<"Case #"<<caso+1<<": "<<dev<<endl;
    }
    //system("pause");
    return 0;
}
