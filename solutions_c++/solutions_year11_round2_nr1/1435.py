#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <vector>
using namespace std;

char sch[100][100];
int N;
double WP[100];
double OWP[100];
double OOWP[100];
double  w[100];
double  g[100];
void calcWP(){
	for(int i=0;i<N;i++){
		double win=0,game=0;
		for(int j=0;j<N;j++){
			if(sch[i][j]=='.') continue;
			else if(sch[i][j]=='0') game++;
			else {
				game++;
				win++;
			}
		}
		w[i]=win;
		g[i]=game;
		WP[i]=win/game;
		//cout<<win<<" "<<game<<" "<<WP[i]<<endl;
	}
}

ostream& operator<<(ostream& os,vector<double> v){
	if(v.size()==0) cout<<"NULL";
	for ( vector<double>::iterator it=v.begin() ; it != v.end(); it++ ) os <<*it <<endl;
	return os;
}

void calcOWP(){
	for(int i=0;i<N;i++){
		double ans=0;
		for(int j=0;j<N;j++){
			if(sch[i][j]=='.')continue;
			else {
				ans+=((w[j]-(sch[j][i]-'0'))/(g[j]-1));
			}
		}
		ans=ans/g[i];
		OWP[i]=ans;
		cout<<ans*g[i]<<" "<<g[i]<<" "<<OWP[i]<<endl;
	}
}

void 	calcOOWP(){
	for(int i=0;i<N;i++){
		double ans=0;
		for(int j=0;j<N;j++){
			if(sch[i][j]=='.') continue;
			else {
				ans+=OWP[j];
			}
		}
		ans=ans/g[i];
		OOWP[i]=ans;
	//cout<<win<<" "<<game<<" "<<OWP[i]<<endl;
	}
}	
					
vector<double>solve(){
		calcWP();
		calcOWP();
		calcOOWP();
		vector<double> ans;
		for(int i=0;i<N;i++){
			double RPI;
			RPI=0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i];
			ans.push_back(RPI);
		}
	return ans;
}

int main(){
	int T;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	while(i!=T+1){
	 ps>>N;
	 for(int k=0;k<N;k++){
		for(int j=0;j<N;j++){
			char ch;
			ps>>ch;
			sch[k][j]=ch;
		}
	 }	
	 output<<"Case #"<<i<<": "<<endl<<solve();
	 i++;	
	}		
	return 0;
}	
