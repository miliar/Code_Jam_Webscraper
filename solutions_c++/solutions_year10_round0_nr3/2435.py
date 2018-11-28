#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <deque>
using namespace std;


#define forn(i,n) for(int i=0;i<n;i++)


int main()
{
	char filename[32]="C-small-attempt6";
	char infile[32], outfile[32];
//	scanf("%s", filename);
	strcpy ( infile, filename );
	strcpy ( outfile, filename );
	strcat ( infile, ".in" );
	strcat ( outfile, ".out" );
	FILE *ifp=freopen ( infile, "r",stdin );
	FILE *ofp=freopen ( outfile, "w",stdout );
	if ( ifp==NULL ) return -1;


	int T;
	scanf ( "%d",&T );
	int R;//一天运行次数
	int K;//容量
	int N;//组数
	int i;
	int tmp;
	int cnt;//开行次数
	int s;//最大人数
	int front;//当前首结点
	int cost;//费用
	int c;//当次使用组数
	forn ( t,T ) {
		cost=0;
		cnt=0;
		scanf("%d%d%d",&R,&K,&N);
		deque<int> q(0);
		for (i=0;i<N;i++) {
			scanf("%d",&tmp);
			q.push_back(tmp);
		}
//		deque<int>::iterator iter;
//		for (iter=q.begin();iter!=q.end();iter++) {
//			printf("%d ",*iter);
//		}
//		printf("\n");
//		printf("%d\n",q.front());
		while (cnt++<R) {
			c=0;
			s=0;
			if (N==1) {
				front=q.front();
				s+=front;
			} else {
				while (s<K) {
					front=q.front();
					if (s+front>K||c==N) break;
					q.pop_front();
					q.push_back(front);
					s+=front;
					c++;
				}
			}
			cost+=s;
		}
		printf ( "Case #%d: %d\n", t+1, cost );
	}



	fclose ( ifp );
	fclose(ofp);
	return 0;
}
