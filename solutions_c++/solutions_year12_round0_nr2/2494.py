#include <iostream>
#include <map>
#include <cstring>

using namespace std;

int main(){
  int casos;
  cin >> casos;
  for(int i = 1 ; i <= casos ; ++i){
    int n,s,p;
    cin >> n >> s >> p;
    int t[n];
    int v1[n],v2[n],v3[n];
    for(int j = 0 ; j < n ; ++j){
      cin >> t[j];
      v1[j] = v2[j] = v3[j] = t[j] / 3;
      if(t[j] % 3 > 0 ) ++v1[j];
      if(t[j] % 3 > 1 ) ++v2[j];
    }
    int total = 0;
    for(int j = 0 ; j < n ; ++j){
      if (v1[j] >= p){
        ++total;
      }else if( s > 0 && v1[j] == p - 1 && v2[j] > 0 && v1[j] == v2[j]){
        --s;
        ++total;
      }
    }
    cout << "Case #" << i << ": " << total << endl;
  }
}
/*
int main(){
  int casos;
  cin >> casos;
  for(int i = 1 ; i <= casos ; ++i){
    int n,s,p;
    cin >> n >> s >> p;
    int t[n];
    int v[n];
    for(int j = 0 ; j < n ; ++j){
      cin >> t[j];
      v[j] = (t[j] > 0 ? t[j] / 3 + ( t[j] % 3 != 0 ? 1 : 0 ) : 0 );
    }
    int total = 0;
    for(int j = 0 ; j < n ; ++j){
      if( s > 0 && t[j] > 1 && v[j] == p-1){
        --s;
        ++total;
        ++v[j];
      }else if (v[j] >= p){
        ++total;
      }
    }
    cout << "Case #" << i << ": " << total << endl;
  }
}*/