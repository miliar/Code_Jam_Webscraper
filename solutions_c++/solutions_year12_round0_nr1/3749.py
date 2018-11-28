#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin>>n;
    char a[5];
    cin.getline(a,2);
    string c="yhesocvxduiglbkrztnwjpfmaq";
    for(int i=0;i<n;i++)
    {
        char s[102];
        cin.getline(s,102);
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;(s[j]<='z' && s[j]>='a') || s[j]==' ';j++)
        {
            if(s[j]!=' ')
                cout<<c[s[j]-'a'];
            else
                cout<<' ';
        }
        cout<<"\n";
    }
}
