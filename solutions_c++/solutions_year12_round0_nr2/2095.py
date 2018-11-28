#include <iostream>
#include <vector>
using namespace std;

int
judge(int a, int* s, int p){
  //  if( a == 0 ) return 0;

  if( a % 3 == 0 && a/3 >= p ){
    return 1;
  }
  if( (a+1) % 3 == 0 && (a+1)/3 >= p){
    return 1;
  }

  if( a < 1 ) return 0;

  if( (a-1) % 3 == 0 && (a-1)/3+1 >= p){
    return 1;
  }
  
  if( *s>0 && (a+2) % 3 == 0 && (a+2)/3 >= p){
    *s = *s-1;
    return 1;
  }

  if( a < 2 ) return 0;

  if( *s>0 && (a-2) % 3 == 0 && (a-2)/3+2 >= p){
    *s = *s-1;
    return 1;
  }

  if( *s>0 && (a+3) % 3 == 0 && (a+3)/3 >= p){
    *s = *s-1;
    return 1;
  }

  if( a < 3 ) return 0;

  if( *s>0 && (a-3) % 3 == 0 && (a-3)/3+2 >= p){
    *s = *s-1;
    return 1;
  }

  return 0;
}

int
main()
{
  int n; cin>>n;
  for(int i = 0; i < n; i++){
    int n, s, p;
    cin>>n>>s>>p;
    vector<int> v;
    for(int j = 0; j < n; j++){
      int t; cin>>t;
      v.push_back(t);
    }

    int c = 0;
    for(int j = 0; j < v.size(); j++){

      c += judge(v[j], &s, p);
      //      cout<<c<<"j "<<v[j]<<endl;
    }

    cout<<"Case #"<<i+1<<": "<<c<<endl;
    //    cout<<"s "<<s<<endl;

  }
}
