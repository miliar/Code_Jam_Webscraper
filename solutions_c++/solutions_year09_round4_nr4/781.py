#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

#define X second
#define Y first

using namespace std;

typedef pair<int,int> PII;
typedef pair<PII,int> PPIII;

double min(double a, double b){ return (a<b?a:b); }

double max(double a, double b){ return (a>b?a:b); }

double dist(PII a, PII b){
    return sqrt((double)((a.X-b.X)*(a.X-b.X) + (a.Y-b.Y)*(a.Y-b.Y)));
}

int main(){
    int ncases;
    cin >> ncases;
    for(int x=1;x<=ncases;x++){
        vector<PPIII> flowers (3);
        
        int n;
        cin >> n;
        
        for(int i=0;i<n;i++){
            cin >> flowers[i].first.X >> flowers[i].first.Y >> flowers[i].second;
        }
        
        
        cout << "Case #" << x << ": ";
        if(n==1) cout << flowers[0].second;
        else if(n==2) cout << max(flowers[0].second,flowers[1].second);
        else {
            double ans = max(flowers[0].second, ((double)(dist(flowers[1].first,flowers[2].first) + flowers[1].second + flowers[2].second))/(double)2.0);
            ans = min(ans,max(flowers[1].second, ((double)(dist(flowers[0].first,flowers[2].first) + flowers[0].second + flowers[2].second))/(double)2.0));
            ans = min(ans,max(flowers[2].second, ((double)(dist(flowers[0].first,flowers[1].first) + flowers[0].second + flowers[1].second))/(double)2.0));
            cout << fixed << setprecision(6) << ans;
        }
        
        cout << endl;
        
    }
}
