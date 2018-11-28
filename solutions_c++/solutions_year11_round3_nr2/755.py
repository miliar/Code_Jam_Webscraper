#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;
typedef vector<ll> vi;

int main() {
  int ncases;
  cin>>ncases;
  for (int nc=1;nc<=ncases;++nc) {
    cout<<"Case #"<<nc<<": ";
    ll l,t,n,c,sum=0;
    cin>>l>>t>>n>>c;
    vi dist(c);
    for (int i=0;i<c;++i) {
      cin>>dist[i];
      sum+=dist[i];
    }
    ll totaltime=(n/c)*sum;
    for (int i=0;i<n%c;++i) totaltime+=dist[i];
    totaltime*=2;
    if (l==0) cout<<totaltime<<endl;
    else {
      ll min=totaltime;
      for (int i=0;i<=n-l;++i) {
        ll time=totaltime,arrival=(i/c)*sum;
        for (int j=0;j<i%c;++j) arrival+=dist[j];
        arrival*=2;
        ll nextarr=arrival+2*dist[i%c];
        if (arrival>=t) time-=dist[i%c];
        else if (nextarr>t) time-=(nextarr-t)/2;
        if (l==1) {
          if (time<min) min=time;
        } else {
          for (int j=i+1;j<n;++j) {
            ll time2=time,arrival2=(j/c)*sum;
            for (int k=0;k<j%c;++k) arrival2+=dist[k];
            arrival2*=2;
            arrival2+=(time-totaltime);
            ll nextarr2=arrival2+2*dist[j%c];
            if (arrival2>=t) time2-=dist[j%c];
            else if (nextarr2>t) time2-=(nextarr2-t)/2;
            if (time2<min) min=time2;
          }
        }
      }
      cout<<min<<endl;
    }
  }
}
