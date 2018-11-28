#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;

char table[20000001];
int main()
{
    freopen("x.in","r",stdin);
    freopen("x.out","w",stdout);
    int t,a,b,tmp,la,lb,lk;
    char str[200],tstr[100],astr[100],bstr[100];
    cin>>t;
    for(int i = 1;i<=t;i++){
        cin>>a>>b;
        la = sprintf(astr,"%d",a);
        lb = sprintf(bstr,"%d",b);
        long long ret = 0;
        memset(table,0,sizeof(table));
        for(int k = a;k<=b;k++){
            if(table[k] == 1)
              continue;
            str[0]='\0';
            lk = sprintf(tstr,"%d",k);
            strcat(str,tstr);
            strcat(str+lk,tstr);

            char ch;
            long long cur = 0;
            for(int j = 0;j<lk;j++){
                if(str[j] == '0')
                   continue;
                ch = str[j+lk];
                str[j+lk] ='\0';
                tmp = atoi(str+j);
                if(la == lk)
                {
                    if(table[tmp]==0 && tmp >= a && tmp <= b){
                        table[tmp] = 1;
                        cur++;
                    }
                }
                else if(lb <= lk){
                    if(table[tmp]==0 && tmp <= b){
                        table[tmp] = 1;
                        cur++;
                    }

                }
                str[j+lk] = ch;

            }
            ret+= cur*(cur-1)/2;
        }
        cout<<"Case #"<<i<<": "<<ret<<endl;
    }

 //   cout << "Hello world!" << endl;
    return 0;
}
