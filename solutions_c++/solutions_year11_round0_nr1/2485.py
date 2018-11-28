#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define forn(i,j,n)  for(int (i)=(j);(i)<=(n);(i)++)
#define Sort(a) sort(a.begin(),a.end())
#define PB push_back
#define MP make_pair

using namespace std;

vector<int> num;
vector<char> col;
    
int find_next(int in, char ch){
    int len = col.size();
    fir(i,in+1,len){
         if(col[i]==ch) return num[i];
    }
    return -1;
}

int main()
{
    fstream fin,fout;
    fin.open("inp.txt",ios::in);
    fout.open("out.txt",ios::out);
    
    int t,n,no,ans,o,b,x,c=1;
    char ch;
    fin>>t;
    
    while(t--){
        num.clear();
        col.clear();
        ans = 0;
        
        fin>>n;
        
        fir(i,0,n){
            fin>>ch>>no;
            col.push_back(ch);
            num.push_back(no);
        }
        
        o=b=1;
        
        fir(i,0,n){
             if(col[i]=='B'){
                  ans+=abs(b-num[i])+1;
                  x=find_next(i,'O');
                  if(x==-1){
                      b=num[i];
                      continue;
                  }
                  
                  if(abs(o-x) <= abs(b-num[i])+1)
                  o=x;
                  
                  else{
                       if(x>o) o+=abs(b-num[i])+1;
                       else o-=abs(b-num[i])+1;
                  }
                  b=num[i];
             }
             else{
                  ans+=abs(o-num[i])+1;
                  x=find_next(i,'B');
                  if(x==-1) {
                      o=num[i];
                      continue;
                  }
                  
                  if(abs(b-x) <= abs(o-num[i])+1)
                  b=x;
                  
                  else{
                       if(x>b) b+=abs(o-num[i])+1;
                       else b-=abs(o-num[i])+1;
                  }
                  o=num[i];
             }
        }
        
        //cout<<"Case #"<<c++<<": "<<ans<<endl;
        fout<<"Case #"<<c++<<": "<<ans<<endl;
    }
    
    system("pause");
    return 0;
}
