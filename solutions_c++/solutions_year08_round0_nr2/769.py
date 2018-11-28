#include<stdio.h>
#include<string.h>

#define MAXN 100

typedef enum { LEAVE,READY } EventType;
typedef enum { A,B } Station;

struct event {
	int timepoint;
	EventType etype;
	Station sta;
} v[4*MAXN];

char str[10];
int turn_around_time;

void Input(int j,Station s)
{
	scanf("%s",str);
	v[j].timepoint = ((str[0]-'0')*10 + (str[1]-'0'))*60 + (str[3]-'0')*10 + (str[4]-'0');
	v[j].etype = LEAVE;
	scanf("%s",str);
	v[j+1].timepoint = ((str[0]-'0')*10 + (str[1]-'0'))*60 + (str[3]-'0')*10 + (str[4]-'0') + turn_around_time;
	v[j+1].etype = READY;
	v[j].sta = s;
	if (s==A) v[j+1].sta = B; else v[j+1].sta = A;
}

int main()
{
	int i,j,n,na,nb,CaseNum;
	int num[2];
	int remain[2];
	int tot;
	struct event temp;
	scanf("%d",&n);
	CaseNum = 1;
	FILE *fp = fopen("ans2_2.txt","w");
	while (CaseNum <= n) {
		scanf("%d",&turn_around_time);
		scanf("%d%d",&na,&nb);

		for (i = 0 , j = 0 ; i < na ; i++ , j+=2) Input(j,A);
		for (i = 0 ; i < nb ; i++,j+=2)	Input(j,B);

		tot = (na+nb)*2;

		for (i = 0 ; i < tot-1 ; i++)
			for (j = i+1 ; j < tot ; j++)
				if (v[i].timepoint > v[j].timepoint || (v[i].timepoint==v[j].timepoint && v[j].etype == READY)) {
					temp = v[i];
					v[i] = v[j];
					v[j] = temp;
				}

		num[A] = num[B] = 0;
		remain[A] = remain[B] = 0;

		for (i = 0 ; i < tot ; i++) {
			if (v[i].etype ==READY) {
				remain[v[i].sta]++;
			} else {
				remain[v[i].sta]--;
				if (remain[v[i].sta] < 0) {
					remain[v[i].sta] = 0;
					num[v[i].sta]++;
				}
			}
		}		

		fprintf(fp,"Case #%d: %d %d\n",CaseNum,num[A],num[B]);
		CaseNum++;
	}
	fclose(fp);
	return 0;
}