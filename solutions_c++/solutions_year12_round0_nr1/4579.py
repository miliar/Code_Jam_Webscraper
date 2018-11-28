#include<iostream>
#include<string>
using namespace std;
int main()
{   string b;
int n,k=1,i;
cin>>n;
getline(cin,b);
while(n--)
{
    char a[]="yhesocvxduiglbkrztnwjpfmaq";
    getline(cin,b);
    cout<<"Case #"<<k<<": ";
    for(i=0;b[i];i++)
    {
                     if(b[i]==' ')
                     cout<<b[i];
                     else
                     {
                         cout<<a[(int)(b[i]-97)];
                     }
                         
    }
    cout<<endl;
    
}
}
