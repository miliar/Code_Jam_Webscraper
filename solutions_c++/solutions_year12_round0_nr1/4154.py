#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    //freopen("speaking.in","r",stdin);
   // freopen("speaking.out","w",stdout);
    char dict[30]="yhesocvxduiglbkrztnwjpfmaq";
    int n;
    cin>>n;
    char x=getchar();
    for (int tt=1;tt<=n;++tt)
        {
             char c;
             cout<<"Case #"<<tt<<": ";
             while ((c=getchar())!='\n')
                   if (c==' ') cout<<" ";
                   else cout<<dict[c-'a'];
             cout<<endl;
         }
}
