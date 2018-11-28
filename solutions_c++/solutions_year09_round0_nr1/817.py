#include<iostream>
#include<cstring>
using namespace std;
char st[5000+5][15+5];
int l,d,n;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout); 
    
    scanf("%d%d%d",&l,&d,&n);

    int o,i,j,z,ans,flag;
    char now[1000];
    for (i=1;i<=d;i++) scanf("%s",st[i]);
    for (o=1;o<=n;o++){
        scanf("%s",now);
        ans=0;
        for (i=1;i<=d;i++){
            flag=0;z=0;
            for (j=0;j<l;j++){
                if (now[z]==st[i][j]){z++;flag++;continue;} else
                if (now[z]=='('){
                    while (now[z]!=')'){
                        z++;
                        if (now[z]==st[i][j]) flag++;
                    }
                    z++;
                }
                else {flag=0;break;}
            }
         //   cout<<flag<<endl;
            if (flag==l) ans++;
        }
        cout<<"Case #"<<o<<": "<<ans<<endl;
    }
    return 0;
    while (1>0){}
}
