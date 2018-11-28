#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; ++cn) {
    int n; cin>>n;
    vector<int> v(n);
    for (int i=0; i<n; i++) cin>>v[i];
    sort(v.begin(), v.end());

    int sum=0;
    vector<int> ke(31);
    for (int i=0; i<n; i++){
      for (int j=0; j<31; j++)
        if (v[i]&(1<<j))
          ke[j]++;
      sum+=v[i];
    }

    bool ok=true;
    for (int i=0; i<31; i++)
      if (ke[i]%2!=0)
        ok=false;

    cout<<"Case #"<<cn<<": ";

    if (!ok)
      cout<<"NO"<<endl;
    else
      cout<<(sum-v[0])<<endl;    
  }
  return 0;
}
