#include <stdio.h>
#include <string.h>
#include <algorithm>

#define INF 2000000000

using namespace std;

struct node  {
	int start , finish;
	bool operator < (const node &o) const {
		if(start < o.start) return 1;
		else if(start == o.start) {
			if(finish < o.finish) return 1;
		}
		return 0;
	}
};

struct node p[1005];
int nnode;
int ncase ,n ,m;
char searchEngine[102][102] ,queryMessage[102];
int mic[1003];

int indexSearch(char *str) {
	int i;
	for(i=0;i<n;i++) 
		if(!strcmp(str , searchEngine[i]))
			return i;
	return -1;
}

void rcvInput(void) {
	int i;
	char junk;
	scanf("%d",&n);
	//printf("%d\n",n);
	scanf("%c",&junk);
	for(i=0;i<n;i++)  {
		gets(searchEngine[i]);
		//printf("%s\n",searchEngine[i]);
	}
	scanf("%d",&m);
	//printf("%d\n",m);
	scanf("%c",&junk);

}

void createPair(int a, int b) {
	p[nnode].start = a;
	p[nnode++].finish = b;
}

void createNode(void) {

	int pair[1002];
	int i ,index;
	for(i=0;i<n;i++)
		pair[i] = 0;
	for(i=0;i<m;i++) {
		gets(queryMessage);
		//printf("%s\n",queryMessage);
		index = indexSearch(queryMessage);
		//printf("%d %d\n",pair[index] , i-1);
		if(pair[index] <= i-1)
			createPair(pair[index] , i-1);
		pair[index] = i+1;
	}
	for(i=0;i<n;i++) 
		createPair(pair[i] ,m-1);

}

void debug() {
	int i;
	for(i=0;i<=m;i++) {
		printf("%d ",mic[i]);
	}
	printf("\n");
}

void process(void) {

	// Initialize
	int i ,j ,tmp;
	for(i=1;i<=m;i++) 
		mic[i] = INF;
	// End initialize 

	for(i=0;i<nnode;i++) {

		if(p[i].start - 1 < 0) tmp = 0;
		else tmp = mic[ p[i].start - 1] + 1;

		if(mic[ p[i].finish ] > tmp) {
			for(j=p[i].start ; j <= p[i].finish ;j++) 
				mic[j] = min(mic[j] , tmp);
		}
		//debug();
	}

}

void clearArray(void) {
	int i;
	for(i=0;i<=m;i++)
		mic[i] = 0;
	nnode = 0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.sol","w",stdout);

	int x;
	scanf("%d",&ncase);
	for(x=1;x<=ncase;x++) {
		clearArray();
		rcvInput();
		createNode();
		sort(p , p+nnode);
		process();
		printf("Case #%d: %d\n", x, mic[m-1]);
	}
	return 0;
}
