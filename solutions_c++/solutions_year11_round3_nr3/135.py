// acm.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cassert>
#include <algorithm>
using namespace std;


int note[1024];
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);

	int cas;
	scanf("%d", &cas);
	for(int cas_i=1;cas_i<=cas;cas_i++)
	{
		printf("Case #%d:", cas_i);
		

		int n,L,H;
		scanf("%d %d %d\n", &n ,&L, &H);

		for(int i=0;i<n;i++){
			scanf("%d", &note[i]);

		}
		bool found = false;
		int x;
		for(x=L;x<=H;x++){
			bool inv = false;
			for(int i=0;i<n;i++){
				int px = note[i];
				if(x % px == 0 || px % x == 0){

				}else{
					inv = true;
					break;
				}
			}
			if(inv){
				continue;
			}else{
				found = true;
				break;
			}
		}
		if(found){
			printf(" %d\n", x);
		}else{
			printf(" NO\n");
		}

	}
	return 0;
}

