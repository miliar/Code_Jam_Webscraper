#include <iostream>
#include <string>
using namespace std;

#define MaxC 36
#define MaxD 28
#define MaxN 100

int T, C, D, N;
string c[MaxC], d[MaxD];
string s;
int kiekiai[500];

void nullkiekiai() {
    for (int i = 0; i < 500; i++)
        kiekiai[i] = 0;
}


void solve (int t) {
    nullkiekiai();
   // printf("[radedeaam\n");
    string ats = "";
    for (int i = 0; i < N; i++) {
        if (ats.size() == 0) {
           ats += s[i]; 
           kiekiai[s[i]]++;
        }else {
            bool combined = false;
            for (int j = 0; j < C; j++) {
                if ( (c[j][0] == s[i] && c[j][1] == ats[ats.size()-1]) || 
                    (c[j][0] == ats[ats.size()-1] && c[j][1] == s[i])) {
                        //combines
                        kiekiai[ats[ats.size()-1]]--;
                        ats[ats.size()-1] = c[j][2];
                        kiekiai[c[j][2]]++;
                        combined = true;
                        break;
                    }
            }
           // printf("combined = %d (%c)\n", combined, s[i]);
            if (!combined) {
                ats+=s[i];
                kiekiai[s[i]]++;
                bool opposed = false;
                for (int j = 0; j < D; j++) {
                 //   printf("opposed: %s %d %d\n", d[j].c_str(), kiekiai[d[j][0]], kiekiai[d[j][1]]);
                    if (kiekiai[d[j][0]] > 0 && kiekiai[d[j][1]] > 0) {
                        nullkiekiai();
                        opposed = true;
                        ats = "";
                    }
                }
            }
            
        }
        //printf("ats = %s\n", ats.c_str());
        //for (int i = 'A'; i <= 'Z'; i++)
         //   printf("%c:%d ", i, kiekiai[i]);
        //printf("\n");
    }
    printf("Case #%d: [", t);
    for (int i = 0; i < ats.size(); i++)
        printf("%c%s",ats[i], i == ats.size() - 1 ? "" : ", ");
    printf("]\n");
}

int main() {
    freopen("magicka.in","r",stdin);
    freopen("magicka.out","w",stdout);
    scanf("%d\n", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d", &C);
        for (int j = 0; j < C; j++)
            cin >> c[j];
        scanf("%d", &D);
        for (int j = 0; j < D; j++)
            cin >> d[j];
        scanf("%d", &N);
        cin >> s;
        solve(i+1);    
    }
    
    
    
    
    return 0;    
}
