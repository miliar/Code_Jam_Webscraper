#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <memory.h>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <iterator>
#include <sstream>
#include <ctype.h>
#include <queue>
#include <numeric>
#include <list>
#include <bitset>
#include <string.h>
#include <stddef.h>
#include <complex>
#include <limits.h>
#include <fcntl.h>
#include <unistd.h>

using namespace std;

#define sz(x) ((int) (x).size())
#define myfor(a,b) for(typeof((b).end()) a=(b).begin();a!=(b).end();a++)
#define clrto(a,b) memset(a,b,sizeof a)
#define clr(x) memset((x), 0, sizeof(x))
#define myall(a) (a).begin(),(a).end()
#define mysort(a) sort(myall(a))
#define scan(a) fscanf(in,"%d",&a)
#define var(a,b) __typeof(b) a=(b)
#define fora(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define ford(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define myforeach(it,c) for( var(it,(c).begin());it!=(c).end();++it)
#define rep(i,n) fora(i,0,n)
#define myreverse(c) reverse(myall(c))
#define myunique(c) mysort(c),(c).resize(unique(myall(c))-(c).begin())
#define pz(x) (x)<0?0:(x)
#define pvt(x) ((x)<0?(x*(-1)):(x))


template<class T>void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

template<class T> T gcd(T a, T b)
{
    return b ? gcd(b, a % b) : a;
}

template <class _T> inline _T SQR(const _T& x)
{
  return x * x;
}

template <class _T> inline string TOSTR(const _T& a)
{
  ostringstream os("");
  os << a;
  return os.str();
}

template <class _T> inline istream& operator << (istream& is, const _T& a)
{
    is.putback(a);
    return is;
}


void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}



typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef vector < bool > VB;
typedef map < string, int > MSI;
typedef long long int64;

////////////////////////////////////////////////
////////////////////////////////////////////////
////////////////////////////////////////////////





int main()
{



    int test=0;
    cin>>test;
    for(int caseno=1;caseno<=test;caseno++)
    {
        VI O,B;
        VS seq;

        O.clear();
        B.clear();
        seq.clear();
        int co=1,cb=1;
        int n=0;
        cin>>n;
        rep(i,n)
        {
              int d=0;
              string ch;
              cin>>ch>>d;
              if(ch=="O")
              {
                  O.push_back(d);
                  seq.push_back(ch);
              }


              else
              {
                   B.push_back(d);
                   seq.push_back(ch);
              }

        }



//cout<<endl;
//               myforeach(p,O)
//                 cout <<*p <<" ";
//
//              cout<<endl;
//         myforeach(p,B)
//                 cout <<*p <<" ";
//
//              cout<<endl;
//        co=O.size();
//        cb=B.size();
//        int larger=co<cb?cb:co;
int h=0;
//cout<<B.size()<<"  "<<O.size() <<endl;
            if (B.size()>=2)
            {


              for( var(it,(B).rbegin() );it!=(B).rend() -1;++it)
                  { *it=pvt(  (  (*it>*(it+1))  ? *it-*(it+1) :(*(it+1)-*it) ) )+1;
              // *it=pvt(  (  (*it>*(it+1))  ? *it-*(it+1) :(*(it+1)-*it) ) )+1;
              // cout<<*it <<" b \n";

                  }

            }

            if(O.size()>=2)
            {

                for( var(it,(O).rbegin());it!=(O).rend() -1 ;++it)
                { *it=pvt(  (  (*it>*(it+1))  ? *it-*(it+1) :(*(it+1)-*it) ) )+1;
               //*it=pvt(  (  (*it>*(it+1) ) ? *it-*(it+1) :(*(it+1)-*it) ) )+1;
               //  cout<<*it <<" c  \n";
                }

            }
//               cout<<endl;
//               myforeach(p,O)
//                 cout <<*p <<" ";
//
//              cout<<endl;
//         myforeach(p,B)
//                 cout <<*p <<" ";
//
//              cout<<endl;


       int ret=0;
       co=cb=1;
       int i=0;
        rep(i,seq.size())
        {

            int stepo=0,stepb=0,can=1;
            if(O.size()==0 && B.size()==0)
              break;




           if (seq[i]=="O" &&  O.size() >0)
           {
               ret+= (O[0] ) ?O[0]:1;

               if( B.size() >0 && B[0]>O[0])
                  B[0]-=O[0];
                else if(B.size() >0)
                   B[0]=1;

                O.erase(O.begin());
           }

           else if(seq[i]=="B" &&  B.size() >0)
            {
                 ret+=( B[0] )?B[0]:1;

               if(O.size() >0 && (O[0]>B[0]))
                  O[0]-=B[0];
                  else if (O.size() >0)
                    O[0]=1;

                B.erase(B.begin());
            }



        }



        printf("Case #%d: %d\n",caseno,ret);



    }


return 0;
}
