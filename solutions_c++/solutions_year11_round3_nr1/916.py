#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int cases;
int curcase;
int pg, pd;
long long N;

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &cases);
	curcase = 1;

	int R, C;
	char str[70][70];

	while (curcase <= cases)
	{
		scanf("%d%d", &R, &C);
		for(int i=0; i<R; ++i)
			scanf("%s", str[i]);
		
		bool possi = true;
		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				if(str[i][j] == '#'){
					if(i == (R - 1)) possi = false;
					else if(j == (C - 1)) possi = false;
					else if(str[i + 1][j] == '#' && str[i+1][j+1] == '#' && str[i][j+1] == '#'){
						str[i][j] = '/';
						str[i + 1][j] = '\\';
						str[i+1][j+1] = '/';
						str[i][j+1] = '\\';
					}
					else
						possi = false;

					if(possi == false)
						break;
				}	
				if(possi == false)
					break;
			}
		}


		printf("Case #%d:\n", curcase);
		if(possi == false)
			printf("Impossible\n");
		else{
			for(int i=0; i<R; i++){
				printf("%s\n", str[i]);
			}
		}
		curcase ++;
	}
}
