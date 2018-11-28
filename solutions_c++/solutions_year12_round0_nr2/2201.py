#pragma comment(linker,"/STACK:16777216")
#pragma warning ( disable: 4786)
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

#define pb push_back

#define vi vector<int>
#define vf vector<float>
#define vd vector<double>
#define vi64 vector<int64>
#define vs vector<string>
#define vc vector<char>

#define int64 long long

#define mii map<int,int>
#define mci map<char,int>
#define mic map<int,char>
#define msi map<string,int>
#define mis map<int,string>

mii mymap;

int triplet(int n,int p,int &s)
{
    int d = n/3;
    if(d>=p)return 1;
    int remainder = n%3;
    if(remainder==0)
    {
        if(s!=0 && n>=2 && n<=28)
        {
            ++d;
            if(d>=p)
            {
                --s;
                return 1;
            }
        }
        return 0;
    }
    if(remainder==1)
    {
        if(d+1>=p)return 1;
        return 0;
    }
    if(remainder==2)
    {
        if(d+1>=p)return 1;
        if(s!=0 && n>=2 && n<=28)
        {
            d+=2;
            if(d>=p)
            {
                --s;
                return 1;
            }
        }
        return 0;
    }
    return 0;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,a,b,c,d,m,n,N,S,P,testCase,caseNo;
	char ch;
	string st;
    cin >> testCase;
    caseNo = 0;
    int sum;
    while(testCase--)
    {
        ++caseNo;
        sum = 0;
        cin >> N >> S >> P;
        for(i = 0;i < N;++i)
        {
            cin >> n;
            sum+=triplet(n,P,S);
        }
        printf("Case #%d: %d\n",caseNo,sum);
    }
	return 0;
}
