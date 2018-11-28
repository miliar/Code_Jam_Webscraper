#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>
#define city 0
#define SIZE 3000000
#define MAX  1000100
using namespace std;


map< string , int > dir;
string solve(string op)
{
    if(op.size()==1)return "";


    return op.substr(0,op.find_last_of("/"));
}



int main(void)
{
    int cases,n,m;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>cases;
    int t=0;
    int i , j;
    string str,sub,op="/";
    bool next;
    while(t<cases){
        t++;
        dir.clear();
        cin>>n>>m;
        for(i=0;i<n;i++){
            cin>>str;
            sub=str;

            while(sub.size()>1){
                next=false;
                if(!dir.count(sub)){
                    next=true;
                    dir.insert(pair<string,int>(sub,0));
                }
                if(!next)break;
                sub=solve(sub);


            }

        }
        int ans=0;
        for(i=0;i<m;i++){
            cin>>str;
            sub=str;
            while(sub.size()>1){
                next=false;
                if(!dir.count(sub)){
                    next=true;
                    ans++;
                    dir.insert(pair<string,int>(sub,0));
                }
                if(!next)break;
                sub=solve(sub);

            }

        }
        cout<<"Case #"<<t<<": "<<ans<<endl;





    }
    return city;
}
