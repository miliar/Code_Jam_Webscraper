
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

typedef stringstream ss;
typedef vector<int> vi;

string toString (int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int fromString(const string& s)
{
     istringstream stream (s);
     int t;
     stream >> t;
     return t;
}

int main() {
    freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);

    int tcnr=0;
    cin>>tcnr;

    rep(nr,tcnr){

        int min=0, max=0, res=0, numLength=0;
        string str="";
        cin>>min>>max;

        rep2(i,min,max)
        {
            str=toString(i);
            numLength=str.size();
            if(numLength==1)
                break;
            else
            {
                string actNum=str, newNum="";
                rep(j,numLength-1)
                {
                    newNum=actNum[numLength-1]+actNum.substr(0,numLength-1);
                    int tempNum=fromString(newNum);
                    if(tempNum>i && tempNum<=max)
                    {
                        res++;
 //                       cout<<i<<"-"<<tempNum<<endl;
                    }
                    actNum=newNum;
                }
            }
        }

        cout<<"Case #"<<(nr+1)<<": "<<res;
        if(nr<tcnr-1)
            cout<<endl;

    }
}
