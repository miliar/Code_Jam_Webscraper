#include<iostream>
using namespace std;
struct In{
    int num,id;
}p[10000001];
int t[1000001];
long long tot[10000001];
int s[1001];
int main(){
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    int C,R,K,N;
    cin>>C;
    for(int cas=1;cas<=C;cas++){
        scanf("%d%d%d",&R,&K,&N);
        int sum=0;
        for(int i=0;i<N;i++){
            scanf("%d",&p[i].num);
            p[i].id=i;
            sum+=p[i].num;
        }
        for(int i=0;i<1000;i++) s[i]=0;
        if(sum<=K){
            cout<<"Case #"<<cas<<": ";
            cout<<(long long)sum*(long long)R<<endl;
            continue;
        }
        t[0]=0;
        int e=0;
        int n=N;
        int tmp;
        for(int i=0;i<n;i++){
            //cout<<i<<endl;
            //cout<<"te="<<t[e]<<endl;
            if(t[e]+p[i].num>K){
                //cout<<"e="<<e<<" "<<p[i].id-1<<endl;
                if(s[(p[i].id-1+N)%N]!=0){
                    tmp=s[(p[i].id-1+N)%N]-1;
                    //cout<<"over "<<tmp<<endl;
                    break;
                }
                //cout<<t[e]<<endl;
                s[(p[i].id-1+N)%N]=e+1;
                //cout<<"s="<<s[p[i].id-1]<<endl;
                e++;
                //cout<<e<<endl;
                t[e]=p[i].num;
                p[n]=p[i];
                n++;
            }else{
                t[e]+=p[i].num;
                p[n]=p[i];
                n++;
            }
        }//cout<<e<<" "<<tmp<<endl;
        tot[0]=0;
        long long q=0;
        //cout<<tot[0]<<endl;
        if(0>tmp) q+=t[0];
        for(int i=1;i<=e+1;i++){
            tot[i]=tot[i-1]+t[i-1];
            if(i-1>tmp) q+=t[i-1];
            //cout<<tot[i]<<endl;
        }
        //cout<<e<<endl;
        //cout<<q<<endl;
        long long ans;
        tmp+=1;
        //cout<<tmp<<" "<<R<<endl;
        if(R<=tmp){//cout<<ans<<endl;
            ans=tot[R];
            
        }else{
            //cout<<(e+2-tmp)*q<<endl;
            ans=tot[tmp]+(R-tmp)/(e+1-tmp)*q;
            
            if((R-tmp)%(e+1-tmp)!=0){
                //cout<<((R-tmp+1)%(e+2-tmp)+tmp-1)<<endl;
                ans+=tot[((R-tmp)%(e+1-tmp)+tmp)]-tot[tmp];
            }
        }
        cout<<"Case #"<<cas<<": ";
        cout<<ans<<endl;
    }
    return 0;
}
