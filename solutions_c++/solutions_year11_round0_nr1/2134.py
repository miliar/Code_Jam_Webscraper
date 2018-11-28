#include<iostream>
using namespace std;
struct dd{
    char s[10];
    int k;
}a[105];
int n;
int find(dd a[105],int k,int flag){
    int i;
    if(flag==1){ //find O
        for(i=k;i<n;i++)
        if(a[i].s[0]=='O') return i;

    }else if(flag==2){ //find B
        for(i=k;i<n;i++)
        if(a[i].s[0]=='B') return i;
    }
    return -1;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,i,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d",&n);
        for(j=0;j<n;j++) scanf("%s%d",a[j].s,&a[j].k);
        int x=1,y=1,w;
        int ans=0;
        for(j=0;j<n;j++){
            if(a[j].s[0]=='O'){
                ans+=abs(a[j].k-x)+1;
                w=find(a,j+1,2);
                if(w!=-1){
                    if(y<=a[w].k) y=min(y+abs(a[j].k-x)+1,a[w].k);
                    else y=max(y-(abs(a[j].k-x)+1),a[w].k);
                }
                 x=a[j].k;
            }else if(a[j].s[0]=='B'){
                ans+=abs(a[j].k-y)+1;
                w=find(a,j+1,1);
                if(w!=-1){
                   if(x<=a[w].k) x=min(x+abs(a[j].k-y)+1,a[w].k);
                   else x=max(x-(abs(a[j].k-y)+1),a[w].k);
                }
                y=a[j].k;
            }
            //cout<<x<<"~~"<<y<<endl;
           // cout<<ans<<"~~"<<endl;
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
