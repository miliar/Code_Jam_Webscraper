#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int a[1000006];
struct node{
    int id,vis;
    long long dis;
    long long ndis;
}e[1000006];
long long sum[1000006];

int cmp(node x,node y){
    return  x.ndis>y.ndis;
}

int cmp1(node x,node y){
    return x.id<y.id;
}

int main(){
    int T;
    int l,n,c,k;
    long long s;
    long long t;
    freopen ("B-large.in","r",stdin);
    freopen ("Bl.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        
        cin>>l>>t>>n>>c;
     //   cout<<l<<" "<<t<<" "<<n<<" "<<c<<endl;
        for(int i=0;i<c;i++){
            cin>>s;
            for(k=0;;k++){
                if(k*c+1>n)break;
                else {
                    e[k*c+i].dis=s;
                    e[k*c+i].id=k*c+i;
                }
            }
        } 
        
        for(int i=0;i<n;i++){
           e[i].vis=0;
        }
        
        sum[0]=0; //之前做没意义 
//        int ans;
        int i;
        int flag=0;
        for(i=1;i<=n;i++){
            sum[i]=e[i-1].dis+sum[i-1];
            if(sum[i]*2>t){
                e[i-1].ndis=sum[i]-t/2;
                for(i++;i<n+1;i++){
                    e[i-1].ndis=e[i-1].dis;
                }
                flag=1;
                
            }
            else {
                e[i-1].ndis=0;
            }
        }
        if(flag==0){
            cout<<"Case #"<<cas<<": "<<sum[n]*2<<endl;
            continue;
        }
        
            
        /*        for(int i=0;i<n;i++)
            cout<<e[i].ndis<<" ";
        cout<<endl;
 
        */
        sort(e,e+n,cmp);

        
        i=0;
        while(l--&&i<n){
            e[i].vis=1;
            i++;
        }
        sort(e,e+n,cmp1);
        i=0;
        while(e[i].ndis==0)i++;
        /* for(;i<n;i++)
            cout<<e[i].ndis<<" "<<e[i].vis<<endl;
         cout<<endl; 
         */
        for(;i<n;i++){
            if(e[i].vis){
                t+=e[i].ndis;
            }
            else t+=e[i].ndis*2;
        }
        cout<<"Case #"<<cas<<": "<<t<<endl;
       // printf("Case #%d: %d\n",cas,t);
    }
}

        
