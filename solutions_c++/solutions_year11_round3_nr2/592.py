#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

//struct myclass {
//    int i;
//    bool operator() (myclass i,myclass j) { return (i.i<j.i);}
//} myobj;

int numBoost;
int timeBoost;
int N;
int patLen;
int* pattern;

int processing() {
    
    int ret;
    double earliestBoost = (double)timeBoost*(double)0.5;
    
    for(int i = 0; i < patLen; i++)
    {
        //printf("%d\n", pattern[i]);
    }
    
    int dist[N];
    double boostableDist[N];
    double slowDist[N];
    int alreadyBoosted[N];
    
    for(int i = 1; i <= N; i++)
    {
        dist[i-1] = pattern[(i-1)%patLen];
        alreadyBoosted[i-1] = 0;
        if((double)earliestBoost>=(double)dist[i-1])
        {
            boostableDist[i-1] = 0.0;
            earliestBoost -= (double)dist[i-1];
            slowDist[i-1] = (double)dist[i-1];
        }
        else if(earliestBoost > 0.0)
        {
            boostableDist[i-1] = (double)dist[i-1]-earliestBoost;
            slowDist[i-1] = earliestBoost;
            earliestBoost = 0.0;
        }
        else
        {
            boostableDist[i-1] = (double)dist[i-1];
            slowDist[i-1] = 0;
        }
        //printf("%d %f\n", dist[i-1], boostableDist[i-1]);
    }
    
    for(int i = 0; i < numBoost; i++)
    {
        int maxIdx = 0;
        double max = 0.0;
        for(int j = 0; j < N; j++)
        {
            if(alreadyBoosted[j] == 1) continue;
            if(boostableDist[j] > max)
            {
                max = boostableDist[j];
                maxIdx = j;
            }
        }
        //printf("max %f %d\n", max, maxIdx);
        alreadyBoosted[maxIdx] = 1;
    }
    
    // Calculate time
    double t = 0.0;
    for(int i = 0; i < N; i++)
    {
        if(alreadyBoosted[i] == 1) {
            //printf("%f %f\n", slowDist[i], boostableDist[i]);
            t += (slowDist[i]/0.5) + boostableDist[i];
        } else {
            //printf("%d\n", dist[i]);
            t += ((double)dist[i]/0.5);
        }
        //printf("t: %f\n", t);
    }
    
    ret = (int)t;
    return ret;
    
}

int main ()
{
	int T, TC = 1;
    
    for(scanf("%d", &T); TC <= T; TC++)
    {
        scanf("%d %d %d %d ", &numBoost, &timeBoost, &N, &patLen);
        
        pattern = new int[patLen];
        for(int i = 0; i < patLen; i++) {
            scanf("%d", &pattern[i]);
        }
        int t = processing();
		printf("Case #%d: %d\n", TC, t);
        delete pattern;
    }

    return 0;
}
