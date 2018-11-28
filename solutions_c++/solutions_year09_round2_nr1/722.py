#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <cctype>
using namespace std;
#define LB 1
#define RB 2
#define NUM 3
#define FET 4

char str[1000000];
char fet[100];
double num;
int len;
int idx;
set <string> fetset;
int token;
double res;

int get_token()
{
	int i;
	char temp[1000];

	while (str[idx] == ' ') {
		idx++;
    }
	if (str[idx] == '(') {
		idx++;
		return LB;
	}
	else if (str[idx] == ')') {
		idx++;
		return RB;
	}
    else if (isalpha(str[idx])) {
        i = 0;
        while (isalpha(str[idx])) {
            temp[i++] = str[idx];
            idx++;
        }
        temp[i] = 0;
        strcpy(fet, temp);
        return FET;
    }
    else {
        i = 0;
        while (isdigit(str[idx]) || str[idx] == '.') {
            temp[i++] = str[idx];
            idx++;
        }
        temp[i] = 0;
        sscanf(temp, "%lf", &num);
        return NUM;
    }

    return -1;
}

void tree(double p, int fl)
{
    token = get_token();    // 0.2
    p *= num;
    token = get_token();    // feture or )

//printf("p = %lf\n", p);
    // leaf
    if ( token == RB ) {
        if ( fl == 1 ) {
//printf("leaf---------------------\n");
            res = p;
        }
        return ;
    }

    if ( fetset.find(fet) != fetset.end() ) {   // exist
//printf("%s exit!!!\n", fet);
        token = get_token(); // (
        tree(p, fl * 1);
        token = get_token();
        tree(p, fl * 0);
    }
    else {  // doesn't exist
//printf("%s NOT exit!!!\n", fet);
        token = get_token(); // (
        tree(p, fl * 0);
        token = get_token();
        tree(p, fl * 1);
    }
    token = get_token();    // )
}

int main()
{
    int T, kase, L, A, n;
    int i, j;
    char temp[100];
    char name[100];

    scanf("%d", &T);
    kase = 1;

    while ( T-- ) {
        scanf("%d", &L);
        gets(str);
        gets(str);
        for ( i = 1 ; i < L ; i++ ) {
            gets(temp);
            strcat(str, temp);
        }

        printf("Case #%d:\n", kase++);

        scanf("%d", &A);
        for ( i = 0 ; i < A ; i++ ) {
            scanf("%s", name);
            scanf("%d", &n);
            fetset.clear();
            for ( j = 0 ; j < n ; j++) {
                scanf("%s", name);
                fetset.insert(name);
            }
            len = strlen(str);
            res = -1.0;
            idx = 0;
            token = get_token();
            tree(1.0, 1);
            printf("%.07lf\n", res);
        }
    }
    return 0;
}
