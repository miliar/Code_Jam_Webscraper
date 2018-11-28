#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>

using namespace std;


char M[] = "yhesocvxduiglbkrztnwjpfmaq";
char in[120];
int main()
{
    freopen("A.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,cas,n,cn;
    cin >> cas;
    getchar();
    for(cn = 1;cn<=cas;cn++)
    {
        gets(in);
        cout << "Case #"<< cn << ": ";
        n = strlen(in);
        for(i=0;i<n;i++)
        if(in[i] == ' ') cout << ' ';
        else cout << M[in[i] - 'a'];
        cout << endl;
    }
    return 0;
}
