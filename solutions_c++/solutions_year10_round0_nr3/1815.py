#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

long long T,R,k,N,sum,mm;
vector<int> g;
vector<pair<int,int> >pom;

int main(){
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>R>>k>>N;
        g.resize(N);
        mm=0;
        for(int j=0;j<N;j++) {cin>>g[j]; mm+=g[j];}
        if(mm<=k) {
            cout<<"Case #"<<i<<": "<<mm*R<<"\n";
            continue;
        }
        sum=0;
        pom.clear();

        long long p=0,rr=R;
        pom.push_back(make_pair(0,0));
        while(rr){
            long long tsum=0,rpoc=0;
            while(tsum+g[p]<=k) {
                tsum+=g[p];
                ++p;
                if(p==N) p=0;
            }
            sum+=tsum;
            --rr;

            pom.back().second=tsum;

            vector<pair<int,int> >::iterator it = pom.begin();
            while(it!=pom.end() && it->first!=p) ++it;
            if(it!=pom.end()){
                    tsum=rpoc=0;
                    for(vector<pair<int,int> >::iterator itt=it;itt!=pom.end();++itt) {
                        tsum+=itt->second;
                        ++rpoc;
                    }

                    //cout<<tsum<<' '<<rpoc<<endl;

                    sum+= tsum*(rr/rpoc);
                    rr%=rpoc;
                    pom.clear();
            }

            pom.push_back(make_pair(p,0));
        }


        cout<<"Case #"<<i<<": "<<sum<<"\n";
    }
    return 0;
}

