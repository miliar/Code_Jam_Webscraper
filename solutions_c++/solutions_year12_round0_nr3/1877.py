#include<cstdio>
#include<map>
#include<string>

using namespace std;

inline bool isLessEq(const string &s, int i, int j){

    int n = s.size();

    for(int k = 0; k < n; ++k){

        if(s[i] < s[j]) return true;
        if(s[i] > s[j]) return false;
        ++i; ++j;
        if(i == n) i = 0;
        if(j == n) j = 0;
    }
    
    return true;

}

string getCanCycle(const string s){

    int min, n;
    min = 0;
    n = s.size();

    for(int i = 1; i < n; ++i) if(isLessEq(s, i, min)) min = i;

    string r;
    r.append(s.begin() + min, s.end());
    r.append(s.begin(), s.begin() + min);

    //printf("'%s' -> '%s' %d\n", s.c_str(), r.c_str(), min);

    return r;
}

int main(void){

    int t, a, b;
    long long int tt;
    map<string, int> m;

    scanf("%d", &t);
    
    for(int i = 1; i <= t; ++i){

        tt = 0;
        m.clear();

        scanf("%d %d", &a, &b);

        for(; a <= b; ++a){

            char b[32];
            sprintf(b, "%d", a);
            string c = getCanCycle(b);


            if(m.find(c) != m.end()){
                tt += m[c];
                m[c]++;
            }
            else m[c] = 1;
        }

        printf("Case #%d: %lld\n", i, tt);
        
    }
    return 0;
}
