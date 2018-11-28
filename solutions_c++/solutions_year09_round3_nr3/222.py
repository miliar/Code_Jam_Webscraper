#include <iostream>
#include <vector>
using namespace std;

void opens(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
}

void openb(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
}

#define MAXN 101

int tes,p,num,pos[MAXN],f[(1<<6)];

int doit(int s){
    if (__builtin_popcount(s)==num) return 0;
    //cout<<"Z"<<endl;
    if (f[s]!=-1) return f[s];
    int res=(int)1e9;
    vector<int>v;
    v.push_back(0);
    v.push_back(p+1);
    for (int i=0;i<num;i++){
        if ((s & (1<<i))){
            v.push_back(pos[i]);
        }
    }
    sort(v.begin(),v.end());
    for (int i=0;i<num;i++){
        if ((s & (1<<i))==0){
            int lo=lower_bound(v.begin(),v.end(),pos[i])-v.begin();
            int hi=lower_bound(v.begin(),v.end(),pos[i])-v.begin();
            int left=pos[i]-v[lo-1]-1;
            int right=v[hi]-pos[i]-1;
            //cout<<i<<' '<<left<<' '<<right<<' '<<pos[i]<<endl;
            res=min(res,doit(s|(1<<i))+left+right);
        }
    }
    return f[s]=res;
}

int main(){
    opens();
    //openb();
    scanf("%d",&tes);
    for (int i=1;i<=tes;i++){
        scanf("%d%d",&p,&num);
        for (int j=0;j<num;j++){
            scanf("%d",&pos[j]);
        }
        memset(f,-1,sizeof(f));
        printf("Case #%d: %d\n",i,doit(0));
    }
    //system("pause");
    return 0;
}
