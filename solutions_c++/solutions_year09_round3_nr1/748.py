#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
#define Vs vector<string>
#define Vsi Vs::iterator
#define Vi vector<int>
#define Vii Vi::iterator
#define Pb(v,e) (v).push_back(e)
#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(

int main()
{

    int testcase;
    scanf("%d",&testcase);
    string s;
    getline(cin,s);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        getline(cin,s);
        char a[256];
        char str[64];
        int i,j,len=s.size(),n=0;
        for(i=0; i<256; i++)a[i]=-1;
        a[s[0]]=1;
        str[0]=1;
        for(i=1; i<len; i++) {
            char ch=s[i];
            if(a[ch]==-1) {
                a[ch]=n;
                n++;
                if(n==1)n++;
            }
            str[i] = a[ch];
        }
        int max=0;
        for(i=0; i<len; i++) {
            if(max<str[i])max=str[i];
        }
        n=max+1;
        long long ret=0;
        for(i=0; i<len; i++) {
            ret*=(int64)n;
            ret+=(int64)str[i];
        }

        cout<<"Case #"<<caseId<<": "<<ret<<endl;
    }
    return 0;
}