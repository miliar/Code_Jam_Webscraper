#include <iostream>
#include <vector>

using namespace std;

int
main()
{
  int t;
  long long g[1000];
  cin>>t;

  for(int i = 0; i < t; i++){
    int r,k,n;
    cin>>r>>k>>n;
    for(int j = 0; j < n; j++){
      cin>>g[j];
    }
    
    vector<pair<int,long long> > v(n);
    for(int j = 0; j < n; j++){
      long long a = 0;
      int gn = 0;

      for(int l = j, c = 0; c < n; l++, c++){
	if(l >= n ) l = 0;
	if( a + g[l] > k) break;
	a += g[l];
	gn++;
      }

      v[j].first = (j + gn) % n;
      v[j].second = a;
    }

    long long ans = 0;
    int ng = 0;
    for(int j = 0; j < r; j++){
      ans += v[ng].second;
      ng = v[ng].first;
      //      cout<<v[ng].second<<" "<<ng<<" "<<ans<<endl;
    }

    cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }
}
