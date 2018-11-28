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

int i,Case = 0,T,A,B;
double singleprob;
vector<double>probabilities;
double result,tmp;

double A1()
{
    //strategy 1
    tmp = B*probabilities[0] + (2.0*B+1)*(1-probabilities[0]);
    result = tmp;

    //strategy 3
    tmp = B+2;
    if(tmp<result)
        result = tmp;

    //strategy 2 no need same as st 2


}
double A2()
{
    //strategy 1
    tmp = (B-1)*(probabilities[0])*(probabilities[1]) +

          (2.0*B)*(probabilities[0])*(1-probabilities[1]) +

          (2.0*B)*(1-probabilities[0])*(probabilities[1]) +

          (2.0*B)*(1-probabilities[0])*(1-probabilities[1]);
    result = tmp;

    //strategy 3
    tmp = B+2;
    if(tmp<result)
        result = tmp;

    //strategy 2 back 1
    tmp = (B+1)*(probabilities[0])*(probabilities[1]) +

          (B+1)*(probabilities[0])*(1-probabilities[1]) +

          (2.0*B + 2)*(1-probabilities[0])*(probabilities[1]) +

          (2.0*B + 2)*(1-probabilities[0])*(1-probabilities[1]);
    if(tmp<result)
        result = tmp;

    //strategy 2 back 2
    tmp = (B+3)*(probabilities[0])*(probabilities[1]) +

          (B+3)*(probabilities[0])*(1-probabilities[1]) +

          (B+3)*(1-probabilities[0])*(probabilities[1]) +

          (B+3)*(1-probabilities[0])*(1-probabilities[1]);
    if(tmp<result)
        result = tmp;
}
double A3()
{
    //strategy 1
    tmp = (B-2)*(probabilities[0])*(probabilities[1])*(probabilities[2]) +


          (2.0*B-1)*(probabilities[0])*(1-probabilities[1])*(probabilities[2]) +

          (2.0*B-1)*(1-probabilities[0])*(probabilities[1])*(probabilities[2]) +

          (2.0*B-1)*(probabilities[0])*(probabilities[1])*(1-probabilities[2]) +


          (2.0*B-1)*(probabilities[0])*(1-probabilities[1])*(1-probabilities[2]) +

          (2.0*B-1)*(1-probabilities[0])*(1-probabilities[1])*(probabilities[2]) +

          (2.0*B-1)*(1-probabilities[0])*(probabilities[1])*(1-probabilities[2]) +


          (2.0*B-1)*(1-probabilities[0])*(1-probabilities[1])*(1-probabilities[2]);


    result = tmp;

    //strategy 3
    tmp = B+2;
    if(tmp<result)
        result = tmp;

    //strategy 2 back 1
    tmp = (1+B-1)*(probabilities[0])*(probabilities[1])*(probabilities[2]) +


          (1+B-1)*(probabilities[0])*(probabilities[1])*(1-probabilities[2]) +

          (1+B-1+B+1)*(probabilities[0])*(1-probabilities[1])*(probabilities[2]) +

          (1+B-1+B+1)*(1-probabilities[0])*(probabilities[1])*(probabilities[2]) +


          (1+B-1+B+1)*(probabilities[0])*(1-probabilities[1])*(1-probabilities[2]) +

          (1+B-1+B+1)*(1-probabilities[0])*(probabilities[1])*(1-probabilities[2]) +

          (1+B-1+B+1)*(1-probabilities[0])*(1-probabilities[1])*(probabilities[2]) +


          (1+B-1+B+1)*(1-probabilities[0])*(1-probabilities[1])*(1-probabilities[2]);
    if(tmp<result)
        result = tmp;

    //strategy 2 back 2
    tmp = (2+B-1+1)*(probabilities[0])*(probabilities[1])*(probabilities[2]) +


          (2+B-1+1)*(probabilities[0])*(probabilities[1])*(1-probabilities[2]) +

          (2+B-1+1)*(probabilities[0])*(1-probabilities[1])*(probabilities[2]) +

          (2+B-1+1+B+1)*(1-probabilities[0])*(probabilities[1])*(probabilities[2]) +


          (2+B-1+1)*(probabilities[0])*(1-probabilities[1])*(1-probabilities[2]) +

          (2+B-1+1+B+1)*(1-probabilities[0])*(probabilities[1])*(1-probabilities[2]) +

          (2+B-1+1+B+1)*(1-probabilities[0])*(1-probabilities[1])*(probabilities[2]) +


          (2+B-1+1+B+1)*(1-probabilities[0])*(1-probabilities[1])*(1-probabilities[2]);
    if(tmp<result)
        result = tmp;

    //strategy 2 back 3
    tmp = (3+B+1)*(probabilities[0])*(probabilities[1])*(probabilities[2]) +


          (3+B+1)*(probabilities[0])*(probabilities[1])*(1-probabilities[2]) +

          (3+B+1)*(probabilities[0])*(1-probabilities[1])*(probabilities[2]) +

          (3+B+1)*(1-probabilities[0])*(probabilities[1])*(probabilities[2]) +


          (3+B+1)*(probabilities[0])*(1-probabilities[1])*(1-probabilities[2]) +

          (3+B+1)*(1-probabilities[0])*(probabilities[1])*(1-probabilities[2]) +

          (3+B+1)*(1-probabilities[0])*(1-probabilities[1])*(probabilities[2]) +


          (3+B+1)*(1-probabilities[0])*(1-probabilities[1])*(1-probabilities[2]);
    if(tmp<result)
        result = tmp;
}
void input()
{
    Case++;
    cin >> A >> B;
    probabilities.clear();
    for(i = 0;i<A;++i)
    {
        cin >> singleprob;
        probabilities.push_back(singleprob);
    }
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
    while(T--)
    {
        input();
        if(A==1)A1();
        if(A==2)A2();
        if(A==3)A3();
        printf("Case #%d: %lf\n",Case,result);
    }
	return 0;
}
