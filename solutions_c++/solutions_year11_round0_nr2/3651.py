#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int t, c, d, n;
char com[5], seq[105];
int eq[30][30], has[30];
bool pwn[30][30];
vector<int> curr;

int main(){
    freopen("B.txt", "w", stdout);
    scanf("%d", &t);
    for (int tc=1; tc<=t; tc++){
        memset(eq, 0, sizeof eq);
        memset(has, 0, sizeof has);
        memset(pwn, 0, sizeof pwn);
        curr.clear();

        scanf("%d", &c);
        for (int i=0; i<c; i++){
            com[0]=' ';
            while(com[0]<'A' or com[0]>'Z')
                scanf("%s", com);
            eq[com[0]-'A'][com[1]-'A']=eq[com[1]-'A'][com[0]-'A']=com[2]-'A';
        }
        scanf("%d", &d);
        for (int i=0; i<d; i++){
            com[0]=' ';
            while(com[0]<'A' or com[0]>'Z')
                scanf("%s", com);
            pwn[com[0]-'A'][com[1]-'A']=pwn[com[1]-'A'][com[0]-'A']=true;
        }

        scanf("%d", &n);
        seq[0]=' ';
        while(seq[0]<'A' or seq[0]>'Z')
            scanf("%s", seq);
        for (int i=0; i<strlen(seq); i++){
            int ovo=seq[i]-'A';
            if (curr.empty()){
                curr.push_back(ovo);
                has[ovo]++;
                continue;
            }
            int temp=eq[curr[curr.size()-1]][ovo];
            if (temp){
                has[curr[curr.size()-1]]--;
                curr.pop_back();
                curr.push_back(temp);
                has[temp]++;
            }
            else {
                bool failed=false;
                for (int j=0; j<26; j++)
                    if (pwn[j][ovo] and has[j])
                        failed=true;
                if (failed){
                    curr.clear();
                    memset(has, 0, sizeof has);
                }
                else {
                    has[ovo]++;
                    curr.push_back(ovo);
                }
            }

        }

        printf("Case #%d: [", tc);
        for (int i=0; i<curr.size(); i++){
            printf("%c", curr[i]+'A');
            if (i<curr.size()-1)
                printf(", ");
        }
        printf("]\n");
    }
	return 0;
}
