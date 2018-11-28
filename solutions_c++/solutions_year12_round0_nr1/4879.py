#include<iostream>
#include<cstdlib>
#include<vector>
#include<climits>
#include<cctype>
#include<map>
#include<list>
#include<cstdio>
#include<algorithm>
#include<memory.h>
#include<cmath>
#include<queue>
#include<fstream>
#define L long long int
#define LD long double
#define pi 3.141592653589793238462643383
#define M 1000000007

using namespace std;

int main()
{
    int t,i,n;
    char h[26];
    string s;
    h[0]='y';
    h[1]='h';
    h[2]='e';
    h[3]='s';
    h[4]='o';
    h[5]='c';
    h[6]='v';
    h[7]='x';
    h[8]='d';
    h[9]='u';
    h[10]='i';
    h[11]='g';
    h[12]='l';
    h[13]='b';
    h[14]='k';
    h[15]='r';
    h[16]='z';
    h[17]='t';
    h[18]='n';
    h[19]='w';
    h[20]='j';
    h[21]='p';
    h[22]='f';
    h[23]='m';
    h[24]='a';
    h[25]='q';
    scanf("%d",&t);
    getline(cin,s);
    ofstream out("cjqra");
    int k=1;
    while(t--)
    {
              getline(cin,s);
              n=s.size();
              out<<"Case #"<<k<<": ";
              for(i=0;i<n;i++)
              if(s[i]!=' ')
              out<<h[s[i]-'a'];
              else
              out<<" ";
              out<<"\n";
              k++;
              
              
    }
    return 0;
}
