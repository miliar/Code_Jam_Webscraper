#include <iostream>

using namespace std;

int main()
{
  int T, t;
  int N, n;
  int a[1000], b[1000];
  
  cin>>T;  
  for (t=0; t<T; ++t)
  {
    cin>>N;
    
    for (n=0; n<N; ++n)
    {
      cin>>a[n]>>b[n];
    }
    
    int c = 0;
    for (int i=0; i<N; ++i)
      for (int j=i+1; j<N; ++j)
      {
        if ((a[i] > a[j] && b[i] < b[j]) || (a[i] < a[j] && b[i] > b[j]))
          ++c;
      }
  	
    cout<<"Case #"<<t+1<<": "<<c<<endl;
    
  }
  return 0;

}
