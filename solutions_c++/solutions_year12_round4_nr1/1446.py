#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstdio>

using namespace std;
vector< pair <int, int> > vines;
int D;

int dfs(int d, int l, int begin){
    int found;
    //cout << "d = " << d << endl;
    //cout << "l = " << l << endl;
    // cout << "begin = " << begin << endl;
    if((d + 2*l) >= D){
        return 1;
    }
    for(int i = vines.size() - 1; i > begin;i--){
        int found = 0;
        int correction;
        if((d + 2*l) >= vines[i].first){
            found = 1;
            if(d + l + vines[i].second < vines[i].first){
                correction = vines[i].first - d - l - vines[i].second;
            }else{
                correction = 0;
            }
            if(dfs(d+l+correction, min(vines[i].second, vines[i].first - d-l), i)){
                return 1;
            }else{
                continue;
            }
        }


    }
    if(!found) return 0;
}

int main()
{
    int t, n;
    cin >> t;
    int d,l;
    int currd, currlen;




    for(int i = 0; i < t; i++){
        cin >> n;
        vines.clear();
        for(int j = 0; j < n; j++){
            scanf("%d %d", &d, &l);
            vines.push_back(make_pair(d, l));
        }
        cin >> D;

        sort(vines.begin(), vines.end());
        //cout << vines[0].first << endl;
        if(dfs(0, vines[0].first, 0)){
            printf("Case #%d: YES\n", i+1);
        }else{
            printf("Case #%d: NO\n", i+1);
        }


    }

    return 0;
}
