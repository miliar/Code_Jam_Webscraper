#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cmath>
#include <math.h>


using namespace std;

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
        vector <pair<int,int> > a;
        a.clear();
        for (int i=0;i<n;i++){
            int x,y;
            cin >> x >> y;
            a.push_back(make_pair(y,x));
        }
        sort(a.begin(),a.end());
        int rat=0;
        int ans=0;
        vector <bool> used(n,true);
        vector <bool> used2(n,true);
        bool f=true,g=true;
        int cnt=0;
        while (f){
            f=false;
            cnt++;
            int i=0;
            while (i<n){
                if ((used[i])&&(a[i].first <= rat)){
                    if (!(used2[i]))
                        rat++;
                    else
                        rat+=2;
                    used[i]=false;
                    ans++;
                }
                else if (used[i]){
                    for (int j=n-1;j>=0;j--){
                        if((used[j])&&(used2[j])&&(a[j].second <=rat)){
                            used2[j]=false;
                            rat++;
                            ans++;
                            i=-1;
                            break;
                        }
                    }
                }
                i++;
            }
            for (int i=0;i<n;i++){
                if (used[i]) f=true;
            }
            if (cnt > 2003){
                cout << "Too Bad" << endl;
                g=false;
                break;
            }
        }
        if (g){
            cout << ans << endl;
        }
    }
}
