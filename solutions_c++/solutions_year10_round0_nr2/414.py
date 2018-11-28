#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cmath>

using namespace std;

ifstream fin("B-small.in");
ofstream fout("B-small.out");
int n,N;
//int t[1001];
int a,b,c;

int gcd(int a, int b)
{
    if (a<b) {int tmp=a;a=b;b=tmp;}
 int r = 1;
 while(r != 0) {
  r = a % b;
  a = b;
  b = r;
 }
 return a;
}

int main()
{
    fin>>N;
    int tmp=N,res,s,tmp1,tmp2;
    while (N!=0){
        fin>>n;
        if (n==2) {fin>>a>>b;s=fabs(a-b);}
        else {
            fin>>a>>b>>c;
            tmp1=fabs(a-b);
            tmp2=fabs(b-c);
            if (tmp1==0) s=tmp2;
            else if (tmp2==0) s=tmp1;
            else s=gcd(tmp1,tmp2);
        }
        if ((a%s)!=0)
        res=s-(a%s);
        else res=0;
        fout<<"Case #"<<tmp-N+1<<": "<<res<<endl;
        N--;
    }
    return 0;
}
