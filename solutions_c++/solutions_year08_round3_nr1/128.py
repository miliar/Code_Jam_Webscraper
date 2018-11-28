#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
        int tc;;
        cin>>tc;
        int p,k,l;
        for(int t = 1;t <=tc;t++)
        {
                long long int ret=0;
                cin>>p>>k>>l;
                long long int V[1001];
                for(int i=0;i<l;i++) cin>>V[i];
                sort(V,V+l);
                int m =0;
                int count =0;
                for(int i=l-1;i>=0;i--){
                        if(count%k==0){
                                m++;
                        }
                        count=(count+1)%k;
                        ret+=m*V[i];
                }
                cout<<"Case #"<<t<<": "<<ret<<endl;
        }
        return 0;
}



