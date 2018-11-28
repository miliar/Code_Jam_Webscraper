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

char C[26][26];
bool D[26][26];

int main()
{
    fstream fin,fout;
    fin.open("inp.txt",ios::in);
    fout.open("out.txt",ios::out);
    
    int t,c,d,n,cnt=1;
    int len,rlen;
    string str,res;
    fin>>t;
    
    while(t--){
        fir(i,0,26) fir(j,0,26){
             C[i][j]='.';
             D[i][j]=0;
        }
        fin>>c;        
        while(c--){
             fin>>str;
             C[str[0]-'A'][str[1]-'A']=str[2];
             C[str[1]-'A'][str[0]-'A']=str[2];
        }
        
        fin>>d;
        while(d--){
             fin>>str;
             D[str[0]-'A'][str[1]-'A']=1;
             D[str[1]-'A'][str[0]-'A']=1;
        }
        
        fin>>n;
        fin>>str;
        res=str[0];
        len = str.length();
        
        bool f=0;
        
        fir(i,1,len){
             rlen=res.length()-1;
             f=0;
             if(rlen==-1) {
                 res+=str[i];
                 continue;
             }
             if(C[res[rlen]-'A'][str[i]-'A']!='.'){
                  res[rlen]=C[res[rlen]-'A'][str[i]-'A'];
                  continue;
             }
             
             fir(j,0,rlen+1){
                  if(D[res[j]-'A'][str[i]-'A']==1){
                  res="";
                  f=1;
                  break;
                  }
             }
             
             if(f==0)
             res+=str[i];
        }
        fout<<"Case #"<<cnt++<<": [";
        if(res.size()>0)
        fout<<res[0];
        fir(i,1,res.length())
        fout<<", "<<res[i];
        fout<<"]"<<endl;
    }
    
    system("pause");
    return 0;
}
