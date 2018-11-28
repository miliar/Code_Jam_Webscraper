#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

double rpif(double wp, double owp, double oowp){
	
	return 0.25*wp+0.50*owp+0.25*oowp;

}

int main(){
	
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout); 
    
    
    struct r{
		double wp,owp,oowp;
	};
	
	struct kk{
		double win,game;
	};
	
    string temp;
	int ii,i,j,k,l;
	int t,N;
	double wp=0,owp=0,oowp=0;
	double win=0,game=0;
	int flag=0;
	char mat[100][100];
	double rpi[100];
	r res[100];
	kk g[100];
	vector<double> owps,oowps;
	double sum=0;
	cin>>t;
	
	

	for ( k=1; k<=t; k++){
		
		cin>>N;
		

		for( i=0; i<N; i++ )
			for( j=0; j<N; j++ )
				cin>>mat[i][j];
		
		for( i=0; i<N; i++ ){
			for( j=0; j<N; j++ ){
				if( mat[i][j] == '1' ){
					win++;
					game++;
				}
				if( mat[i][j] == '0' )
					game++;
				}
			g[i].game=game;
			g[i].win=win;
			res[i].wp=win/game;
			win=0;
			game=0;
			}
		
		/*cout<<"wps=";
		for ( i=0; i<N; i++ )
		cout<<res[i].wp<<" "<<g[i].win<<" "<<g[i].game<<endl;
		*/	
		for( i=0; i<N; i++ ){
			for( j=0; j<N; j++ ){
				if ( i==j )
					continue;
				if (mat[i][j] == '1'){
					//cout<<"bak="<<(g[j].win)/(g[j].game-1)<<endl;
					owps.push_back ( (g[j].win)/(g[j].game-1) );}
				if (mat[i][j] == '0' ){
					//cout<<"bak="<<(g[j].win-1)/(g[j].game-1)<<endl;
					owps.push_back ( (g[j].win-1)/(g[j].game-1) );}
				}
			for ( l=0; l<owps.size(); l++ )
				sum+=owps[l];
			//cout<<"sum="<<sum<<endl;
			res[i].owp=sum/owps.size();
			owps.clear();
			sum=0;
		}
		/*
		cout<<"owps=";
		for ( i=0; i<N; i++ )
		cout<<res[i].owp<<" ";
		cout<<endl;
		*/
		
		
		sum=0;
		
		for( i=0; i<N; i++ ){
			for( j=0; j<N; j++ ){
				if (i==j)
					continue;
				if ( mat[i][j]== '1' or  mat[i][j]== '0' )
					oowps.push_back(res[j].owp);
			}
			for( l=0; l<oowps.size(); l++ )
				sum+=oowps[l];
			res[i].oowp=sum/oowps.size();
			sum=0;
			oowps.clear();
		}
		/*		
		cout<<"oowps=";
		for ( i=0; i<N; i++ )
		cout<<res[i].oowp<<" ";
		cout<<endl;
*/
		cout<<"Case #"<<k<<":"<<endl;
		for ( i=0; i<N; i++ )
			cout<<rpif(res[i].wp, res[i].owp, res[i].oowp)<<endl;
		

		

	}
	
	return 0;
	
}
		
			
			
			
			
			
			

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
