#include<cstdio>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;
class walkway{
public:
	int length;
	double ws, rs;
} walk[1001];
class cmp{
public:
	bool operator()(const walkway &a, const walkway &b){
		if(a.rs < b.rs) return true;
		return false;
	}
};

int main(void){
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");

	int T;
	int X, S, R, time, N;
	fscanf(fin,"%d",&T);
	for(int t=1;t<=T;t++){
		fprintf(fout,"Case #%d: ",t);
		fscanf(fin,"%d %d %d %d %d",&X,&S,&R,&time,&N);
		int walklen = X;
		for(int i=0;i<N;i++){
			int t1,t2;
			fscanf(fin,"%d %d %lf",&t1,&t2,&walk[i].ws);
			walk[i].length = t2 - t1;
			walk[i].rs = walk[i].ws + R;
			walk[i].ws += S;
			walklen -= (t2 - t1);
		}
		walk[N].length = walklen;
		walk[N].rs = R;
		walk[N].ws = S;
		N++;

		sort(walk,walk+N,cmp());
		int len = X;
		double ftime = time;
		double spend = 0;
		for(int i=0;i<N;i++){
			if(ftime != 0){
				double ts = walk[i].rs;
				double tc = (double)(walk[i].length) / ts;

				if( tc <= ftime ){
					ftime -= tc;
					spend += tc;
				} else{
					double sl = ftime * (double)ts;

					spend += ftime;
					spend += ((double)(walk[i].length) - sl) / walk[i].ws;

					ftime = 0;
				}
			} else{
				double ts = walk[i].ws;
				double tc = (double)(walk[i].length) / ts;
				spend += tc;
			}
		}
		fprintf(fout,"%lf\n",spend);
	}

	fcloseall();
}