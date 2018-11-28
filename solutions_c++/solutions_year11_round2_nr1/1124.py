#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
const int MAXN = 200;
string grid[MAXN];
double calcwp(int amar, int bad, int n)
{
    int totalPlayed = 0, totalWon = 0;
    for(int i = 0; i < n; i++) {
        if(grid[amar][i] == '.' || bad == i) continue;
        totalPlayed++;
        if(grid[amar][i]=='1') totalWon++;
    }
    return (1.0*totalWon)/totalPlayed;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++) {
        cout<<"Case #"<<tc<<": "<<endl;
        int n;
        cin>>n;
        for(int i = 0;  i < n; i++) {
            cin>>grid[i];
        }
        vector<double> wpv(n,0.0);
        vector<double> owpv(n,0.0);
        vector<double> oowpv(n,0.0);

        for(int i = 0; i < n; i++) {
            //calculate wp
            wpv[i] = calcwp(i,-1,n);
            int totalop = 0;
            double cumwp = 0.0;
            for(int j = 0; j < n; j++) {
                if(grid[i][j]=='.') continue;
                cumwp+=calcwp(j,i,n);
                totalop++;
            }
            double owp = cumwp/totalop;
            owpv[i]=owp;
        }
        for(int i = 0; i < n; i++) {
                int totalop = 0;
            double cumowp = 0.0;
            for(int j = 0; j < n; j++) {
                if(grid[i][j]=='.') continue;
                cumowp+=owpv[j];
                totalop++;
            }
            oowpv[i] = cumowp/totalop;

        }
        for(int i = 0; i < n; i++) {
            printf("%.7f\n", 0.25 * wpv[i] + 0.50 * owpv[i] + 0.25 * oowpv[i]);
        }



    }
    return 0;
}
