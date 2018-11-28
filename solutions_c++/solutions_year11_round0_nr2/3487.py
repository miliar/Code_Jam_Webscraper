#include <iostream>
#include<stdio.h>
#include<string>
#include<cstdlib>
#include<algorithm>
#include<cstring>
using namespace std;
int HE[50][50];
int OP[50][50];
int c,d,n;
int have[50];
string cc,dd,va;
string ans;

bool haveop(){
    for(int i=0;i<ans.length();i++){
        for(int j=0;j<ans.length();j++){
            if(OP[ans[i]-'A'][ans[j]-'A']==1)return 1;
        }
    }
    return 0;
}
string ANS[1000];
int main()
{
    int  t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        memset(HE,-1,sizeof(HE));
        memset(OP,-1,sizeof(OP));
        memset(have,0,sizeof(have));
        cin>>c;
        for(int i=1;i<=c;i++){
            cin>>cc;
            HE[cc[0]-'A'][cc[1]-'A']=cc[2]-'A';
            HE[cc[1]-'A'][cc[0]-'A']=cc[2]-'A';
        }
        cin>>d;
        for(int i=1;i<=d;i++){
            cin>>dd;
            OP[dd[0]-'A'][dd[1]-'A']=1;
            OP[dd[1]-'A'][dd[0]-'A']=1;
        }
        cin>>n;
        cin>>va;
    //    cout<<va<<endl;
        ans.clear();
        for(int i=0;i<n;i++){
            ans+=va[i];
         //   cout<<" "<<va[i]<<endl;
 //           cout<<ans<<endl;
            if(ans.length()<2)continue;
            while(1){
                if(ans.length()<2)break;
                int z1=ans.length();
                int a1=ans[ans.length()-1]-'A';
                int a2=ans[ans.length()-2]-'A';
                if(HE[a1][a2]!=-1){
                    ans.erase(z1-1);
                    z1--;
                    ans.erase(z1-1);
                    z1--;
                    char ff='A'+HE[a1][a2];
                    ans+=ff;
                }
                else{
                    break;
                }
            }
            if(haveop()){
                ans.clear();
            }
        }
        ANS[ca].clear();
        ANS[ca]=ans;
     //   cout<<ans<<endl;
    }
    for(int i=1;i<=t;i++){
        cout<<"Case #"<<i<<": ";
        cout<<"[";
        for(int j=0;j<ANS[i].length();j++){
            if(j>0){
                cout<<", ";
            }
            cout<<ANS[i][j];

        }
        cout<<"]"<<endl;
    }
    return 0;
}
