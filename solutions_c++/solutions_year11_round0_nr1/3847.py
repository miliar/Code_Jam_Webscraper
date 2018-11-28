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


vector<ii> input;
char str[100];
int next[1003],cas=1;
void reset(){}
int fnext(int i,int col){

	for(int k=i+1;k<input.size();k++)
		if(col==input[k].first)
			return input[k].second;
	return 0;
}
void process(){	

	
	int i,Time;
	for(i=0;i<input.size();i++)
		if(input[i].first==0){
			next[i]=fnext(i,1);
				
		}
		else next[i]=fnext(i,0);


		//now time loop
		int curO=1,curB=1;
		i=0;
		Time=0;
		while(i<input.size()){
		
			if(input[i].first==0){//orange

				if(curO<input[i].second){
				
					Time++;
					curO++;
					if(curB<next[i])					
						curB++;					
					else if(curB>next[i])
						curB--;
					//else nothing
					
				}
				else if(curO>input[i].second){
					Time++;
					curO--;

					if(curB<next[i])					
						curB++;					
					else if(curB>next[i])
						curB--;
				}
				else { //push button
				
					if(curB<next[i])					
						curB++;					
					else if(curB>next[i])
						curB--;

					Time++;
					i++;
					
				
				}

			
			}//end of orange
			else {// blue
			
				if(curB<input[i].second){
				
					curB++;
					Time++;
					if(curO<next[i])
						curO++;
					else if(curO>next[i])
						curO--;

				}
				else if(curB>input[i].second){
					curB--;
					Time++;

					if(curO<next[i])
						curO++;
					else if(curO>next[i])
						curO--;

				
				}
				else {

					if(curO<next[i])
						curO++;
					else if(curO>next[i])
						curO--;
					Time++;
					i++;
				}
			
			}

		
		
		}

		printf("Case #%d: %d\n",cas++,Time);

}
int main()
{
	freopen("source/A-large.in","rt",stdin);	
	freopen("source/A.out","wt",stdout);	
	int T,p,N;
	cin>>T;
	while(T--){
		
		input.clear();
		cin>>N;
		for(int i=0;i<N;i++){
		
			cin>>str>>p;
			ii a;
			a.first=(str[0]=='O')?0:1;
			a.second=p;
			input.push_back(a);
		
		}
		process();
	
	}
		
	return 0;
}
