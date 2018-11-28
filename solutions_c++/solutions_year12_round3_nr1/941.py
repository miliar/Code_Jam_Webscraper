#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define mp make_pair
#define pb push_back

vector < vector <int> > a;
vector<int> color(1001);
bool f;

bool dfs(int v){
    color[v]=1;
    for (int j=0;j<a[v].size();j++){
        int to=a[v][j];
        if (color[to]==0){
            dfs(to);
        }
        else f=true;
    }
    color[v]=2;
    if (f) return true;
    else return false;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for (int o=1;o<=t;o++){
        cout << "Case #" << o << ": ";
        int n;
        cin >> n;
        vector <int> tmp;
        a.assign(1001,tmp);
        for (int i=0;i<n;i++){
            int m;
            cin >> m;
            for (int j=0;j<m;j++){
                int x;
                cin >> x;
                a[i].push_back(x-1);
            }
        }
        for (int i=0;i<n;i++){
            f=false;
            color.assign(1000,0);
            if (dfs(i)){
                cout << "Yes"<<'\n';
                f=true;
                break;
            }
        }
        if (!(f)) cout << "No" <<'\n';
    }
}
