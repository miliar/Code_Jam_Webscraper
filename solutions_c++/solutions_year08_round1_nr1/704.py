#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vi::iterator vii;
typedef vs::iterator vsi;
typedef vd::iterator vdi;
typedef vi::reverse_iterator viri;
typedef vs::reverse_iterator vsri;
typedef vd::reverse_iterator vdri;

#define foru(i,a,b) for(int i(a); i<=(b); i++)
#define ford(i,a,b) for(int i(a); i>=(b); i--)
#define repu(i,a,b) for(int i(a); i<(b); i++)
#define repd(i,a,b) for(int i(a); i>(b); i--)
#define foreachu(t,i,v) for(t i=(v.begin()); i<(v.end()); i++)
#define foreachd(t,i,v) for(t i=(v.rbegin()); i<(v.rend()); i++)
#define all(v) v.begin(),v.end()

template<typename T> void vector_remove(vector<T> &v,T i){
    foreachu(typename vector<T>::iterator, ptr, v)
      if(*ptr==i){
        v.erase(ptr);
        break;
      }
}

int main(int argc, char** argv)
{
    int T;
    
    cin >> T;
    foru(X,1,T){
      int n,Y=0;
      cin >> n;
      vi x(n), y(n);
      repu(i,0,n)
        cin >> x[i];
      repu(i,0,n)
        cin >> y[i];
        
      sort(all(x));
      sort(all(y));
      repu(i,0,n)
        Y += x[i] * y[n-i-1];

      cout<<"Case #"<<X<<": "<<Y<<endl;
    }

    return 0;
}
