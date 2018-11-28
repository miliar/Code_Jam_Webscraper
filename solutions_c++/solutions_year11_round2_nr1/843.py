#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>

#define NAME_VAL(a) cerr<<#a<<" = "<<(a)<<endl;
#define SWAPi(a,b) { int t=a;a=b;b=t; }
#define SWAPd(a,b) { double t=a;a=b;b=t; }
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define FORab(i,a,b) for(i=(a);i<=(b);i++)
#define FOR(i,n) FORab(i,0,(n)-1)
#define FOR1(i,n) FORab(i,1,n)

class fraction
{
public:
int s;
int m;
fraction() { s=0,m=1; }

double todouble() { return (double)s/m; }



void reduce() { int t=gcd(s,m);s/=t;m/=t; }

int gcd(int a,int b)
{
    if(a<b) { int t=a;a=b;b=t; }

    while(b>0)
    {
        int t=b;
        b=a%b;
        a=t;
    }
    return a;
}

void add(int b)
{
    s+=b*m;
    reduce();
}

void add(fraction b)
{
    s=s*b.m+b.s*m;
    m=m*b.m;
    reduce();
}

void divide(int b)
{
    m*=b;
    reduce();
}

};

using namespace std;

void preprocess()
{

}

void main2(int c) {
    int n;
    cin>>n;
    char board[101][101];
    int i,j,k;
    long double wp[101],owp[101],oowp[101],rpi[101];
    int op[101]={};
    FOR(i,n)
    {
        cin>>board[i];
        wp[i]=0.0;
        owp[i]=0.0;
        oowp[i]=0.0;
    }
    FOR(i,n)
    {
        FOR(j,n)
        {
            if(board[i][j]=='1')
            {
                op[i]++;
                wp[i]+=1.0;
            }
            else if(board[i][j]=='0')
            {
                op[i]++;
            }
        }
        wp[i]/=op[i];
    }
    FOR(i,n)
    {
        FOR(j,n)
        {
            if(board[i][j]=='1')
            {
                owp[i]+=wp[j]*op[j]/(op[j]-1.0);
            }
            else if(board[i][j]=='0')
            {
                owp[i]+=(wp[j]*op[j]-1)/(op[j]-1.0);
            }
        }
        owp[i]/=op[i];
    }
    FOR(i,n)
    {
        FOR(j,n)
        {
            if(board[i][j]=='1' || board[i][j]=='0')
            {
                oowp[i]+=owp[j];
            }
        }
        oowp[i]/=op[i];

        rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        cout<<endl<<rpi[i];
    }

    cout<<endl;
}

int main() {
    int c,cases;
    preprocess();
    cin>>cases;
    FOR1(c,cases) {
        cout<<"Case #"<<c<<": ";
        main2(c);
    }
    return 0;
}
