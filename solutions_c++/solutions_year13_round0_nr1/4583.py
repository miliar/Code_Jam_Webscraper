#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int a[4][4],sumr[4],sumc[4],d1,d2;    string s[4];
void read(){
    memset(a,0,sizeof(a));      int i,j;
    for (i=0;i<4;i++){
        cin>>s[i];
        for (j=0;j<4;j++){
            if (s[i][j]=='X')
                a[i][j]=1;
            else{
                if (s[i][j]=='O')
                    a[i][j]=100;
                else{
                    if (s[i][j]=='T')
                        a[i][j]=101;
                }
            }
        }
    }
}
string solution(){
    memset(sumr,0,sizeof(sumr));    memset(sumc,0,sizeof(sumc));
    d1=0;d2=0;int i,j;
    for (i=0;i<4;i++)   for (j=0;j<4;j++){
        sumr[i]+=a[i][j];       sumc[j]+=a[i][j];
        if (i==j)   d1+=a[i][j];
        if ((i+j)==3) d2+=a[i][j];
    }
    if (((d1%100)==4)||((d2%100)==4))
        return "X won";
    if (((d1/100)==4)||((d2/100)==4))
        return "O won";
    for (i=0;i<4;i++){
        if (((sumr[i]%100)==4)||((sumc[i]%100)==4))
            return "X won";
        if (((sumr[i]/100)==4)||((sumc[i]/100)==4))
            return "O won";
    }
    for (i=0;i<4;i++) for (j=0;j<4;j++)
        if (a[i][j]==0)
            return "Game has not completed";
    return "Draw";
}
int main(){
    int ntest,test;
    freopen("A-large.in","r",stdin);    freopen("output.txt","w",stdout);
    cin>>ntest;
    for (test=1;test<=ntest;test++){
        read();
        if (test>1) cout<<endl;
        cout<<"Case #"<<test<<": "<<solution();
    }
    fclose(stdin);          fclose(stdout);
    return 0;
}
