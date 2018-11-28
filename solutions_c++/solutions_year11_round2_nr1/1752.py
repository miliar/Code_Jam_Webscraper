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
#include <iomanip>

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define forn(i,j,n)  for(int (i)=(j);(i)<=(n);(i)++)
#define Sort(a) sort(a.begin(),a.end())
#define PB push_back
#define MP make_pair
#define N 102

using namespace std;

int main()
{
    fstream fin,fout;
    fin.open("inp.txt",ios::in);
    fout.open("out.txt",ios::out);
    
    int cnt=1,t,n,w[N],l[N];
    double oowp[N],ww[N],ll[N],ans[N];
    int w1[N],l1[N];
    string str[N];
    fin>>t;
    
    while(t--){
        fin>>n;
        fir(i,0,n) fin>>str[i];
        
        fir(i,0,n){
            w[i]=0;   
            l[i]=0;    
            fir(j,0,n){
            if(str[i][j]=='1') w[i]++;
            else if(str[i][j]=='0') l[i]++;
            }
        }
        
        int x;
        fir(i,0,n){
           ww[i]=0;
           x=0;    
           fir(j,0,n){
               if(i==j || str[i][j]=='.') continue;
               x++;
               w1[j]=l1[j]=0;
               fir(k,0,n){
                   if(k==i) continue;
                   if(str[j][k]=='1') w1[j]++;
                   else if(str[j][k]=='0') l1[j]++;
               }
               ww[i]+=((double)w1[j]/(double)(w1[j]+l1[j]));
           }
           ww[i]/=x;
        }
        
        fir(i,0,n){
            x=0;
            oowp[i]=0.0;
            fir(j,0,n){
               if(str[i][j]!='.') x++,oowp[i]+=ww[j];
            }
            oowp[i]/=x;
        }
        
        fir(i,0,n){
        ans[i] = 0.25 * ((double)w[i]/(double)(w[i]+l[i])) + 0.25*oowp[i] + 0.5*ww[i];
        }

        fout<<"Case #"<<cnt++<<":"<<endl;
        fir(i,0,n)
        fout<<setprecision(12)<<ans[i]<<endl;
    }
    system("pause");
    return 0;
}
