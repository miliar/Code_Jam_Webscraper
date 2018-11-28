#include<iostream>
using namespace std;
int main()
{
 int i,j,k,ncases;
 char ch='a';
 char input[31][1000],output[31][1000];
 char e[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
 cin>>ncases;
 for(i=0;i<=ncases;i++)
 gets(input[i-1]);
 for(i=0;i<ncases;i++)
 {
        for(j=0;input[i][j]!='\0';j++)
        {
                ch=input[i][j];
                if(isalpha(ch))
                {
                        k=ch;
                        output[i][j]=e[k-97];
                }
                else
                output[i][j]=ch;
        }
        cout<<"\nCase #"<<i+1<<": "<<output[i];
 }
 return 0;
}
 
 
