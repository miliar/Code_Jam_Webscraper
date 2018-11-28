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
#define int64 long long

int rotate(int n,int A,int B)
{
    //cout << "Rotaing .....................\n";
    //cout << n << endl;
    int len;
    char scanftest[100];

    sprintf(scanftest,"%d",n);
    string st = scanftest;

    len = st.size();
    st += st;
    string tempst;

    int i;
    //for(i = 1;(i<len) && (st[i]>=st[0]);++i)
    set<int> myset;
    for(i = 1;(i<len);++i)
    {
        tempst.assign(st,i,len);
        int m = atoi(tempst.c_str());

        if((A<=n)&&(n<m)&&(m<=B))
        {
            myset.insert(m);
        }
    }
    return myset.size();
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int i,caseNo,testCase;
	int A,B,sum;


    cin >> testCase;
    caseNo = 0;
    while(testCase--)
    {
        ++caseNo;
        sum = 0;
        cin >> A >> B;
        for(i = A;i<=B;++i)
            sum += rotate(i,A,B);
        printf("Case #%d: %d\n",caseNo,sum);
    }
	return 0;
}
