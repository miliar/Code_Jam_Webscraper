#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> V;
int P,L,K;

int main(){
 int Ntc;
 cin>>Ntc;
 for(int tc=1;tc<=Ntc;tc++)
  {
   V.clear();
   cin>>P;cin>>K;cin>>L;
   long long t;
   for(int i=0;i<L;i++)
   { cin>>t;V.push_back(t);}
    sort(V.begin(),V.end());
    int p=1;int k=1;
    if(L>P*K){
     cout<<"Case #"<<tc<<": IMPOSSIBLEs";
     cout<<"\n";
		}else{
         long long res=0;
			for(int i=L-1;i>=0;i--){
                res+=V[i]*p;
                k++;
                if(k==K+1){k=1;p++;};
			}
     		cout<<"Case #"<<tc<<": "<<res;
     		cout<<"\n";
       }
  }
}
