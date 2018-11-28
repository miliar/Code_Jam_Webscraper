#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 100
#define BIT(x) (1<<(x-1))
using namespace std;
#define min(a,b) (((a) < (b)) ? (a) : (b))
int button[2][MAX+1];
int pos[2];//O is 0 B is 1
int end[2]={0};
struct _node{
	int col;
	int pos;
};
int n;
struct _node seq[MAX*2+1];
int  solve()
{
	int time=0;
	int delta=0;
	int flag[2]={0};
	int tmp,tmp1;
	int i;
	for (i=0;i<n; ++i){
		if (seq[i].col == 0){	
			tmp = abs(seq[i].pos-pos[0]) + 1;
			tmp1 = abs(pos[1] - button[1][flag[1]]);
			if (tmp >= tmp1)
				pos[1] = button[1][flag[1]];
			else{
				if (pos[1] > button[1][flag[1]])
					pos[1] -= tmp;
				else 
					pos[1] += tmp;
			}				
			time += tmp;
			pos[0] = seq[i].pos;
			flag[0]++;
		}else{
			tmp = abs(seq[i].pos-pos[1]) + 1;
			tmp1 = abs(pos[0] - button[0][flag[0]]);
			if (tmp >= tmp1)
				pos[0] = button[0][flag[0]];
			else{
				if (pos[0] > button[0][flag[0]])
					pos[0] -= tmp;
				else 
					pos[0] += tmp;
			}				
			time += tmp;
			pos[1] = seq[i].pos;
			flag[1]++;
		}
	}
	return time;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("large_out.txt", "w", stdout);
	int nt, it,x;
	char tmp;
	scanf("%d", &nt);
	int k,i,j;
	for (it = 1; it <= nt; it++)
	{
		pos[0] = 1;
		pos[1] = 1;
		memset(end,0,sizeof(end));

		scanf("%d ", &n);
		for (i=0; i<n; ++i){
			scanf("%c ",&tmp);
			if (tmp == 'O'){
				scanf("%d ",&button[0][end[0]++]);
				seq[i].pos = button[0][end[0]-1];
				seq[i].col = 0;
			} else{
				scanf("%d ",&button[1][end[1]++]);
				seq[i].pos = button[1][end[1]-1];
				seq[i].col = 1;
			}
		}

		printf("Case #%d: %d\n",it,solve());
		
	}
	return 0;
}