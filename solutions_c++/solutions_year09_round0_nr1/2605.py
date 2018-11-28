#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cassert>
#include<queue>
#include<stack>
#include<sstream>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<list>
#include<cctype>
#include<iterator>

using namespace std;

#define sz size()
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define ii pair< int, int >
#define dd pair< double , double >
#define ll long long
#define vi vector< int > 
#define vvi vector< vi > 
#define v(x) vector< x > 
#define vs v(string)
#define vc v(char)
#define all(x) x.begin(),x.end()
#define fr(i,start,end) for(int i=start;i<end;i++)
#define fz(i,x) fr(i,0,x.sz)
#define ss stringstream
#define gi(i) scanf("%d",&i)
#define gl(i) scanf("%lld",&i)
#define dbgc(x) cout<<"Hello world - "<<#x<<endl;
#define dbg(x) cout<<#x<<"-->"<<x<<endl

typedef struct Dict
{
    string msg;
    map<char , struct Dict * > link;
}dict;
int check(dict * root , vs &test , int wcnt)
{
    int temp=0;
    if(wcnt<test.sz)
    {
        fz(i,test[wcnt])
        {
            if(root->link.find(test[wcnt][i])!=root->link.end())
                temp+=check(root->link[test[wcnt][i]],test,wcnt+1);
        }
        return temp;
    }
    return 1;
}
int main()
{
    int l,d,n;
    scanf("%d %d %d",&l,&d,&n);
    string str;
    dict * root = new dict;
    dict * temp = root;
    fr(i,0,d)
    {
       cin>>str;
       fz(i,str)
       {
            if(temp->link.find(str[i]) != temp->link.end())
            {
                temp = temp->link[str[i]];
            }
            else
            {
                temp->link[str[i]]= new dict;
                temp = temp->link[str[i]];
            }
       }
       temp->msg=str;
       temp=root;
    }
    fr(i,0,n)
    {
        cin>>str;
        vs test;
        fz(j,str)
        {
            if(str[j]=='(')
            {
                int t=j;
                while(str[++t]!=')');
                test.pb(str.substr(j+1,t-j-1));
                j=t;
            }
            else
                test.pb(string(1,str[j]));
        }
        printf("Case #%d: %d\n",i+1,check(root,test,0));
    }
    return 0;    
}
