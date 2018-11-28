// acm.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cassert>
using namespace std;


char pic[64][64];
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);

	int cas;
	scanf("%d", &cas);
	for(int cas_i=1;cas_i<=cas;cas_i++)
	{
		printf("Case #%d:\n", cas_i);
		int r,c;
		scanf("%d %d\n", &r, &c);
		memset(pic, 0, sizeof(pic));
		for(int i=0;i<r;i++){
			scanf("%s\n", pic[i]);
			assert(strlen(pic[i]) ==c);

		}
		for(int i=0;i<r;i++){
			for(int ii=0;ii<c;ii++){
				if(pic[i][ii] == '#'){
					if(pic[i][ii+1] == '#' && pic[i+1][ii] == '#'  && pic[i+1][ii+1] == '#'){
						pic[i][ii] = '/';
						pic[i][ii+1] = '\\';
						pic[i+1][ii] = '\\';
						pic[i+1][ii+1] = '/';
					}else{
						goto invalid;
					}
				}
			}
		}
		for(int i=0;i<r;i++){
			printf("%s\n", pic[i]);
		}
		continue;
invalid:
		printf("Impossible\n");

	}
	return 0;
}

