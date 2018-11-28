#line 2 "DiagonalDisproportion.cpp"
///////////////////////////////////Pre-Written Code/////////////////////////////
    #include  <ctime>
    #include  <string.h>
    #include <stdio.h>
    #include <vector>
    #include <queue>
    #include <iostream>
    #include <algorithm>
    #include <stdlib.h>
    #include <math.h>
    #include <numeric>
    #include <map>
    #include <set>
    #include <sstream>
    #include <functional>

    using namespace std;
    #define all(c) c.begin(),c.end()
    #define rep_(i,n) for(i=n-1;i>=0;i--)
    #define rep(i,n) for(i=0;i<n;i++)
    #define forr(i,a,b) for(i=a;i<=b;i++)
    #define forr_(i,a,b) for(i=a;i>=b;i--)
    #define min(a,b) ( a>b? b : a )
    #define max(a,b) ( a>b? a : b )
    #define sz size()
    #define pb(a) push_back(a)
    #define mset(a,v) memset(a,v,sizeof(a))
    #define f first
    #define s second
    #define tr(c,i) for( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
    #define EPS 1e-11

    typedef vector<int> vi;
    typedef vector<vi> vvi;
    typedef map<int,int> mi;
    typedef pair<int,int> pii;
    typedef vector<pii> vpii;
    typedef vector<string> vs;
    typedef pair<string,int> psi;
    typedef vector<psi> vpsi;
    typedef queue<int> qi;
    typedef queue<pii> qpii;
    typedef unsigned long long ubig;
    typedef long long big;
    typedef long double bigd;
    typedef stringstream ss;
    template<class T> string tos(T x){stringstream ss;  ss<<x; return ss.str();}
    void rot(vvi v,vvi& tmp,int r1,int c1,int r2,int c2)
    {
        tmp.resize(c2-c1+1);
        int i,j;
        rep(i,tmp.sz)
            tmp[i].resize(r2-r1+1);
        forr(i,r1,r2)
            forr(j,c1,c2)
                tmp[j-c1][tmp[0].sz-(i-r1)-1]=v[i][j];
    }
    bool isPal(string s)
    {
        int i=0,j=s.sz-1;
        while(i<j)
        {
            if(islower(s[i]) && islower(s[j]) && s[i]!=s[j])
                return false;
            i++; j--;
        }
        return true;
    }

    bool* sieve(int n)
    {
       bool* prime = new bool[n+1];
       int i;
       rep( i , n+1 ) prime[i]=true;
       prime[0]=false;
       prime[1]=false;
       int m=(int) sqrt(n);
       for (int i=2; i<=m; i++)
          if ( prime[i] )
             for (int k=i*i; k<=n; k+=i)
                prime[k]=false;

       return prime;
    }

    ubig toD( int b , string s )
    {
        ubig res=0,tmp=1;
        int i;
        int arr[256];
        rep( i , s.sz ) s[i]=tolower(s[i]);
        rep( i , 256 ) arr[i]=i-48;
        forr( i , 'a' , 'z' ) arr[i]= i-'a'+10;
        rep_( i , s.sz )
            res+= arr[ s[i] ]*tmp, tmp*=b;
        return res;
    }
    string toB( int b , ubig n )
    {
        string s="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" , res ;
        if( !n ) return "0";
        while( n )
        {
            res.pb( s[n%b] );
            n/=b;
        }
        reverse( all(res) );
        return res;
    }
    int gcd(int a ,int b)
    {
        if( b==0 )return a;
        return gcd( b , a%b );
    }
    int lcm(int a, int b)
    {
        return a*b/gcd(a,b);
    }
    unsigned inf=1000000000*2;
    ///////////////////////////////////Pre-Written Code/////////////////////////////
int find( string str , map<string,char> mp )
{
    tr( mp , it )if( it->f==str )return true;
    return false;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    string ans="";
    string inv,tmp;
    int t , i , j , a , x;
    cin>>t;
    forr( x , 1 , t )
    {
        map<string,char> com;
        set<string> op;
        ans="";
        cin>>a;
        rep( i , a )
            cin>>tmp, com[ tmp.substr(0,2) ]=tmp[2] , reverse(all(tmp)) , com[ tmp.substr(1) ]=tmp[0];
        cin>>a;
        rep( i , a )cin>>tmp, op.insert(tmp) , reverse(all(tmp)) , op.insert(tmp);
        cin>>a>>inv;
        rep( i , inv.sz )
        {
            ans+=inv[i];
            if( ans.sz > 1 )
            {
                if( find( ans.substr( ans.sz-2 , 2 ) , com ) )
                {
                    ans = ans.substr(0,ans.sz-2)+com[ ans.substr( ans.sz-2 , 2 ) ];
                }
                else
                {
                    rep( j , ans.sz-1 )
                    {
                        tmp=inv[i];
                        tmp+=ans[j];
                        if( op.find(tmp)!=op.end() ){ ans=""; break; }
                    }
                }
            }
        }
        cout<<"Case #"<<x<<": [";
        if(ans.sz>=1)cout<<ans[0];
       forr( i , 1 , (int)ans.sz-1 )cout<<", "<<ans[i];
        cout<<"]\n";
    }
    return 0;
}
