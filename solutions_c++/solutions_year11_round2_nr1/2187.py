#include <iostream>
#include<iomanip>
#include <cmath>
#include <fstream>
using namespace std;

ifstream fin("D:\\acm\\pa11\\a\\A-large.in");
ofstream fout("D:\\acm\\pa11\\a\\A-large.out");
 
#define cin fin
#define cout fout
const int set_size = 105;
const double mat = 10000000.0;
double wp[set_size],owp[set_size],oowp[set_size];
int x[set_size][set_size];
struct 
{
     int win,lost;
}winner[set_size];
void set()
{
     for( int i = 0; i<set_size; i++)
		 x[i][0] = 0;
	 for( int i = 0; i<set_size; i++)
		 winner[i].lost = winner[i].win = 0;
	 return ;
}
int main()
{
	 int i,j,k,n;
	 char ch;
	 int Case,win,lost;
	 cin>>Case;
	 for( i =1; i<=Case; i++)
	 {
	     cin>>n;
		 set();
		 for( j = 1; j<=n; j++)
		 {
			 win = lost = 0;
			 for( k = 1; k<=n; k++)
			 {
				 cin>>ch;
				 if( ch == '.' ) { x[j][k] = -1; continue;}
				 if( ch == '0' ) { ++lost; x[j][k] = 0;x[j][0]++;}
				 if( ch == '1' ) { ++win; x[j][k] = 1;x[j][0]++;}
			 }
			 wp[j] = mat*win/(win+lost);
			 winner[j].lost = lost;
			 winner[j].win = win;
		 }
		 for( j = 1; j<=n; j++)
		 {
		     owp[j] = 0;
			 int xwin,xlost;
			 for( k = 1; k<=n; k++)
			 {
				 if( x[j][k] == 0||x[j][k] == 1 )
				 {
					 xwin = winner[k].win; 
					 xlost = winner[k].lost;
				     if( x[k][j] == 0 ) --xlost;
					 if( x[k][j] == 1 ) --xwin;
					 owp[j] += mat*xwin/(xwin+xlost);
				 }
			 }
			 owp[j] = owp[j]/x[j][0];
		 }
		 for( j = 1; j<=n; j++)
		 {
		     oowp[j] = 0;
			 for( k = 1; k<=n; k++)
			 {
			     if( x[j][k] == 0||x[j][k] == 1 )
				 {
				     oowp[j] += owp[k];
				 }
			 }
			 oowp[j] = oowp[j]/x[j][0];
		 }
		 cout<<"Case #"<<i<<":"<<endl;
		 for( j = 1; j<=n; j++)
		 {
		     double sum = wp[j]/4 + owp[j]/2 + oowp[j]/4;
			 cout<<setw(0)<<setprecision(12)<<sum/mat<<endl;
		 }
	 }
     return 0;
}