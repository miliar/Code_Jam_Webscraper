// que2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stdio.h"
#include <algorithm>
using namespace std;

struct TimeTable{
	int begin;
	int end;
	bool dealed;
};

TimeTable ta[128];
TimeTable tb[128];

int ba[128];
int bb[128];

int GetMin(){
	int BufMin;
	int BufIn;
	char c;
	BufMin = 0;
	scanf("%d", &BufIn);
	BufMin = BufIn;
	BufMin *= 60;
	scanf("%c", &c);
	scanf("%d", &BufIn);
	BufMin += BufIn;
	return BufMin;
}

int lessb(const TimeTable& t1, const TimeTable& t2){
	return t1.begin < t2.begin;
}
int lesse(const TimeTable& t1, const TimeTable& t2){
	return t1.end < t2.end;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	scanf("%d", &t);
	int i;
	for(i = 1 ; i <= t ; ++i){
		int turn;
		scanf("%d", &turn);
		int fa, fb;
		scanf("%d %d", &fa, &fb);
		int j, k;

		memset(ta, 0, sizeof(ta));
		memset(tb, 0, sizeof(tb));
		
		for(j = 0 ; j < fa ; ++j){
			ta[j].begin = GetMin();
			ta[j].end = GetMin();
		}
		for(j = 0 ; j < fb ; ++j){
			tb[j].begin = GetMin();
			tb[j].end = GetMin();
		}
		sort(ta, ta + fa, lesse);
		sort(tb, tb + fb, lesse);
		for(j = 0 ; j < fa ; ++j){
			bb[j] = ta[j].end + turn;
		}
		for(j = 0 ; j < fb ; ++j){
			ba[j] = tb[j].end + turn;
		}
		sort(ta, ta + fa, lessb);
		sort(tb, tb + fb, lessb);
		printf("Case #%d: ", i);
		int used = 0;
		for(j = 0 ; j < fa ; ++j){
			for(k = 0 ; k < fb ; ++k){
				if(ta[j].begin < ba[k]){
					break;
				}
			}
			if(k > used){
				++used;
			}
		}
		printf("%d ", fa - used);

		used = 0;
		for(j = 0 ; j < fb ; ++j){
			for(k = 0 ; k < fa ; ++k){
				if(tb[j].begin < bb[k]){
					break;
				}
			}
			if(k > used){
				++used;
			}
		}
		printf("%d\n", fb - used);
	}
	return 0;
}

