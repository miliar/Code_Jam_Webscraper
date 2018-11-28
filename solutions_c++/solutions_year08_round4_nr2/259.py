#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

double PI =  3.14159265358979323846;
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

int main() {
    int cases;
    cin>>cases;
    for (int tt=0;tt<cases;tt++) {
          int px,py,n,m,area;
          cin>>n>>m>>area;
          bool found =false;
          for (int x1=0;x1<=n&&!found;x1++)  
          for (int y1=0;y1<=m&&!found;y1++)
          for (int x2=x1;x2<=n&&!found;x2++)
          for (int y2=0;y2<=m&&!found;y2++) {
              px=x2-x1;py=y2-y1;
              int obsah=abs(x1*py-y1*px);
              if (obsah==area) {
                 found=true;                 
              cout<<"Case #"<<tt+1<<": "<<"0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
              }
          }
          if (!found) cout<<"Case #"<<tt+1<<": IMPOSSIBLE"<<endl;
    }
}
