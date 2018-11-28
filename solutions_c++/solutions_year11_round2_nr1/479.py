//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

//#pragma warning(disable:4786)
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (int)(c).size()
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define LL long long
#define FOR(_name,_A,_B)  for(int _name=_A;_name<=(_B);_name++)

char str[103][103];
int T,N,cas=1;
double WP[103],OWP[103],OOWP[103];
void reset(){}
void calWP(){

	int win,loss;
	for(int i=0;i<N;i++){
	
		win=loss=0;
		for(int j=0;j<N;j++)
			if(str[i][j]=='1')
				win++;
			else if(str[i][j]=='0')
				loss++;
		WP[i]=(win*1.0)/(1.0*win+loss);
		//cout<<WP[i]<<endl;
	}
		

}
double cal_team_ith_op(int team,int op){

	int win,loss,i;
	win=loss=0;
	for(i=0;i<N;i++){
		if(i==team) continue;
		if(str[op][i]=='1')
			win++;
		if(str[op][i]=='0')
			loss++;
	}
	return (win*1.0)/(win+loss*1.0);
}
double calOWP4(int team){

	int nop=0;
	double total=0.0;
	for(int i=0;i<N;i++)
	if(str[team][i]=='0'||str[team][i]=='1'){	
		
		total+=cal_team_ith_op(team,i);
		nop++;
	
	}
	return total/nop;
}
void calOWP(){

	for(int i=0;i<N;i++){
		
		OWP[i]=calOWP4(i);
		//cout<<OWP[i]<<endl;
	}
	
}
double calOOWP4(int team){

	int nop=0;
	double sum=0.0;

	for(int i=0;i<N;i++)
		if(str[team][i]=='0'||str[team][i]=='1'){
			sum+=OWP[i];
			nop++;
		}

		return sum/nop;
}
void calOOWP(){

	for(int i=0;i<N;i++){
	OOWP[i]=calOOWP4(i);
	}

}
void process(){	

	calWP();
	calOWP();
	calOOWP();

	printf("Case #%d:\n",cas++);
	for(int i=0;i<N;i++)
	{
		printf("%.8lf\n",EPS+0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	
	
	}

}
int main()
{
	freopen("Source/A-large.in","rt",stdin);
	freopen("Source/out.txt","wt",stdout);
	
	cin>>T;
	while(T--){
	
		cin>>N;
		for(int i=0;i<N;i++)
			cin>>str[i];
	
		process();
	}
		
	return 0;
}
