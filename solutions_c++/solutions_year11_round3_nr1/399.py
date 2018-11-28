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

int main()
{
    fstream fin,fout;
    fin.open("inp.txt",ios::in);
    fout.open("out.txt",ios::out);
    
    int t,cnt=1,r,c;
    bool f;
    string arr[100];
    fin>>t;
    
    while(t--){
        fin>>r>>c;
        fir(i,0,r) fin>>arr[i];
        
        f=0;
        fir(i,0,r){
            fir(j,0,c){
                if(arr[i][j]=='#'){
                    if(i+1==r || j+1==c){
                       f=1;
                       break;
                    }
                    
                    if(arr[i+1][j]!='#' || arr[i][j+1]!='#' || arr[i+1][j+1]!='#'){
                       f=1;
                       break;
                    }
                    
                    arr[i][j]='/';
                    arr[i+1][j+1]='/';
                    arr[i+1][j]='\\';
                    arr[i][j+1]='\\';
                }
            }
            if(f) break;
        }
        
        fout<<"Case #"<<cnt++<<":"<<endl;
        if(f)
        fout<<"Impossible"<<endl;
        else{
            fir(i,0,r){
                fout<<arr[i]<<endl;
            }
        }
    }
    system("pause");
    return 0;
}
