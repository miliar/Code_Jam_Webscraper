#include<stdio.h>
#include<stdlib.h>

typedef long long int LL;

const int MAX_GROUP = 1005;

int num_case = 0;

int num_run = 0;
int num_peop = 0;
int num_group = 0;
int group[MAX_GROUP];

int nr[MAX_GROUP];
int mr[MAX_GROUP];

int cyroffset = 0;
int cymoffset = 0;
int cyruns = 0;
int cymoney = 0;
int cyidx = 0;

void simulate(){
	int cur = 0;
	int money = 0;
	int used_run = 0;
	int space = num_peop;
	while(1){
		if(nr[cur] != -1 && mr[cur] != -1)break;
		nr[cur] = used_run;
		mr[cur] = money;
		space = num_peop;
		for(int i = 0;i < num_group;i++){
			if(space < group[cur])break;
			space -= group[cur];
			money += group[cur];
			cur++;
			if(cur >= num_group)cur = 0;
		}
		used_run++;
	}
	cyruns = used_run - nr[cur];
	cymoney = money - mr[cur];
	cyroffset = nr[cur];
	cymoffset = mr[cur];
	cyidx = cur;
}

int main(){
	scanf("%d", &num_case);
	for(int caseno = 0;caseno < num_case;caseno++){
		scanf("%d %d %d", &num_run, &num_peop, &num_group);
		for(int i = 0;i < num_group;i++)
			scanf("%d", &group[i]);
		for(int i = 0;i <= num_group;i++){
			nr[i] = -1; mr[i] = -1;
		}

		simulate();
		/*for(int i = 0;i < num_group;i++)
			printf("nr = %d mr=%d\n", nr[i], mr[i]);
		printf("\n");	*/
		int gotm = 0;
		int startrunidx = 0;
		int findrun = 0;
		if(num_run < cyroffset){
			findrun = num_run;
			startrunidx = 0;
		}else{
			num_run -= cyroffset;
			gotm += cymoffset;
			int k = 0;
			if(cyruns != 0)
				k = num_run/cyruns;
			gotm += k*cymoney;
			findrun = (cyruns != 0 ? num_run%cyruns : 0) + cyroffset;
			startrunidx = cyidx;
		}

		for(int i = 0;i < num_group;i++){
			if(nr[i] == findrun){
				gotm += mr[i] - mr[startrunidx];
			}
		}
		printf("Case #%d: %d\n", caseno+1, gotm);
	}
}
