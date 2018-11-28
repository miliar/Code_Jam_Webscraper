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
#define N 1000003

using namespace std;

    int arr[N];
    int C[N];
    
int main()
{
    fstream fin,fout;
    fin.open("inp.txt",ios::in);
    fout.open("out.txt",ios::out);
    long long t,cnt=1,tim;
    long long c,n,tt,l;

    fin>>t;
    while(t--){
       fin>>l>>tt>>n>>c;
       fir(i,0,c){
           fin>>C[i];
       }
       
       long x=0;
       fir(i,0,n){
          arr[i]=C[x%c];
          x++;
       }
       
       tim=0;
       long long curr=0;
       while(tim<tt){
           if( ((arr[curr]*2)+tim)<tt){
           tim+=arr[curr]*2;
           curr++;
           }
           else{
              arr[curr]-=(tt-tim)/2;
              tim=tt;
              break;
           }
           if(curr==n)break;
       }
       
       if(curr==n){
                   fout<<"Case #"<<cnt++<<": "<<tim<<endl;
       continue;
       }
       
       sort(arr+curr,arr+n);
       
       for(int i=n-1;i>=curr;i--)
       {
           if(l>0){
           tim+=arr[i];
           l--;
           }
           else
           tim+=(2*arr[i]);
       }
       
       fout<<"Case #"<<cnt++<<": "<<tim<<endl;
    }
    system("pause");
    return 0;
}

