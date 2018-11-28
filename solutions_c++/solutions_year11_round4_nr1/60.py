#include "hpmv.h"

hello
int X,S,R;
int T,N;
int3 ways[1024];
in(X,S,R,T,N);
inarr(N,ways);
int2 ways2[1024];
FOR(i,N)ways2[i]=int2(ways[i].g2,ways[i].g1-ways[i].g0);

int remain = X;
FOR(i,N) remain-=ways2[i].g1;
ways2[N]=int2(0, remain);

sort(ways2,ways2+N+1);

//outarr(N+1,ways2,"\n");ent;

double totalTime = 0;
double runLeft = T;

FOR(i,N+1){
	double wouldTime = ways2[i].g1/((double)(R+ways2[i].g0));
	if(runLeft>=wouldTime)
	{
		totalTime+=wouldTime;
		runLeft -= wouldTime;
	}
	else{
		double leftDist = ways2[i].g1;
		if(runLeft>0)	
		{
			leftDist -= runLeft*(ways2[i].g0+R);
			//out("leftDist",leftDist);ent;
			totalTime += runLeft;
			runLeft = 0;
		}
	//	out("tt1",totalTime);ent;
		
		totalTime += leftDist/((double)(ways2[i].g0+S));
		//out("tt2",totalTime);ent;
	}
	//out(totalTime);ent;
}
out(totalTime);ent;


cya
