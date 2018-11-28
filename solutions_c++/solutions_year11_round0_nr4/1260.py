#include <iostream>

using namespace std;

double answer();
double derangement(int n);
double factorial(int n);
double expectation(int n);
double probability(int n,int bads);
double choose(int n,int k);

const int N=1001;

int main(){
  int t;
  cin>>t;
  cout.precision(6);
  cout.setf(ios::fixed|ios::showpoint);
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<answer()<<'\n';
}

double answer(){
  int elements,bads=0;
  cin>>elements;
  for(int i=1;i<=elements;i++){
    int element;
    cin>>element;
    if(element!=i)
      bads++;
  }
  return expectation(bads);
}

double expectation(int n){
  if(n==0)
    return 0;
  double lower=0;
  for(int i=0;i<n;i++)
    lower+=expectation(i)*probability(n,i);
  return (1+lower)/(1-probability(n,n));
}

double probability(int n,int bads){
  return choose(n,bads)*1*derangement(bads)/factorial(n);
}

double derangement(int n){
  static double cache[N];
  static int cached[N];

  double& ret=cache[n];
  if(cached[n]++)
    return ret;
  if(n<2)
    return ret=1-n;
  return ret=(n-1)*(derangement(n-1)+derangement(n-2));
}

double choose(int n,int k){
  static double cache[N][N];
  static int cached[N][N];

  double& ret=cache[n][k];
  assert(k<=n);
  if(cached[n][k]++)
    return ret;
  if(k==0 || k==n)
    return ret=1;
  return ret=choose(n-1,k)+choose(n-1,k-1);
}

double factorial(int n){
  static double cache[N];
  static int cached[N];

  double& ret=cache[n];
  if(cached[n]++)
    return ret;
  if(n<1)
    return ret=1;
  return ret=(n)*factorial(n-1);
}
