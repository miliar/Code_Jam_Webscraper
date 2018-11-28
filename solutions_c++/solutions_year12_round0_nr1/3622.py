#include<iostream>
#include<cstdio>
using namespace std;
char s[27]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
//    freopen("/home/wxf/A-small-attempt2.in","r",stdin);
//    freopen("/home/wxf/A-small-attempt2.out","w",stdout);
    int t,cas=1;
    char w[200];
    cin>>t;cin.getline(w,200);
    while(t--)
    {
        cin.getline(w,200);
        cout<<"Case #"<<cas++<<": ";
        for(int i=0;w[i];i++)
        {
            if(w[i]==' ') cout<<" ";
            else cout<<s[w[i]-97];
        }
        cout<<endl;
    }
    return 0;
}
