# include <iostream>

using namespace std;

int main () {
  
  long long noofcases, i, j, k, n, A, B, C, D, x0, y0,M;
  long long p,q,r;
  cin>>noofcases;
  long long output[noofcases];
  for(i=0;i<noofcases;i++) {
    cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
    long long x[n], y[n];
    x[0] = x0; 
    y[0] = y0;
    for(j=1;j<=n-1;j++) {
      x[j]=(A*x[j-1] + B)%M;
      y[j]=(C*y[j-1] + D)%M;
    }
    // gets combi of 3 pts and check whether sum is divisible by 3.
    k=0;
    for(p=0;p<n;p++) {
      for(q=p+1; q<n; q++) {
	for(r=q+1; r<n; r++) {
	  // we get p,q,r;
	  if( ((x[p]+x[q]+x[r])%3==0) && ((y[p]+y[q]+y[r])%3==0) ) 
	    k++;
	}
      }
    }
    output[i]=k;
  }
  for(i=0;i<noofcases;i++) 
    cout<<"Case #"<<i+1<<": "<<output[i]<<endl;
  
  return 0;
}
