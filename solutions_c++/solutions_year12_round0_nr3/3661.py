#include<iostream>
#include<cstdio>
#include<fstream>
#include <math.h>
using namespace std;
int arr[1001][2]={0};
void recycle(int a)
{
    if(a>99)
    {
            arr[a][0]=(a%10)*100+(a/10);
            arr[a][1]=(a%100)*10+(a/100);
    }
    else if(a>9) arr[a][0]=(a%10)*10+(a/10);
}
int main()
{
    int t,a,b,cnt=0;
    fstream f,g;
    for(int i=10;i<1000;i++) recycle(i);
    f.open("C-small-attempt0.in",ios::in);
    g.open("output.out",ios::out);
    f>>t;
    for(int i=1;i<=t;i++)
    {
        f>>a>>b;
        for(int j=a;j<=b;j++)
        {
                if(j < arr[j][0] && arr[j][0]<=b) cnt++;
                if(j < arr[j][1] && arr[j][1]<=b) cnt++;
        }
        g<<"Case #"<<i<<": "<<cnt<<endl;
        cnt=0;
    }
    return 0;
}
