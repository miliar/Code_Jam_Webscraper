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

 void f(VI numbers, int index, int sum, string output)
{
	if (index == numbers.size())
	{
		cout<<output << " } = "<<   sum <<"\n";
		return;
	}

	// include numbers[index]
	string str=output;
	str+=" ";
	str+= TOSTR( numbers[index]);
	f(numbers, index + 1, sum + numbers[index], str);

	// exclude numbers[index]
	f(numbers, index + 1, sum, output);
}

struct ret{

VI in;
VI ex;
long long sum;

}fin;

 VI mainlist;

bool sumit(VI &in,VI &out)
{
    int ins=0,exs=0;
    myforeach(i,in)
    {
      //  cout<<" include "<<*i <<"  "<<mainlist[*i]<<endl;
         ins ^= mainlist[*i];
    }


     myforeach(i,out)
     {
         //  cout<<" exclude "<<*i <<"  "<<mainlist[*i]<<endl;
           exs ^= mainlist[*i];
     }


    return ins==exs &&in.size() && out.size();
}

void myf(VI numbers, int index, int sum, VI output,VI exclude)
{
	if (index == numbers.size())
	{
	    if(sumit(output,exclude))
          {
              if(fin.sum<sum)
              {
                  fin.in = output;
		          fin.ex=exclude;
		          fin.sum=sum;


              }
          }



		return;
	}

	// include numbers[index]
VI Ori=output,exori=exclude;


	output.push_back( int(index));
	myf(numbers, index + 1, sum + numbers[index], output,exori);

	// exclude numbers[index]
	exclude.push_back(index) ;
	myf(numbers, index + 1, sum, Ori,exclude);
}

int main()
{

int cs;
cin>>cs;
for(int cc=1;cc<=cs;cc++)
{
    fin.sum=0;
    int num;
    cin>>num;
    mainlist.clear();
    rep(i,num)
      {int d;
          cin>>d;

      mainlist.push_back(d);
      }
      VI a,b;

fin.in.clear();
fin.ex.clear();
fin.sum=0;

      myf(mainlist, 0, 0,a,b);


    if(!fin.sum)
    printf("Case #%d: NO\n",cc);
    else
      printf("Case #%d: %d\n",cc,fin.sum);
}

}
