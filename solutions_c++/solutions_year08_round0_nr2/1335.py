#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;
struct x {
	int in;
	int out;
};	

int ttime;
int A_count, B_count;

x NA[101];
x NB[101];
char temp1[10],temp2[10];

int A_start(int time) { int res=0; for (int i=0; i<A_count;i++) if (NA[i].in==time) res++; return res; }
int B_start(int time) { int res=0; for (int i=0; i<B_count;i++) if (NB[i].in==time) res++; return res; }
int A_end(int time) { int res=0; for (int i=0; i<A_count;i++) if (NA[i].out==time) res++; return res; }
int B_end(int time) { int res=0; for (int i=0; i<B_count;i++) if (NB[i].out==time) res++; return res; }

int main(int argc, char *argv[])
{
	int lines;
	std::cin >> lines;

	for (int i=0;i<lines;i++) {
		std::cin >> ttime;
		std::cin >> A_count >> B_count;
		for (int j=0;j<A_count;j++) {
			scanf("%s",temp1);
			scanf("%s",temp2);
			NA[j].in=(temp1[0]-'0')*600+(temp1[1]-'0')*60+(temp1[3]-'0')*10+(temp1[4]-'0');
			NA[j].out=(temp2[0]-'0')*600+(temp2[1]-'0')*60+(temp2[3]-'0')*10+(temp2[4]-'0');
			}
		for (int j=0;j<B_count;j++) {
			scanf("%s",temp1);
			scanf("%s",temp2);
			NB[j].in=(temp1[0]-'0')*600+(temp1[1]-'0')*60+(temp1[3]-'0')*10+(temp1[4]-'0');
			NB[j].out=(temp2[0]-'0')*600+(temp2[1]-'0')*60+(temp2[3]-'0')*10+(temp2[4]-'0');
			}
		int from_a=0;
		int from_b=0;
		int stops_a=0;
		int stops_b=0;
		#define MIN(x, y) ((x) < (y) ? (x) : (y))

		for (int k=0;k<60*24;k++) {
			if (A_end(k-ttime)) { stops_b+=A_end(k-ttime); /*_*/}
			if (B_end(k-ttime)) { stops_a+=B_end(k-ttime); /*_*/}
			if (A_start(k)) {
				int cstart=MIN(A_start(k),stops_a);
				from_a+=A_start(k)-cstart;
				stops_a-=cstart;
				/*_*/
				}
			if (B_start(k)) {
				int cstart=MIN(B_start(k),stops_b);
				from_b+=B_start(k)-cstart;
				stops_b-=cstart;
				/*_*/
				}

		}
//		printf("Case All: %d %d\n",A_count,B_count);
//		printf("Case Stop: %d %d\n",stops_a,stops_b);
		printf("Case #%d: %d %d\n",i+1,from_a,from_b);	
	}
}
//printf("A: %d %d  B: %d %d\\n",from_a,stops_a,from_b,stops_b);

