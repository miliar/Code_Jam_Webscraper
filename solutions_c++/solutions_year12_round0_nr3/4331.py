#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <complex>
#include <list>
#include <functional>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
#define F(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define C cout<<
#define E <<endl

typedef vector<int> vi;

template <class T> inline bool isPwr2(T x){return (x != 0) && ((x & (x - 1)) == 0);}
string int2str(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

int main()
{
    int t,cs=1,A,B;
    long long cnt=0;
    READ;
    WRITE;

    cin>>t;
    while(t--)
    {
        cin>>A>>B;
        cnt=0;


        for(int i=A;i<=B;i++)
        {
            if (i==1000) continue;
            string str=int2str(i);
            int sz=str.size(),num;
            string str_temp="";


            if(sz==2)
            {

                num=(str[1]-48)*10+(str[0]-48);
                if(num>i && num!=i && int2str(num).size()== sz && num<=B) cnt++;



            }

            if(sz==3)
            {
               // num=(str[1]-48)*100+(str[0]-48)*10+(str[2]-48);
               //if(num>i && num!=i && int2str(num).size()== sz && num<=B) {C " "<<i<<" "<<num E;cnt++;}

                //2nd phase

                num=(str[2]-48)*100+(str[0]-48)*10+(str[1]-48);
               if(num>i && num!=i && int2str(num).size()== sz && num<=B) cnt++;

               num=(str[1]-48)*100+(str[2]-48)*10+(str[0]-48);
               if(num>i && num!=i && int2str(num).size()== sz && num<=B) cnt++;


            }


//            for(int j=10;;j*=10)
//            {
//                if((i/j)==0) break;
//                int num=(i%j)*j+(i/j);
//
//                if(int2str(num).size()== sz && num<=B) {C " "<<i<<" "<<num E;cnt++;}
//
//            }

        }

        C "Case #"<<cs++<<": "<<cnt E;
    }

    return 0;
}
