#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <queue>
#include <stack>
using namespace std;
char digits[]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define repd(i,n) for (int i((n)-1); i >= 0; --i)
#define rep2(i,x,m) for(int i=x;i<m;i++)
#define rep2d(i,x,m) for(int i=x;i>=0;i--)
#define repit(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define fill(a,c) memset(&a, c, sizeof(a))
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
int cas(string s) {
	stringstream ss;
	ss << s;
	int res;
	ss >> res;
	return res;
}
string itob(int n,int b)
{
       
       int i,sign;
       char s[100];
       if((sign=n)<0)
       {
                     n=-n;
       }
       i=0;
       do
       {
           s[i]=digits[n%b];
           i++;
       }while(n/=b);
       if(sign<0)
         s[i++]='-';
       s[i]='\0';
       reverse(s,s+strlen(s));
       return s;
}
int itoa(string n,int b)
{
       int k=1,sum=0,l;
       repd(i,n.length())
       {
           rep(j,36) if(digits[j]==n[i]) {l=j;break;}
           sum+=l*k;
           k*=b;
       }
       return sum;
       
}

string mult(string m,int b)
{
    int a=itoa(m,b);
    a=a*a;
    return itob(a,b);
}
string add(string m,string n,int b)
{
    int a=itoa(m,b);
    int c=itoa(n,b);
    a=a+c;
    return itob(a,b);
}    
int main()
{
    freopen("in.txt","r",stdin);
    freopen("o.txt","w",stdout);
    int N;
    cin>>N;
    getchar();
    int r=0;
    while(N--)
    {
              r++;
              string str;
              int num[10];
              getline(cin,str);
              stringstream in(str);
              int k=0;
              while (in >> num[k])
              k++;
              //rep(h,k) cout<<num[h]<<" ";
              rep2(i,2,10000000)
              {
                                int flag[k],v=1;
                                rep(g,k) flag[g]=1;
                                int count=0;
                                rep(j,k)
                                {
                                        int sum=0;
                                        string s=itob(i,num[j]);
                                       // if(i==3) cout<<num[j]<<"--base\n";
                                        //cout<<s<<"\n";
                                        int c=0;
                                        while(c<50)
                                        {
                                                    c++;
                                                    sum=0;
                                        rep(l,s.length())
                                        {
                                                         //if(i==3) cout<<s[l]<<"--s[l]\n";
                                                         string t=s.substr(l,1);
                                                         
                                                         t=mult(t,num[j]);
                                                         //if(i==3) cout<<t<<"--t\n";
                                                         sum+=itoa(t,num[j]);
                                                         //if(i==3 && l==s.length()-1) cout<<sum<<"--sum\n";
                                        }
                                        //if (i==3 && sum==1) cout<<sum<<"--sum\n"; 
                                        if(sum==1) break;
                                        s=itob(sum,num[j]);
                                        }
                                        //if(i==3) cout<<sum<<" -sum"<<i<<"-i\n";
                                        if(sum==1)
                                        {
                                                         count++;
                                                         flag[j]=0;
                                        } 
                                }
                                rep(g,k) if(flag[g]) {v=0;break;} 
                                if(!v) continue;
                                cout<<"Case #"<<r<<": "<<i<<"\n"; 
                                break;                            
              }
    }
    getchar();
}
