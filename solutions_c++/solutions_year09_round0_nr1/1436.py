#include <iostream>
#include <string>
#include <memory.h>
using namespace std;

int l, d, n;

char words[10000][20];
string str;

char mask[20][300];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> l >> d >> n;
    
    for (int i = 0; i < d; ++i) {
        cin >> str;
        for (int j = 0; j < l; ++j)
            words[i][j] = str[j];
    }
    
    for (int i = 0; i < n; ++i) {
        cin >> str;
        for (int j = 0; j < l; ++j)
            memset(mask[j], 0, sizeof(mask[j]));
            
        int pos = 0;
        for (int j = 0; j < l; ++j) {
            if (str[pos] != '(')
               mask[j][str[pos++]] = 1;
            else {
                 ++pos;
                 while (str[pos] != ')') {
                       mask[j][str[pos++]] = 1;
                 }
                 ++pos;                 
            }            
        }
        int res = 0;
        for (int j = 0; j < d; ++j) {
            bool flag = true;
            for (int k = 0; k < l; ++k)
                if (mask[k][words[j][k]] == 0) {
                   flag = false;
                   break;
                }	
            if (flag)
               ++res;
	    }
		printf("Case #%d: %d\n", i + 1, res);
    }
    
    return 0;
}
