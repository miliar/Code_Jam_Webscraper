#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int N,Ni;
    cin >> N;
    fgetc(stdin);
    for (Ni=0; Ni<N; Ni++) {
        string line;
        getline(cin, line);
        // printf("line%d: %s, sz=%d\n", Ni, line.c_str(), line.size());
        map<char, int> maps;
        map<char, int>::iterator it;
        vector<int> ans(line.size(), 0);
        vector<bool> flags(line.size(), false);
        int cc = 0;
        for (int i=0; i<line.size(); i++) {
            if (i==0) {
                maps[line[i]] = 1;
                ans[i] = 1;
                flags[1] = true;
            }else{
                it = maps.find(line[i]);
                if (it == maps.end()) {
                    while(flags[cc]) cc++;
                    maps[line[i]] = cc;
                    ans[i] = cc;
                    flags[cc] = true;
                    cc++;
                } else {
                    ans[i] = it->second;
                }
            }
        }
        if (cc <= 1) cc = 2;

        /*if (Ni+1==19)
        {
            printf("line%d: %s, sz=%d\n", Ni, line.c_str(), line.size());
            for (int k=0; k<ans.size(); k++) {
                printf("%d,", ans[k]);
            }
            printf("\n  base=%d\n", cc);
        }*/

        long long result = 0;
        for (int j=0; j<ans.size(); j++) {
            result *= cc;
            result += ans[j];
        }

        printf("Case #%d: %lld\n", Ni+1, result);
    }

    return 0;
}
