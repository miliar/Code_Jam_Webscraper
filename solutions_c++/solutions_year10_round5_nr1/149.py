#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<int> primes;
void pre_calc();
int answer(int d,vector<int> v);
int works(int p,int s,int y,int z,const vector<int>& v);
const int bad=-1;
int MOD;

int main(){
  pre_calc();
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int d,k;
    cin>>d>>k;
    vector<int> v(k);
    for(int j=0;j<k;j++)
      cin>>v[j];
    int a=answer(d,v);
    cout<<"Case #"<<i+1<<": ";
    if(a==bad)
      cout<<"I don't know.\n";
    else
      cout<<a<<'\n';
  }
}

const int N=1000001;
const int D=7;
int composite[N];
int pow10[D];

void pre_calc(){
  pow10[0]=1;
  for(int i=1;i<D;i++)
    pow10[i]=10*pow10[i-1];
  for(int p=2;p<N;p++)
    if(!composite[p])
      for(int k=p+p;k<N;k+=p)
        composite[k]=1;
  for(int p=2;p<N;p++)
    if(!composite[p])
      primes.push_back(p);
}

int answer(int d,vector<int> v){
  if(v.size()==1)
    return bad;
  if(v==vector<int>(v.size(),v.front()))
    return v.front();
  if(v.size()==2)
    return bad;
  const int s=v[0],y=v[1],z=v[2];
  if(y==z){
    vector<int> other(v.size(),y);
    other[0]=s;
    assert(other==v);
    return y;
  }
  const int most=pow10[d];
  int p=0;
  set<int> possibles;
  const int highest=*max_element(v.begin(),v.end());
  while(p<primes.size() && primes[p]<most){
    if(primes[p]>highest){
      int now=works(primes[p],s,y,z,v);
      assert(now<MOD);
      if(now!=bad && possibles.find(now)==possibles.end()){
        //cout<<"now="<<now<<" mod= "<<MOD<<'\n';
        possibles.insert(now);
      }
    }
    p++;
  }
  assert(possibles.size()>=1);
  if(possibles.size()==1)
    return *possibles.begin();
  return bad;
}

inline int add(int a,int b){
  assert(a>=0 && b>=0 && a<MOD && b<MOD);
  return (a+b)%MOD;
}

inline int sub(int a,int b){
  assert(a>=0 && b>=0 && a<MOD && b<MOD);
  return (a-b+MOD)%MOD;
}

inline int mult(int a,int b){
  assert(a>=0 && b>=0 && a<MOD && b<MOD);
  return static_cast<long long>(a)*b%MOD;
}

int next(int a,int b,int s){
  return add(mult(a,s),b);
}

int euclid_invert(int m,int p){
  //cout<<"trying to invert "<<m<<" mod "<<p<<'\n';
  long long a=m,am=1,ap=0;
  long long b=p,bm=0,bp=1;
  while(b){
    assert(am*m+ap*p==a);
    assert(bm*m+bp*p==b);
    int q=a/b,r=a%b;
    assert(r==a-b*q);
    int rm=am-bm*q;
    int rp=ap-bp*q;
    assert(rm*m+rp*p==r);
    a=b; am=bm; ap=bp;
    b=r; bm=rm; bp=rp;
  }
  assert(am*m+ap*p==a);
  assert(a==1);
  return ((am%p)+p)%p;
}


int works(int p,int s,int y,int z,const vector<int>& v){
  //cout<<"trying: "<<p<<'\n';
  MOD=p;
  const int d=sub(y,z),m=sub(s,y);
  const int im=euclid_invert(m,p);
  const int a=mult(d,im);
  const int b=sub(y,mult(a,s));
  assert(next(a,b,s)==y && next(a,b,y)==z);
  for(int i=1;i<v.size();i++)
    if(next(a,b,v[i-1])!=v[i])
      return bad;
  return next(a,b,v.back());
}
