#include<iostream>
#include<stdio.h>
using namespace std;

int B[1000], E[1000], w[1000];
struct walk {
    int speed;
    int dist;
};

walk wk[1001];

int main() {
    int T, c=0, i, j, k, tot_dist, X, S, R, N;
    double t;
    cin >> T;
    while(T--) {
	tot_dist = 0;
	cin >> X >> S >> R >> t >> N;
	for(i=0; i<N; i++)
	{
	    cin >> B[i] >> E[i] >> w[i];
	    w[i] += S;
	    for(j=i; j>=1; j--) {
		if(wk[j].speed > w[i]) {
		    wk[j+1] = wk[j];
		} else {
		    break;
		}
	    }
	    //cerr << "j = " << j << endl;
	    j++;
	    wk[j].speed = w[i];
	    wk[j].dist = E[i] - B[i];
	    tot_dist += wk[j].dist;
	    //cerr << "tot_dist = " << tot_dist << endl;
	}
	wk[0].speed = S;
	wk[0].dist = X - tot_dist;


	double time = 0;
	for(i=0; i<N+1; i++) {
		//cerr << "time = " << t << " w[i] = speed:"<< wk[i].speed << " dist:" << wk[i].dist << endl;
	    if(t > 0) {
		double speed = wk[i].speed + R - S;
		//cerr << "Speed : " << speed << endl;
		double time1 = wk[i].dist / speed;
		//cerr << "time1 : " << time1 << endl;
		if(time1 < t) {
			//cerr << "Here " << __LINE__ << endl;
		    t-=time1;
		    time += time1;
		} else {
			//cerr << "Here " << __LINE__ << endl;
		    time += t;
		    double dist_travelled = t*speed;
		    //cerr << "Dist travelled : " << dist_travelled << endl;
		    time += (wk[i].dist - dist_travelled)/wk[i].speed;
		   t = 0;
		}
	    } else {
	        double dist = wk[i].dist;
	        time += dist/wk[i].speed;
	    }
	}
	printf("Case #%d: %.6f\n", ++c, time);
//        cout << "Case #"<< ++c << ": " << time << endl;
    }
}
