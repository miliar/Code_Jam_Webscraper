#include<iostream>
#include<cstdio>
#include<conio.h>
#include<string.h>
using namespace std;

char c[100]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    char sr[110];
    freopen("input.in","r",stdin);
    freopen("output.out","w+",stdout);
    int t;
    cin>>t;
    int i;
    gets(sr);
    for(i=0;i<t;i++)
    {
                    
                    cout<<"Case #"<<(i+1)<<": ";
    
                    gets(sr);
                    //cout<<strlen(str);
                    int j;
                    for(j=0;j<strlen(sr);j++)
                    {
                                              if(sr[j]!=' ')
                                              sr[j]=c[(sr[j]-97)];
                    }
                    cout<<sr<<endl;
    }
                                            
}
