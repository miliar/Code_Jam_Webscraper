#include<iostream>
using namespace std;

int main()
{
    long long T,r,n,g[1100],k,data[1100],time[1100];
    cin >>T;
    for(int i = 1; i<=T;i++)
    {
        cout << "Case #"<<i<<": ";
        cin >> r >> k >> n;
        for(int j =0; j < n;j++){
            cin >> g[j];
            data[j]=-1;
        }
        
        long long p = 0;
        data[0] = 0;
        time[0] = 0;
        long long j = 0,pp;
        long long tt;
        for(;;){
            j++;
            long long temp = 0;
            long long pp = p;
            while(temp+g[p]<=k){
                temp +=g[p];
                p++;
                p%=n;
                if(p==pp)break;
            }
            if(data[p]>=0){
                tt = data[pp]+temp;
                break;
            }
            time[p] = j;
            data[p] = data[pp]+temp;
        }
        r-=time[p];
        long long every = tt-data[p];
        long long ans = (r/(j-time[p]))*every;
        ans += data[p];
        r %=(j-time[p]);
        if(r>0)for(;;){
            long long temp = 0;
            long long pp = p;
            while(temp+g[p]<=k){
                temp +=g[p];
                p++;
                p%=n;
                if(p==pp)break;
            }
            r--;
            ans += temp;
            if(r == 0)break;
            
        }
        cout << ans << endl;
    }
}

        
