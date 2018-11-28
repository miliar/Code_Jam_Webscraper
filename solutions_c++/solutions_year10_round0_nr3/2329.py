#include <iostream>
#include <vector>
using namespace std;


long long anadir(vector< pair<long long,long long> >& perm, pair<long long,long long>& aux){
    for(long long i=0;i<perm.size();++i)
        if(perm[i].first==aux.first and perm[i].second == aux.second)return i;
    perm.push_back(aux);
    return -1;
}

int main(){
    long long T;
    cin>>T;
    for(long long i=1;i<=T;++i){
        long long R,k,N;
        cin>>R>>k>>N;
        vector<long long> v(N);
        vector<pair<long long,long long> > perm(0);
        vector<long long> guanys(0);
        for(long long j=0;j<N;++j){
            cin>>v[j];
        }
        long long fi=0;
        long long j;
        long long repetit = -1;
        long long total = 0;
        
        for(j=0;j<R and repetit<0;++j){
            long long suma=0;
            long long cont = fi;
            bool ini = false;
            while((not ini or cont!=fi) and suma+v[cont]<=k){
                suma+=v[cont];
                total+=v[cont];
                ++cont;
                cont%=N;
                ini = true;
            }
            
            pair<long long,long long> aux = pair<long long,long long> (fi,cont);
            repetit = anadir(perm,aux);
            if(repetit<0)guanys.push_back(total);
            fi = cont;
        }
        cout<<"Case #"<<i<<": ";
        if(repetit<0){
            cout<<guanys[guanys.size()-1]<<endl;
        }
        else{
            --j;
           // cerr<<"rep "<<repetit<<endl;
            long long cicle = j-repetit;
           // cerr<<"j "<<j<<endl;
            long long g;
            if(repetit==0)g=0;
            else g = guanys[repetit-1];
            long long g2;
            if(repetit+(R-repetit)%cicle==0)g2=0;
            else g2 = guanys[repetit-1+(R-repetit)%cicle];
            long long sol1 = g;
            long long sol2 = (guanys[j-1]-g)*((R-repetit)/cicle);
            long long sol3 = g2-g;
            //cerr<<sol1<<" "<<sol2<<" "<<sol3<<endl;
            cout<<sol1+sol2+sol3<<endl;
        }
        
    }
}