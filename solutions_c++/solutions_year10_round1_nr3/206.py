#include <iostream>

using namespace std;

int solve(int a,int aa,int b,int bb);
bool winning(int a,int b);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int a,aa,b,bb;
    cin>>a>>aa>>b>>bb;
    assert(a<=aa);
    assert(aa-a<=30);
    assert(b<=bb);
    assert(bb-b<=30);
    cout<<"Case #"<<i+1<<": "<<solve(a,aa,b,bb)<<'\n';
  }
}

int solve(int a,int aa,int b,int bb){
  int ret=0;
  for(int i=a;i<=aa;i++)
    for(int j=b;j<=bb;j++)
      ret+=winning(i,j);
  return ret;
}

bool winning(int a,int b){
  if(a==b) return false;
  if(a<b) swap(a,b);

  assert(a>b);
  assert(2*b<=a || a%b>0);

  if(a%b==0) return true;
  const int max_k=a/b;
  assert(max_k>=1);
  const bool max_k_works=!winning(b,a-max_k*b);
  if(max_k==1)
    return max_k_works;

  return true;
}
