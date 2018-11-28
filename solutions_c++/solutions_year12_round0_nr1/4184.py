#include<iostream>
#include<string>
using namespace std;
int main()
{
    //freopen("it.txt","r",stdin);
    //freopen("ot.txt","w",stdout);
    string op="yhesocvxduiglbkrztnwjpfmaq",a;
    int t,i,j;
    while(cin>>t)
    {
                 getchar();
                 j=1;
                 while(j<=t)
                 {
                           getline(cin,a);
                           cout<<"Case #"<<j<<": ";
                           for(i=0;i<a.length();++i)
                           {
                                                    if(a[i]==' ')
                                                    cout<<' ';
                                                    else
                                                    cout<<op[((int)a[i])-97];
                           }
                           ++j;
                           cout<<endl;
                 }
    }
    return 0;
}
