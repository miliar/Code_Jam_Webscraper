#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <stack>
#include<cctype>
#include<map>
#include<set>
#include<stdio.h>
using namespace std;

#define ABS(x) ((x)<0?-(x):x)
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
string intToStr(int num)
{
    string out;
    if(num == 0)
    return "0";
    while(num>0)
    {
        char ch = (char)(48 + num%10);
        out = ch+out;
        num  /= 10;
    }
    return out;
}

int main()
{
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("out.out", "wt", stdout);
    int t;
    cin>>t;
    int out=0,a,b,temp;
    string s;
    for(int i=0;i<t;i++)///////////////////////// Test Cases
    {
        out = 0;
        cin>>a;
        cin>>b;
        for(int j=a;j<=b;j++)//////////////////////// Range
        {

            temp = j;
            s=intToStr(temp);

            for(int k=0;k<s.size();k++)////////////////////////// Rotation
            {
                int x = temp%10;
                temp /= 10;
                int y =s.size()-1;
                while(y--)////////////// New
                {
                    x *= 10;
                }
                x += temp;
                if(x>=a && x<=b && x>j)
                {
                    out++;
                }

                temp = x;
            }
        }
        cout<<"Case #"<<i+1<<": "<<out<<endl;
    }
	return 0;
}
