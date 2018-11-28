#include <stdio.h>
#include <algorithm>
#define MAX 1000

using namespace std;
struct box{
	int start,get;
}table1[2][MAX],table2[2][MAX];
bool cmp(box i,box j){
	if (i.start == j.start)
		return i.get < j.get;
	else
		return i.start < j.start;
}
int main(){
	int t_case,t,i,j,i1,j1;
	int time,h,w;
	int nab,nba,na,nb;
	int resa,resb;
	char t1[10],t2[10];
	scanf("%d",&t_case);
	for (t = 1;t <= t_case;t++){
		scanf("%d%d%d",&time,&na,&nb);
		for (i = 0;i < na;i++){
			scanf("%s%s",t1,t2);
			sscanf(t1,"%d:%d",&h,&w);
			table1[0][i].start = h*60+w;
			sscanf(t2,"%d:%d",&h,&w);
			table1[0][i].get = h*60+w;
		}
		sort(table1[0],table1[0]+na,cmp);
		for (i = 0;i < nb;i++){
			scanf("%s%s",t1,t2);
			sscanf(t1,"%d:%d",&h,&w);
			table2[0][i].start = h*60+w;
			sscanf(t2,"%d:%d",&h,&w);
			table2[0][i].get = h*60+w;
		}
		sort(table2[0],table2[0]+nb,cmp);
		resa = 0,resb = 0;
		nab = 0,nba = 0;
		i = 0,j = 0;
		i1 = 0,j1 = 0;
		while (i < na || j < nb){
			while (i < na && (j == nb
					|| (i < na && table1[0][i].start < table2[0][j].start))){
				table2[1][nab].start = table1[0][i].get+time;
				table2[1][nab].get = table2[1][nab].start+table1[0][i].get-table1[0][i].start;
				nab++;
				if (i1 < nba && table1[1][i1].start <= table1[0][i].start)
					i1++;
				else
					resa++;
				i++;
			}
			sort(table2[1],table2[1]+nab,cmp);
			while (j < nb && (i == na
					|| (j < nb && table1[0][i].start >= table2[0][j].start))){
				table1[1][nba].start = table2[0][j].get+time;
				table1[1][nba].get = table1[1][nab].start+table2[0][j].get-table2[0][j].start;
				nba++;
				if (j1 < nab && table2[1][j1].start <= table2[0][j].start)
					j1++;
				else
					resb++;
				j++;
			}
			sort(table1[1],table1[1]+nba,cmp);
		}
		printf("Case #%d: %d %d\n",t,resa,resb);
	}
}
