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
#define myreverse(c) reverse(all(c))
#define myunique(c) mysort(c),(c).resize(unique(myall(c))-(c).begin())
#define pz(x) (x)<0?0:(x)


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

VS com;
VS opp;

bool check(string &str)
{
    rep(i,com.size())
    {
        string look(com[i],0,2);
       // cout<<"\n com "<< look <<endl;

        int pos=str.find(look);
        if ( pos != string::npos )
             return true;
    }

    rep(j,opp.size())
    {
        string look="";
        look+=opp[j][0];
        //cout<<"\n opp "<< look <<endl;
        int pos=str.rfind(look);
        if ( pos != string::npos )
             {
                 look="";
                 look+=opp[j][1];
                // cout<<"\n opp2 "<< look <<endl;
                 int npos=str.find(look,pos+1);
                  if ( npos != string::npos )
                       return true;

             }
    }

    return false;
}


void fixit(string &str)
{
    rep(i,com.size())
    {
        string look(com[i],0,2);
        string rpl(com[i],2,1);
        //cout<<"\n com "<< look <<endl;

        int pos=str.find(look);
        if ( pos != string::npos )
        {
           // cout<<"\n before com replace |"<<str<<"|\n";
             str.replace( pos,2 ,rpl );

            // cout<<"\n after com replace |"<<str<<"|\n";
        }

    }

    rep(j,opp.size())
    {
        string look="";
        look+=opp[j][0];
       // cout<<"\n opp "<< look <<endl;
        int pos=str.find (look);
        if ( pos != string::npos )
             {
                 look="";
                 look+=opp[j][1];
                // cout<<"\n opp2 "<< look <<endl;
                 int npos=str.find(look,pos+1);
                // cout<<npos<<"  "<<str.length();
                  if ( npos != string::npos  )
                  {
                    // cout<<"\n before opp replace |"<<str<<"|\n";
                       //str.replace( pos,npos-pos +1 , "" );
                       str="";
                     // cout<<"\n after opp replace |"<<str<<"|\n";
                  }


             }
    }


}



int main()
{
       int caseno=0;
    cin>>caseno;

    rep(test,caseno)
    {
        com.clear();
        opp.clear();




        int comno=0,oppno=0;
        int mainlen=0;


        cin>>comno;
        for(int i=0;i<comno;i++)
        {
            string ch;
           cin>>ch;
            com.push_back(ch);

            swap(ch[0],ch[1]);

            com.push_back(ch);
        }


        cin>>oppno;
        for(int i=0;i<oppno;i++)
        {
            string ch;

            cin>>ch;
            opp.push_back(ch);
            swap(ch[0],ch[1]);

            opp.push_back(ch);

        }

        myunique(com);
        myunique(opp);
//        myforeach(it,com)
//          cout <<*it<<endl;
//        myforeach(it,opp)
//          cout<<*it<<endl;
          int rsc=0;
         rsc=0;
        int added=0;
        string out;
        string rs="";

        cin>>mainlen;
        cin>>out;
      myforeach(it,out)
      {
          rs+=*it;
          fixit(rs);
//          while(check(rs))
//            fixit(rs);
      }


        printf("Case #%d: ",test+1);

          printf("[");
        rep(i,rs.length())
        {
            if(i)
              printf(", %c",rs[i]);
            else
                printf("%c",rs[i]);
        }

          printf("]\n");







    }
return 0;
}
