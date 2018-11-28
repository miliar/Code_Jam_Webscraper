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

//double PI =  3.14159265358979323846;
#define dd long double
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

int main() {
    int cases;
    cin>>cases;
    for (int tt=1;tt<=cases;tt++) {
        vector<VI> a=vector<VI>(105,VI(105,0));
        vector<VI> b=vector<VI>(105,VI(105,0));
        
        int h,w,r;
        cin>>h>>w>>r;h++;w++;
        for (int i=0;i<r;i++) {
            int q,w;cin>>q>>w;
            b[q+1][w+1]=1;
        }
        a[2][2]=1;
        for (int i=2;i<=h;i++) for (int j=2;j<=w;j++) if (i!=2||j!=2) {
            if (b[i][j]==1) a[i][j]=0;
            else a[i][j]=(a[i-1][j-2]+a[i-2][j-1])%10007;
        }
        cout<<"Case #"<<tt<<": "<<a[h][w]<<endl;

    }
}
