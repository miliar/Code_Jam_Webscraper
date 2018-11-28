/**********************************************************************
Author: sproblvem
Created Time:  2011/5/7 12:32:56
File Name: a.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}

typedef struct _robot_info{
	int pos;
	int ti;
} robot_info;

int main() {
	FILE *fout = fopen("a.out", "w");
   	int kase;
   	scanf("%d", &kase);
	for (int ii = 0; ii < kase; ++ii){
		int res = 0;
		int n = 0;
		scanf("%d", &n);
		robot_info robot[2];
		robot[0].pos = 1;
		robot[0].ti = 0;
		robot[1].pos = 1;
		robot[1].ti = 0;
		char robot_color[10];
		for (int i = 0; i < n; ++i){
			int button = 0;
			scanf("%s %d", robot_color, &button);
			int ind = 0;
			if ('B' == robot_color[0])
				ind = 1;
			int cost = (abs(button - robot[ind].pos) <= res - robot[ind].ti) ? 0 : abs(button - robot[ind].pos) - (res - robot[ind].ti); 
			res += cost + 1;
			robot[ind].pos = button;
			robot[ind].ti = res;
		}
		fprintf(fout, "Case #%d: %d\n", ii + 1, res);
	}
    return 0;
}

