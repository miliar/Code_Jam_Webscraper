#include <string>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>


using namespace std;

string s,fans="yhesocvxduiglbkrztnwjpfmaq";
int i,n,L,j;
stringstream ss;

int main()
{
    freopen("Speaking in Tongues.in" , "r" , stdin);
    freopen("Speaking in Tongues.out" , "w" , stdout);
    getline (cin,s);
    ss << s;
    ss >> n;
    for (i=1; i<=n; i++)
    {
        cout << "Case #" << i << ": ";
        getline (cin,s);
        L=s.size();
        for (j=0; j<L; j++)
            if (s[j]!=' ')cout << fans[s[j]-'a'];else cout << " ";
        cout << endl;
    }
}
