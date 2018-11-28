#include <iostream>
#include <string>
#include <cmath>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
int value[500];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        memset(value,-1,sizeof(value));
        string str;
        cin>>str;
        value[str[0]]=1;
        int start=0;
        for(int i=0;i<str.size();i++) {
                if(value[str[i]]==-1){
                        if(start==1)start++;
                        value[str[i]]=start++;

                }


        }


        typedef long long LL;
        LL sum=0;
        LL b=0;
        for(int i=0;i<str.size();i++) {
            LL digit=0;
            digit=value[str[i]];
            b=max(b,digit);
        }
        b++;
        for(int i=0;i<str.size();i++) {
            LL digit=0;
            //if(isdigit(str[i])) digit=str[i]-'0';
             digit=value[str[i]];
          //  b=max(b,digit);
            //cout<<digit;
            sum=sum*b+digit;
        }
        cout<<"Case #"<<t<<": "<<sum<<endl;

    }
    return 0;
}

