#include <iostream>
#include <vector>
using namespace std;

int delta(int n)
{
  if (n>0) return 1;
  if (n<0) return -1;
  return 0;
}

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int n; cin>>n;
    vector<pair<bool, int> > v;
    for (int i=1; i<=n; i++){
      char c;
      int a;
      cin>>c>>a;
      v.push_back(make_pair(c=='O', a));
    }

    int p1=1, p2=1, turn=0;
    for (int i=0; i<n; turn++){
      int t1=-1, t2=-1;
      if (v[i].first) {
        t1=v[i].second;
        for (int j=i+1; j<n; j++){
          if (!v[j].first){
            t2=v[j].second;
            break;
          }
        }
      }
      else{
        t2=v[i].second;
        for (int j=i+1; j<n; j++){
          if (v[j].first){
            t1=v[j].second;
            break;
          }
        }
      }

      bool inc=false;

      if (t1>=0 && t1!=p1) p1+=delta(t1-p1);
      else if (v[i].first && t1==p1) inc=true;
      else;

      if (t2>=0 && t2!=p2) p2+=delta(t2-p2);
      else if (!v[i].first && t2==p2) inc=true;
      else;

      if (inc) i++;
    }

    cout<<"Case #"<<cn<<": "<<turn<<endl;
  }
  return 0;
}
