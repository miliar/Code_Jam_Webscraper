#include<cstdio>
#include <iostream>
using namespace std;

int main ()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,n;
    char map[27]="yhesocvxduiglbkrztnwjpfmaq",str[30][101];
    cin>>n;
    cin>>j;
    for(i=0;i<n;i++)
    {
    gets(str[i]);
}
for(i=0;i<n;i++)
    {
    j=0;
    while(str[i][j]!='\0')
    {
                       if(str[i][j]!=32)
                       {
                        str[i][j]=map[str[i][j]-97];
                        }
                      
    ++j;
    }
    cout<<"Case #"<<i+1<<": "<<str[i]<<"\n";
    
}
//system("pause");
    return 0;
}
