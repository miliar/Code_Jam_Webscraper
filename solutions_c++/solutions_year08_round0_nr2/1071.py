#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

struct Node{
	int start;
	int end;
};

bool cmpstart(Node a,Node b)
{
	return a.start<b.start;
}
bool cmpend(Node a,Node b)
{
	return a.end<b.end;
}

int main()
{
	int N;
	int i,j,k;
	Node A[200],B[200];
	int at,bt;
	int anum,bnum;
	int T;
	int temp[4];

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&N);
	for(i=1; i<=N; i++){
		scanf("%d",&T);
		scanf("%d%d",&anum,&bnum);
		for(j=0; j<anum; j++){
			scanf("%d:%d %d:%d",&temp[0],&temp[1],&temp[2],&temp[3]);
			A[j].start=temp[0]*60+temp[1];
			A[j].end=temp[2]*60+temp[3];
		}
		for(j=0; j<bnum; j++){
			scanf("%d:%d %d:%d",&temp[0],&temp[1],&temp[2],&temp[3]);
			B[j].start=temp[0]*60+temp[1];
			B[j].end=temp[2]*60+temp[3];
		}
		at=anum;
		bt=bnum;
		sort(A,A+anum,cmpend);
		sort(B,B+bnum,cmpstart);
		for(j=0,k=0; j<anum && k<bnum; k++){
			if(A[j].end+T<=B[k].start){
				bt--;
				j++;
			}
		}
		sort(A,A+anum,cmpstart);
		sort(B,B+bnum,cmpend);
		for(j=0,k=0; j<bnum && k<anum; k++){
			if(B[j].end+T<=A[k].start){
				at--;
				j++;
			}
		}
		printf("Case #%d: %d %d\n",i,at,bt);
	}
	return 0;
}
