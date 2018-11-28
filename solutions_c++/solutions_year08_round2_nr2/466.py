#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<int64> vi64;
typedef vector<vi64> vvi64;
typedef vi::iterator vii;
typedef vs::iterator vsi;
typedef vd::iterator vdi;
typedef vi64::iterator vi64i;
typedef vi::reverse_iterator viri;
typedef vs::reverse_iterator vsri;
typedef vd::reverse_iterator vdri;
typedef vi64::reverse_iterator vi64ri;

#define foru(i,a,b) for(int i(a); i<=(b); i++)
#define ford(i,a,b) for(int i(a); i>=(b); i--)
#define repu(i,a,b) for(int i(a); i<(b); i++)
#define repd(i,a,b) for(int i(a); i>(b); i--)
#define foreachu(t,i,v) for(t i=(v.begin()); i<(v.end()); i++)
#define foreachd(t,i,v) for(t i=(v.rbegin()); i>(v.rend()); i++)
#define all(v) v.begin(),v.end()

template<typename T> void vector_remove(vector<T> &v,T i){
    foreachu(typename vector<T>::iterator, ptr, v)
      if(*ptr==i){
        v.erase(ptr);
        break;
      }
}

vi64 primes;

void findprimes(int low, int high){
  bool prime;
  if(low<3&&high<3){
    primes.push_back(2);
    low=3;
  }
  foru(i,low,high){
    prime=true;
    repu(j,2,i)//don't try to optimize
      if(i%j == 0){
        prime=false;
        break;
      }
    if(prime)
      primes.push_back(i);
  }
}

vi64 findprimefactors(int num){                      
  vi64 result;
  foreachu(vi64i, ptr, primes){
    if(*ptr > num)
      break;                
    if(num%*ptr == 0)
      result.push_back(*ptr);
  }
  return result;
}

int main(int argc, char** argv)
{
    int C;
    
    cin >> C;
    foru(X,1,C){
      int A,B,P;
      cin >> A >> B >> P;
      int64 Y = B-A+1;
      vvi64 sets(Y), primefactors(Y);
      primes.clear();
      findprimes(P,B);
      repu(i,0,Y){
        sets[i] = vi64(1,i+A);
        primefactors[i] = findprimefactors(i+A);
      }

      bool end;
      bool repeat;
merge:
      repeat = false;
      repu(i,0,sets.size()){
        if(!sets[i].empty()){
          repu(j,0,sets.size()){
            if(!sets[j].empty() && i!=j){
              end=false;                               
              foreachu(vi64i, ptr1, primefactors[i]){
                foreachu(vi64i, ptr2, primefactors[j]){
                  if(*ptr1 == *ptr2){
                    primefactors[j].erase(ptr2);//automatically duplicate
                    ford(k,sets[j].size()-1,0){
                      sets[i].push_back(sets[j][k]);
                      sets[j].pop_back();
                    }
                    ford(k,primefactors[j].size()-1,0){
                      primefactors[i].push_back(primefactors[j][k]);
                      primefactors[j].pop_back();
                    }
                    end=true;
                    repeat=true;
                    Y--;
                  }
                  if(end)
                    break;
                }
                if(end)
                 break;
              }
            }
          }
        }
      } 
      
      if(repeat)
        goto merge;
        
      cout<<"Case #"<<X<<": "<<Y<<endl;
    }

    return 0;
}
