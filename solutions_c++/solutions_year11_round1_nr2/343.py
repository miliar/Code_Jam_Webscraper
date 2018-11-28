
#include <set>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <string>
#include <iostream>
using namespace std;

bool tab[256];

string convert(string s) {
    for(int i=0;i<s.length();i++)
        if (!tab[s[i]]) s[i] = '_';
    return s;
}

int count(string s) {
    int count = 0;
    for(int i=0;i<s.length();i++) {
        if (!tab[s[i]]) s[i] = '_';
        else { tab[s[i]]=0; count++; }
    }
    for(int i=0;i<s.length();i++) if (s[i]!='_') tab[s[i]]=1;
    return count;
}

string gen(string s) { for(int i=0;i<s.size();i++) s[i]='_'; return s;}

bool cont(string s, char c) { for(int i=0;i<s.size();i++) if (s[i]==c) return true; return false; }

int CN = 1;
void scase() {
    int n,m;
    cin >> n >> m;
    string D[n], E[n], F[n];
    int points[n];
    bool only[m];
    for(int i=0;i<n;i++) {
        cin >> D[i];
    }
    cout << "Case #" << CN++ << ":";
    while(m--) {
        string L; cin >> L;
        
        for(int i=0;i<n;i++) { 
            //printf("checking i = %d\n",i);
            points[i] = 0; 
            for(int j=0;j<n;j++) E[j] = gen(D[j]);
            string board = gen(E[i]);
            for(int j=0;j<L.size();j++) {
                //printf("j=%d L[j]=%c\n",j,L[j]);
                bool check = false;
                for(int k=0;k<n;k++) if (E[k]==board && cont(D[k], L[j])) check = true;
                if (!check) continue;
                //printf("check done\n");
                for(int k=0;k<n;k++) for(int z=0;z<D[k].size();z++) if (D[k][z] == L[j]) E[k][z] = L[j];
                board = E[i];
                if (!cont(D[i], L[j])) points[i]++;
            }
            //printf("points %s = %d\n",D[i].c_str(), points[i]);
        }

        int best = 0;
        for(int i=0;i<n;i++) if (points[i]>points[best]) best=i;
        cout << " " << D[best];

    
    
    }

    cout << endl;

}

int main() {
    int j; cin >> j;
    while(j--) scase();
    return 0;
}




        

