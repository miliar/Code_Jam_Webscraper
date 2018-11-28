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

int main()
{
    READ;
    WRITE;

    int t;

   // cin>>t;
    scanf("%d\n",&t);
    int ar[500]={0};
    char chr[500];
    chr[101]='o';
chr[106]='u';
chr[112]='r';
chr[32]=' ';
chr[109]='l';
chr[121]='a';
chr[115]='n';
chr[108]='g';
chr[99]='e';
chr[107]='i';
chr[100]='s';
chr[120]='m';
chr[118]='p';
chr[110]='b';
chr[114]='t';
chr[105]='d';
chr[98]='h';
chr[116]='w';
chr[97]='y';
chr[104]='x';
chr[119]='f';
chr[102]='c';
chr[111]='k';
chr[117]='j';
chr[103]='v';
chr['z']='q';
chr['q']='z';

int cs=1;
    while(t--)
    {
        string str,str_out="";

        //cin>>str;
        //cin>>str_out;
        getline(cin,str);
       // getline(cin,str_out);



        for(int i=0;i<str.size();i++)
        {
          /*  if(ar[(int)str[i]]!=1)
            {ar[(int)str[i]]=1;
            C "chr["<<(int)str[i]<<"]='"<<str_out[i]<<"';" E;}
*/
        str_out+=chr[(int)str[i]];

            //if(ar[(int)str[i]]!=0 && ar[(int)str[i]]!=(int)str_out[i]) C "Error @ "<<i E;
            //ar[(int)str[i]]=(int)str_out[i];


        }

        C "Case #"<<cs++<<": "<<str_out E;

    }

  //  cout << "Hello world!" << endl;
    return 0;
}
