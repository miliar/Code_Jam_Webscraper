#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <vector>
#include <set>
#include <math.h>
#include <algorithm>
#include <cstring>

using namespace std;

#define REP(a,b) for(int (a)=0;a<(int)b;a++)
#define FOR(a,b,c) for(int (a)=b;a<(int)c;a++)
#define MP(A,B) pair<long long, long long>(A,B)
#define PB push_back
#define S(a) scanf("%d",&a);
#define SCH(a) scanf("%s",a);
#define foreach(a,b) for(__typeof(b).begin() a  = b.begin(); a != b.end();a++)

struct Walk
{
	int begin;
	int end;
	int increase;
	
	Walk(int a, int b, int c)
	{
		begin=a;
		end =b;
		increase =c;
	}
	
	Walk(){}
	
	bool operator < (Walk w) const
	{
		if(w.increase!=increase)
		{
			return increase<w.increase;
		}
		else if(begin!=w.begin)
		{
			return w.begin<begin;
		}
		else
		{
			return w.end<end;
		}
	}
	
	
};

Walk walk[1000];


int main()
{
	int T;
	S(T);
	
	REP(c,T)
	{
		double X;
		double S;
		double R;
		double t;
		int N;
		scanf("%lf %lf %lf %lf %d",&X,&S,&R,&t,&N);
		
		REP(n,N)
		{
			int a;
			int b;
			int c;
			S(a);
			S(b);
			S(c);
			walk[n]=Walk(a,b,c);
		}
		
		sort(walk,walk+N);
		
		double day=0;
		int start=0;
		
		
		
		

		
		REP(n,N)
		{
			X-=walk[n].end-walk[n].begin;
		}
		
		double help  = min(t*R,X);
		
		double helptime = help/(R);
		
		day+=help/(R);
		day+=(X-help)/(S);
		
		t-=helptime;
		
		//cout<<"T: " <<t<<endl;
		
		
		while(start<N)
		{
			//cout<<"INCREASE : "<<walk[start].increase<<endl;
			double way =walk[start].end-walk[start].begin;
			double fast = min(t*(R+walk[start].increase),way);
			
			//cout<<"FAST : "<<fast<<endl;
			
			day+=fast/(R+walk[start].increase);
			day+=(way-fast)/(S+walk[start].increase);
			
			t-=fast/(R+walk[start].increase);
			
			X-=way;
			start++;
		}
		
		
		printf("Case #%d: %.8lf\n",c+1,day);
	}
}









