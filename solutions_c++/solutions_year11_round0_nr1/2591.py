#include<iostream>
#include<cmath>
#include <sstream>
#include <vector>
#define EPS 1e-20
#define ABS(X)  ((X)>0?(X):-(X))
#define FORN(i,n) FOR(i,0,n)
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define FOR(i,a,n) for (int i=(a);(i)<(n);i++)
using namespace std;
int toInt(string s){
stringstream st(s);

int l;
st>>l;
return l;
}
int main(int a, char ** b){
	
	int casos,n;
	cin>>casos;
	
	FORN(cc,casos){
		cin>>n;

		vector<string> S;
		FORN(i,2*n){
			string ww;
			cin>>ww;
			
			S.push_back(ww);
		}
	//	FORN(i,2*n)cout<<S[i]<<endl;
		int o=1;
		int b=1;
		int time=0;
		int timediff=0;
		int time_left_b=0;
		int time_left_o=0;
		FORN(i,n){
			if (S[i*2]=="O"){
			
			//mover
			int mover=ABS((toInt(S[(i*2)+1]))-o);
			o=toInt(S[(i*2)+1]);
			time+=mover;
			time_left_b+=1;
			//apretar
			time++;
				
			//restar lo que teniamos
			time-=MIN(time_left_o,mover);
			time_left_b+=MAX(mover-time_left_o,0);
			time_left_o=0;
			}
			else{
			//mover
			int mover=ABS((toInt(S[(i*2)+1]))-b);
			b=toInt(S[(i*2)+1]);
			time+=mover;
			time_left_o+=1;
			
			//apretar
			time++;
				
			//restar lo que teniamos
			time-=MIN(time_left_b,mover);
			time_left_o+=MAX(mover-time_left_b,0);
			time_left_b=0;
			}
		}
		cout<<"Case #"<<(cc+1)<<": "<<time<<endl;
		
		
	}
		

}
