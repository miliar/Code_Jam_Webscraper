#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

// for size length iterator begin end push_back int char string vector stringstream

#define FOR(i,m,n) for(int i=(m);i<=(int)(n);i++)
#define rep(i,n) FOR(i,0,(n)-1)

using namespace std;
string readln()
{
    string s="";
    char buf[1000];
    cin.getline(buf,1000);
    s=buf;
    return s;
}

int timeinmin(char a,char b,char c,char d)
{
    a-='0';
    b-='0';
    c-='0';
    d-='0';
    return (a*10+b)*60+ c*10+d;

}

void pv(vector<int> a)
{
    rep(i,a.size())
        cout <<a[i]<<"  ";
    cout << "\n";
}

string main_fn()
{
    string retval="";
    int na,nb,T;
    stringstream ss0(readln());
    stringstream ss(readln());
    vector<int> sa,ea,sb,eb;
    ss>>na>>nb;
    ss0>>T;
    rep(i,na)
    {
        string s=readln();
        sa.push_back(timeinmin(s[0],s[1],s[3],s[4]));
        ea.push_back(timeinmin(s[6],s[7],s[9],s[10]));
    }

    rep(i,nb)
    {
        string s=readln();
        sb.push_back(timeinmin(s[0],s[1],s[3],s[4]));
        eb.push_back(timeinmin(s[6],s[7],s[9],s[10]));
    }

    sort(sa.begin(),sa.end());
    sort(sb.begin(),sb.end());
    sort(ea.begin(),ea.end());
    sort(eb.begin(),eb.end());

    int TA=na,TB=nb;
    rep(i,na)
    {
        rep(j,eb.size())
        {
            if(eb[j]+T <= sa[i])
            {
                TA--;
                eb[j]=999999;
                break;
            }
        }
    }
    rep(i,nb)
    {
        rep(j,ea.size())
        {
            if(ea[j]+T <= sb[i])
            {
                TB--;
                ea[j]=999999;
                break;
            }
        }
    }

    char buf[100];
    sprintf(buf,"%d %d",TA,TB);
    retval=buf;
    return retval;
}
int main()
{
    int N;
    char buf[1000];
    cin >> N;
    cin.getline(buf,1000);
    rep(i,N)
    {
        cout << "Case #"<<i+1<<": "<<main_fn()<<"\n";
    }
} 
