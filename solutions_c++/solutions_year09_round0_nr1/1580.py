#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <functional>
#include <iterator>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <cassert>
#include <list>

using namespace std;

#define FOR(i, l, u) for(int (i)=(l); (i) < (u); ++(i))
#define FORD(i, u, l) for(int (i) = (u); (i) >= (l); --(i))
#define SHIFTL(i,n) ((i) << (n))
#define SHIFTR(i,n) ((i) >> (n))
#define POW2(n) SHIFTL(1, n)

typedef vector<int> v_int;
typedef vector<string> v_string;
typedef map<string, int> map_s;
typedef set<string> set_s;
typedef set<int> set_i;
typedef pair<int,int> pair_i;

int process(string a, set_s y){
     set_s x=y;
     set_s temp;
     set_s :: iterator iter;
     for(int i=0,n=0;i<a.length();i++,n++){
             if(a[i]=='('){
                      do{
                         i++;
                         for(iter=x.begin();iter!=x.end();iter++){
                                                           if((*iter)[n]==a[i])
                                                                             temp.insert(*iter);
                         }
                      }while(a[i]!=')');     
             }
             else{
                  for(iter=x.begin();iter!=x.end();iter++){
                                                           if((*iter)[n]==a[i])
                                                                             temp.insert(*iter);
                  }
             }
             x = temp;
             temp.clear();
     }
     return x.size();
}


int main() {
	int L,D,N;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
    fin>>L>>D>>N;
    string x;
    set_s mset;
    for(int i=0;i<D;i++){
            fin>>x;
            mset.insert(x);    
    }
    cout<<mset.size()<<endl;
    for(int i=0;i<N;i++){
            fin>>x;
            fout<<"Case #"<<i+1<<": "<<process(x,mset)<<endl;
    }
	return 0;
}
