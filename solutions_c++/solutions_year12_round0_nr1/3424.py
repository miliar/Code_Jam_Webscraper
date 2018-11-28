#include<iostream>
#include<cstdio>
#include<conio.h>
#include<string.h>
using namespace std;

char conv[100]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    char str[110];
    //cout<<strlen(conv);
    freopen("input.in","r",stdin);
    freopen("output.out","w+",stdout);
    int t;
    cin>>t;
    int i;
    gets(str);
    for(i=0;i<t;i++)
    {
                    
                    cout<<"Case #"<<(i+1)<<": ";
    
                    gets(str);
                    //cout<<strlen(str);
                    int j;
                    for(j=0;j<strlen(str);j++)
                    {
                                              if(str[j]!=' ')
                                              str[j]=conv[(str[j]-97)];
                    }
                    cout<<str<<endl;
    }
                                            
    //getch();
}
