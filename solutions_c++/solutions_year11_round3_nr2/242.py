#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;


long long t;
int N;
int L;
int C;
long long dist[2000000];

int main(){
    int cases;
    cin>>cases;
    for(int cas=1;cas<=cases;cas++){
        cin>>L>>t>>N>>C;
        vector<long long> a(C);
        //memset(dist,0,sizeof(dist));
        for(int i=0;i<C;i++)
            cin>>a[i];
        for(int i=0;i<N;i++)
            dist[i]=a[i%C];
        
        int start;
        long long sum=0;
        long long speedup=0;
        for(int i=0;i<N;i++){
            sum+=dist[i]*2;
            if(sum>=t){
                start = i;
                speedup = (sum-t)/2;
                break;
            }
        }
        sum=0;
        for(int i=0;i<N;i++){
            sum+=dist[i]*2;
        }

        vector<int> cp(&dist[start+1],&dist[N]);
        long long saving=0;
        if(L!=0){
            if(L <= cp.size()){
                sort(cp.rbegin(),cp.rend());
                for(int i=0;i<L-1;i++){
                    saving+=cp.at(i);
                }
                if(speedup > cp.at(L-1))
                    saving += speedup;
                else
                    saving += cp.at(L-1);
            }else{
                sort(cp.rbegin(),cp.rend());
                for(int i=0;i<cp.size();i++){
                    saving+=cp.at(i);
                }
                saving+=speedup;
            }
        }
        cout<<"Case #"<<cas<<": "<<(sum-saving)<<"\n";
    }
}
