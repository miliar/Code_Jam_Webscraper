#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
using namespace std;

typedef long long  ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ld> vld;
typedef vector<vld> vvld;
typedef pair<ld,ld> ldld;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef pair<ll,ll> llll;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<string,string> ss;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef pair<char,char> cc;

typedef set<int> si;
typedef set<int>::iterator siit;
typedef set<char> sc;
typedef set<char>::iterator scit;
typedef set<string> sstr;
typedef set<string>::iterator sstrit;


#define sz(v) int((v).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define ALL(C) (C).begin(), (C).end()
#define INF numeric_limits<int>::max()
#define MINF numeric_limits<int>::min()
#define DODEB 1
#define db(C) if(0){std::cout<<#C <<" = "<< (C)<<std::endl;}
#define dbv(C) if(0){std::cout<<#C <<" = "; for(typeof((C).begin()) i = (C).begin(); i != (C).end(); i++){ cout<<*i<<" "; } cout<<endl;}
#define LET(i,e) __typeof(e) i = (e)
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define CPRESENT(c,x) (find(all(c),x) != (c).end())
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define SORT(C) sort(ALL(C))
#define SORTD(C) sort(ALL(C))
#define REV(C)	reverse(ALL(C))
#define UN(v)	SORT(v), v.erase(unique( v.begin(), v.end()), v.end())
#define MIN(C) *min_element(ALL(C))
#define MINPOS(C) (int)(min_element(ALL(C)) - (C).begin())
#define MAX(C) *max_element(ALL(C))
#define MAXPOS(C) (int)(max_element(ALL(C)) - (C).begin())
#define SUM(C) accumulate(ALL(C), 0)
#define BE(C) ((C).begin())
#define EN(C) ((C).end())
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define FORV(iter,c)  if ((c).begin() != (c).end()) for (typeof((c).begin()) iter = (c).begin(); iter != (c).end(); i++)
#define FORVV(i, j, c)  for (int  i = 0; i < (int)(c).size(); i++) for (int  j = 0; j < (int)(c[0]).size(); j++)
#define pb push_back
#define Fi(xy) ((xy).first)
#define Se(xy) ((xy).second)
#define SQ(x)	((x)*(x))
#define mp make_pair
#define CLC(act,val) (*({act; static typeof(val) CLCR; CLCR = (val); &CLCR;}))
#define FIRSTP(k,a,b,cond) CLC(LET(k, a); for(; k < (b); ++k) if(cond) break, k)
#define LASTP(k,a,b,cond) CLC(LET(k, b); while((a) <= (--k)) if(cond) break, k)
#define EXISTS(k,a,b,cond) (FIRSTP(k,a,b,cond) < (b))
#define ALLMEET(k,a,b,cond) (!EXISTS(k,a,b,!(cond)))
#define RMVAL(c,val)  while( find(ALL(c),val) != (c).end() ){ c.erase( find(ALL(c),val) );};
#define CLOCK cout<<"CLOCK "<< (double)clock()/CLOCKS_PER_SEC <<endl

const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-10;//NOTES:eps

ll gcd(ll x, ll y)
{
    return x ? gcd(y%x,x) : y;
}
ll lcm(ll x, ll y)
{
    return x*(y/gcd(x,y));
}
string c2s(char c)
{
    string s="";
    s+=c;
    return s;
}

template<typename T> void remin(T& a, const T& b)
{
    if (b < a) a = b;
}
template<typename T> void remax(T& a, const T& b)
{
    if (b > a) a = b;
}
// should use like vi c= lenmin(a,b), not func(lenmin(a,b))
template<typename T> T lenmin( const T & a, const T & b)
{
    if ( (a.size()) < ( b.size()) )        return a;
    else if ( (a.size()) > ( b.size() ) )        return b;
    else    	return (a) < (b) ? (a) : (b);
}
template<typename T> T lenmax( const T & a, const T & b)
{
    if ( (a.size()) > ( b.size()) )        return a;
    else if ( (a.size()) < ( b.size() ) )        return b;
    else    	return (a) > (b) ? (a) : (b);
}


template<class T> string toString(T n)
{
    ostringstream ost;    //NOTES:toString
    ost<<n;
    ost.flush();
    return ost.str();
}
int toInt(string s)
{
    int r=0;    //NOTES:toInt(
    istringstream sin(s);
    sin>>r;
    return r;
}

template <typename T> vi n2vi(  T in, int base)
{
    char buff[200];
    itoa( in, buff, base);
    vi c;
    int l  = strlen(buff);
    for (int i = 0; i < l ; ++i  )
    {
        c.push_back( buff[i] - '0');
    };
    return c;
}

template <typename T> ll vi2n(  T in, int base)
{
    ll tic =1;
    ll sum = 0;
    int p ;

    for ( p = in.size()-1; p>=0; --p)
    {
        sum += in[p]* tic;
        tic*= base;
    }
    return sum;
}

int CN;

////////////////////////////////////////////////
// real work here
////////////////////////////////////////////////
int pushdir ( vvs & out, string in)
{

   if(0)
   {    cout<<" out contant" <<endl;
        FOR( i, 0, sz(out))
        {
            FOR( j, 0, sz(out[i]))
            {
            	cout<<" " << out[i][j];
            };
            cout<<endl;
        };
   }

    vs dis;
    string t = in;
    if(t[0]=='/') t=t.substr(1);
    int l ;
    while( (l=t.find('/'))!=string::npos)
    {
        string k  = t.substr(0,l );
        t=t.substr(l+1);
        dis.pb(k);
    }
    dis.pb(t);
    dbv(dis);

   vs findme;
   vs oldfindme = findme;
   for( ; sz(findme) < sz(dis); )
   {

        findme.pb(dis[sz(findme)]);
        dbv(findme);
        if( find(out.begin(),out.end(),findme) != out.end())
           {
            oldfindme = findme;
             continue;
           }
        else
            break;
   };
    dbv(findme);
    dbv(oldfindme);

    vs tmpdis = dis;
    do
    {
            out.pb(tmpdis);
            tmpdis.erase(sz(tmpdis)-1+tmpdis.begin());
    }while(sz(tmpdis)>0);

   return sz(dis) - sz(oldfindme);
}

int work(vs old, vs cr)
{
    vvs dir;

    FOR( i, 0, sz(old))
    {
    	pushdir(dir, old[i]);
    };
    int sum = 0;
    FOR( i, 0, sz(cr))
    {
    	sum += pushdir(dir, cr[i]);
    	cout<<" for  "<<cr[i]<< "  do for "<< sum  <<endl;
    };
    return sum;
}

int main()
{


    ifstream infile ("GCJinput.txt");
    ofstream outfile ("GCJoutput.txt");
    string line;

    if (infile.is_open())
    {
        getline (infile,line);
        istringstream r(line);
        r>> CN;
        int cid = 0;

        do
        {
            cid++;
            // from here process the input content
            getline (infile,line);
            if (!(line.size () > 0))
                return 0;
            istringstream param(line);
            int p1,p2;
            param >> p1;
            param >> p2;
            outfile<<"Case #"<<(cid)<<": ";
            vs old;
            FOR( i, 0, p1)
            {
                getline (infile,line);
                    old.pb(line);
            };
            vs cr;
            FOR( i, 0, p2)
            {
                          getline (infile,line);
                    cr.pb(line);

            };

              outfile<<work(old, cr)<<endl;

        }
        while (! infile.eof() );
        infile.close();
    };
    outfile.close();

    return 0;




}




//D:\G codejam\test_a\main.cpp
//D:\G codejam\test_a\GCJoutput.txt
