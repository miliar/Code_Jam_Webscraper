#include <stdio.h>
#include <iostream>
#define WH(a)   while(a)
#define REP(i,a,b)  for(int i = a;i<b;i++)
#define FOR(i,a)    for(int i = 0;i<a;i++)

using namespace std;

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    char a[1000] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char b[1000] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    char code[200];
    int i = 0;
    WH(a[i]!='\0')
    {
        code[a[i]] = b[i];
        i++;
    }
   // REP(i,97,123)   cout<<code[i]<<" ";
    code['z'] = 'q';
    code['q'] = 'z';
    //cout<<"\n";
   // REP(i,97,123)   cout<<code[i]<<" ";
    int t;
    cin>>t;
    char a1 = getchar();
    int caseno = 1;
    FOR(i,t)
    {
        cout<<"Case #"<<caseno<<": ";
        caseno++;
        char c [1001];
        gets(c);
        int j = 0;
        WH(c[j]!='\0')
        {
            cout<<code[c[j]];
            j++;
        }
        cout<<"\n";
    }
    return 0;
}
