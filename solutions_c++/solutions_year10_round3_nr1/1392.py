#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
using namespace std;

int main(){
 long x,y,br;
 int t,n;
 cin>>t;
 for(int tn=1;tn<=t;tn++){
    cin>>n;
    vector<pair<long, long> > pq;
    br=0;
    for(int i=0;i<n;i++){
       cin>>x>>y;
       pq.push_back(make_pair(x,y));
    }
    sort(pq.begin(), pq.end());
    //cout<<" ----- "<<endl;
    for(int i=0;i<n;i++)
      for(int j=i+1;j<n;j++)
        //cout<<pq[i].first<<", "<<pq[i].second<<endl;
        if((pq[i].first<pq[j].first && pq[i].second>pq[j].second) || (pq[i].first>pq[j].first && pq[i].second<pq[j].second))
           br++;
    cout<<"Case #"<<tn<<": "<<br<<endl;
 }
 //system("PAUSE");
 return 0;    
}
