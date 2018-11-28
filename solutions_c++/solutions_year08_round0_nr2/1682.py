#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define rall(v) (v).rbegin(),(v).rend()

vector<int> M[2][1510];

int T;
int Na,Nb,N;
const int INF = 0x3f3f3f3f;

int getMin(int st, int time)
{
    FOR(i,time,1510) if(M[st][i].size() > 0) return i;	
    return INF;
}


void doTrip(int st, int time)
{

	//printf("Estação:%d Tempo:%d\n",st,time);
	for(int i=st;; i=(i+1)%2)
	{
		int nextLeave = getMin(i,time);					
		if(nextLeave >= INF) return;
	 	time = M[i][nextLeave].back() + T;
		M[i][nextLeave].pop_back();
	}

}

int main()
{

	int Hleave,Mleave,Harrive,Marrive;

	scanf("%d",&N);
	
	FOR(t,0,N)
	{

	    scanf("%d ",&T);
	    scanf("%d %d ",&Na,&Nb);
	    FOR(i,0,Na)
	    {
		scanf("%d:%d %d:%d ",&Hleave,&Mleave,&Harrive,&Marrive);
		M[0][Hleave*60+Mleave].push_back(Harrive*60+Marrive);
		sort(rall(M[0][Hleave*60+Mleave]));
	    }
	    FOR(i,0,Nb)
	    {
		scanf("%d:%d %d:%d ",&Hleave,&Mleave,&Harrive,&Marrive);
		M[1][Hleave*60+Mleave].push_back(Harrive*60+Marrive);
		sort(rall(M[1][Hleave*60+Mleave]));
	    }	
	    	    
	    int A=0, B=0;

	    while(true)	
	    {
		int ac = getMin(0,0);
		int bc = getMin(1,0);
		if(ac >= INF && bc >= INF) break;	
		
		if(ac < bc || (ac==bc && M[0][ac].back() < M[1][bc].back())) {
			A++;
			doTrip(0,ac);		
		}		
		else{
			 B++;			
			 doTrip(1,bc);
		}
	    }	
		
	    printf("Case #%d: %d %d\n",t+1,A,B);
	}
	return 0;
}
