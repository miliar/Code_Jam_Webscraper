#include<iostream>
#include<stdio.h>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;
const int maxn=100000;
int pre[maxn];
int PO[maxn][2];
int T[maxn];
int n;
int main()
{
    int ca;
    cin>>ca;
    for(int caa=1;caa<=ca;caa++){
    cin>>n;
    char s[2],a;
    int t1=0,t2=0;
    for(int i=1;i<=n;i++){
        scanf("%s%d",s,&PO[i][1]);
    //    cout<<s[0]<<endl;
        if(s[0]=='O'){
            PO[i][0]=1;
            pre[i]=t1;
            t1=i;
        }
        else{
            PO[i][0]=2;
            pre[i]=t2;
            t2=i;
        }
    }
    int tt=0;
    int Onow=1;
    int Bnow=1;
    T[0]=0;
    //for(int i=1;i<=n;i++)cout<<PO[i][0]<<" "<<PO[i][1] <<endl;
    for(int i=1;i<=n;i++){
        if(PO[i][0]==1){
             T[i]=max(T[i-1]+1,T[pre[i]]+abs(PO[i][1]-Onow)+1);

             Onow=PO[i][1];
             //cout<<"i: "<<i<<"  "<<T[i]<<" po : "<<Onow<<endl;

        }else{
            T[i]=max(T[i-1]+1,T[pre[i]]+abs(PO[i][1]-Bnow)+1);
            Bnow=PO[i][1];
            //cout<<"i: "<<i<<"  "<<T[i]<<" po : "<<Bnow<<endl;
                    }

    }
    cout<<"Case #"<<caa<<": "<<T[n]<<endl;

    }
    return 0;
}
