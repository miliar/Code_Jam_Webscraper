#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

typedef long long lld;

#define BROKEN printf("Broken\n");continue;
#define SIZE 100

#define IN freopen("A-small-attempt0.in","r",stdin);
#define OUT freopen("out1","w",stdout);

int T;

char cmap[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	IN
	OUT
	int i,t;
	char temp[SIZE+10];

	scanf("%d",&T);
	getchar();
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		gets(temp);

        int len = strlen(temp);
        for(i=0;i<len;i++){
            if(temp[i] == ' '){
                printf("%c",temp[i]);
                continue;
            }

            printf("%c",cmap[ temp[i] - 'a' ]);
        }
        printf("\n");

	}
	return 0;
}
