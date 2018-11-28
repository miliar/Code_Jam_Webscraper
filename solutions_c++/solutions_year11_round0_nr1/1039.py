//kbriut@yahoo.com
//GNU:Ming@Code:Blocks
#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>
using namespace std;
int i,j,n,t,mn,sum,xsum,txt,No,Nb;
#define S 1005
string seq[S];
int val[S];
vector<int>Vo,Vb;
int updateO(int pos,int vpos){
    if(vpos>=No)return pos;
    if(Vo[vpos]==pos)return pos;
    if(Vo[vpos]>pos)return pos+1;
    else return pos-1;
}
int updateB(int pos,int vpos){
    if(vpos>=Nb)return pos;
    if(Vb[vpos]==pos)return pos;
    if(Vb[vpos]>pos)return pos+1;
    else return pos-1;
}
int main(){
    //freopen("1.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        Vo.clear();
        Vb.clear();
        for(i=1;i<=n;i++){
            cin>>seq[i]>>val[i];
            if(seq[i]=="O")Vo.push_back(val[i]);
            else Vb.push_back(val[i]);
        }
        //for(i=1;i<=n;i++)cout<<seq[i]<<" "<<val[i]<<endl;
        int ans=0;
        int pos=1;
        int po=1,pb=1;
        No=Vo.size();
        Nb=Vb.size();
        int posVo=0,posVb=0;

        while(pos<=n){
            if(seq[pos]=="O"){
                if(val[pos]==po)pos++,posVo++;
                else po=updateO(po,posVo);
                pb=updateB(pb,posVb);
            }
            else{
                if(val[pos]==pb)pos++,posVb++;
                else pb=updateB(pb,posVb);
                po=updateO(po,posVo);
            }
            ans++;
        }
        printf("Case #%d: %d\n",++txt,ans);
    }
    return 0;
}
