#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
char A[111],c[30];
int t,n;string s;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    c[0]='y';c[1]='h';c[2]='e';c[3]='s';c[4]='o';c[5]='c';c[6]='v';
    c[7]='x';c[8]='d';c[9]='u';c[10]='i';c[11]='g';c[12]='l';c[13]='b';
    c[14]='k';c[15]='r';c[16]='z';c[17]='t';c[18]='n';c[19]='w';
    c[20]='j';c[21]='p';c[22]='f';c[23]='m';c[24]='a';c[25]='q';
    scanf("%d\n",&t);
    for (int i=1;i<=t;i++){
        gets(A);s=A;n=s.length();
        cout<<"Case #"<<i<<": ";
        for (int i=0;i<n;i++){
            if (s[i]==' ')cout<<" ";
            else cout<<c[s[i]-'a'];}
        cout<<endl;}
    cin>>n;
    return 0;
}
