#include<iostream>
#include<string>
#include<set>
#include<vector>
#include<stdio.h>
using namespace std;
set<char> check[25];
vector<string> str;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int L, D, N;
    int i, j, sum, cnt, p;
    string tem;
    while (scanf("%d %d %d", &L, &D, &N) != EOF) {
        str.clear();
        for (i = 0; i < D; i++) {
            cin >> tem;
            str.push_back(tem);
        }
        for (i = 1; i <= N; i++) {
            cin >> tem;
            for (j = 0; j < L; j++)
                check[j].clear();
            cnt = 0;
            for (j = 0; j < tem.size(); j++)
                if (tem[j] == '(') {
                    j++;
                    while (tem[j] != ')')
                        check[cnt].insert(tem[j++]);
                    cnt++;
                } else
                    check[cnt++].insert(tem[j]);
           /* for(j = 0; j < L; j++){
                for(set<char>::iterator q = check[j].begin(); q!=check[j].end(); q++)
                    printf("%c ",*q);
                printf("\n");
            }*/
            sum = 0;
            for (j = 0; j < str.size(); j++) {
                for (p = 0; p < str[j].size(); p++)
                    if ( check[p].find(str[j][p]) == check[p].end() )break;
                sum += (p == str[j].size());
            }
            printf("Case #%d: %d\n", i, sum);
        }
    }
}