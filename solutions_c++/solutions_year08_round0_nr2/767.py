#include <iostream>
using namespace std;

typedef struct{
    int start;
    int end;
    int id;
}TRIPS;
TRIPS trips[300];
int flag[300];

bool cmp(const TRIPS &a, const TRIPS &b){
    if(a.start == b.start) return a.end < b.end;
    return a.start < b.start;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int kase, i, j, k, t, na, nb;
    int a1, a2, b1, b2;
    char ch;
    cin >> kase;    
    for(i = 1; i <= kase; i++){
        cin >> t;
        cin >> na >> nb;
        for(j = 0; j < na; j++){
            cin >> a1 >> ch >> a2 >> b1 >> ch >> b2;
            trips[j].start = a1*60 + a2;
            trips[j].end = b1*60 + b2;
            trips[j].id = 0;
        }
        for(j = na; j < na+nb; j++){
            cin >> a1 >> ch >> a2 >> b1 >> ch >> b2;
            trips[j].start = a1*60 + a2;
            trips[j].end = b1*60 + b2;
            trips[j].id = 1;
        }
        sort(trips, trips+na+nb, cmp);
        int ans0 = 0, ans1 = 0;
        int tm, id;
        memset(flag, 0, sizeof(flag));
        for(j = 0; j < na+nb; j++){
            if(flag[j] == 0){
                if(trips[j].id == 0) ans0++;
                else ans1++;
                flag[j] = 1;
                tm = trips[j].end;
                id = trips[j].id;
                for(k = j+1; k < na+nb; k++){
                    if(flag[k] == 0 && trips[k].id != id && trips[k].start >= tm + t){
                        flag[k] = 1;
                        tm = trips[k].end;   
                        id = trips[k].id;
                    }
                }
            }
        }
        cout << "Case #" << i << ": " << ans0 << " " << ans1 << endl;    
    }
    return 0;
}
