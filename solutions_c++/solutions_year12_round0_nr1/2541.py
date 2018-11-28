#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <string>
#define eps 1e-9
#define inf 0x7fffffff
#define N 1005
using namespace std;
int a[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int main()
{
    int n,i,j,m;
    cin>>n;
    getchar();
    char b[109];
    for (i=0;i<n;i++){
        gets(b);
        cout<<"Case #"<<i+1<<": ";
        for (j=0;b[j];j++)
            if (b[j]>='a'&&b[j]<='z')cout<<(char)(a[b[j]-'a']+'a');
            else cout<<b[j];
        cout<<endl;
        }
    return 0;
}
