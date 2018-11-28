#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("C:\\A-large.in");
ofstream fout("C:\\A-small-attempt6.out");
 
#define cin fin
#define cout fout

int a[101],b[101];
void set()
{
     for( int i = 0; i<101; i++)
		 a[i] = b[i] = 0;
}
int main()
{
     char BO;
	 int toward;
	 int Case,n;
	 cin>>Case;
	 for( int i = 1; i<=Case; i++)
	 {
	     int signa,signb,flaga,flagb;
		 signa = signb = 1;
		 flaga = flagb = 0;
		 int times = 0;
		 set();
		 cin>>n;
		 for( int j = 1; j<=n; j++)
		 {
		     cin>>BO>>toward;
			 if( BO == 'O')
			 {
//				 if( a[toward] ) continue;
			     if( flaga >= abs(toward-signa))
				 {
				     signa = toward;
					 flaga = 0;
					 times += 1;
					 flagb += 1;
				 }
				 else
				 {
					 times += abs(toward-signa)-flaga+1;
					 flagb += abs(toward-signa)-flaga+1;
					 signa = toward;
					 flaga = 0;
				 }
//				 a[toward] = 1;
			 }
			 if( BO == 'B')
			 {
//				 if( b[toward] ) continue;
			     if( flagb >= abs(toward-signb))
				 {
					 signb = toward;
					 times+=1;
					 flagb = 0;
					 flaga += 1;
				 }
				 else
				 {
				     times += abs(toward-signb)-flagb+1;
					 flaga += abs(toward-signb)-flagb+1;
					 signb = toward;
					 flagb = 0;
				 }
//				 b[toward] = 1;
			 }
		 }
		 cout<<"Case #"<<i<<": ";
		 cout<<times<<endl;
	 }
	 return 0;
}