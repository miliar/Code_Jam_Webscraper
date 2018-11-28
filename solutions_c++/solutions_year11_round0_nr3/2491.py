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
    
    int t,ans,sum,n,m,x,c=1;
    fin>>t;
    
    while(t--){
        fin>>n;
        m=INT_MAX;
        sum=ans=0;
        
        while(n--){
             fin>>x;
             m = min(m,x);
             sum+=x;
             ans^=x;
        }
        if(ans!=0)
        fout<<"Case #"<<c++<<": NO"<<endl;
        else
        fout<<"Case #"<<c++<<": "<<sum-m<<endl;
    }
    
    system("pause");
    return 0;
}
