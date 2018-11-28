#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
typedef long long ll;

ll gcd(ll a,ll b){
    if(b==0)return a;
    return gcd(b,a%b);
}

ll lcm(ll a,ll b){
    ll r= (a/gcd(a,b))*b;
    //cout<<"lcm("<<a<<","<<b<<") = "<<r<<"\n";
    return r;
}

ll tunes[100000];
ll N,L,H;
ll lcx[10000];
ll gcx[10000];

int solution;

bool solve(ll lc,ll gc){
    //cout<<"solve("<<lc<<","<<gc<<")\n";
    int l = (L+lc-1)/lc;
    int h = H/lc;
    if(gc % lc!=0)return false;
    gc /= lc;

    //bruteforce
    for(ll x=l;x<=h;x++){
        if(gc%x==0){
            solution = x*lc;
            return true;
        }
    }
    
    return false;
}

int main(){
    int cases;
    cin>>cases;

    for(int cas=1;cas<=cases;cas++){
        cin>>N>>L>>H;
        for(int i=0;i<N;i++)
            cin>>tunes[i];
        sort(&tunes[0],&tunes[N]);
        cout<<"Case #"<<cas<<": ";

        int s = lower_bound(&tunes[0],&tunes[N],L)-&tunes[0];
        int e = upper_bound(&tunes[0],&tunes[N],H)-&tunes[0];

        ll lc = 1;
        ll gc = 0;
        for(int i=0;i<s;i++){
            lc = lcm(tunes[i],lc);
        }
        for(int i=e;i<N;i++){
            gc = gcd(gc,tunes[i]);
        }

        bool solved=false;
        if(s!=e){

            ll gcs = gc;
            gcx[e] = gc;
            for(int i=e-1;i>=s;i--){
                gcs = gcd(gcs,tunes[i]);
                gcx[i]=gcs;
            }
            for(int i=s;i<=e;i++){
                if(lc > H)break;
                //cout<<lc<<"\n";
                if(solve(lc,gcx[i])){
                    solved = true;
                    break;
                }
                lc = lcm(lc,tunes[i]);
            }
        }else{
            solved = solve(lc,gc);
        }
        if(!solved){
            cout<<"NO\n";
        }else{
            cout<<solution<<"\n";
        }
    }
}
