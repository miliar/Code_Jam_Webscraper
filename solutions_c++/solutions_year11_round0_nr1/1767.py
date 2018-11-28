
#include <iostream>
using namespace std;

int abs(int i)
{
	if(i<0)
		i=-i;
	return i;
}

int max(int a,int b){
	return a>b?a:b;
}

int solve()
{
	int tasknum;
	cin>>tasknum;

	int opos=1,bpos=1;
	int owait=0,bwait=0;
	int otime=0,btime=0;
	int passtime = 0;

	char role;
	int dest;
	for(int i=0;i<tasknum;++i){
		cin>>role>>dest;
		if(role=='O'){
			otime = max(abs(dest-opos)-owait,0)+1;
			passtime+=otime;
			bwait+=otime;
			owait = 0;
			opos=dest;
		}else{
			btime = max(abs(dest-bpos)-bwait,0)+1;
			passtime+=btime;
			owait += btime;
			bwait=0;
			bpos=dest;
		}
	}

	return passtime;
}

int main()
{
	int casenum;
	cin>>casenum;
	for(int i=0;i<casenum;++i){
		cout<<"Case #"<<(i+1)<<": "<<solve()<<endl;
	}
}
