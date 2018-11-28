#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
	double cnk[50][50];
int main(){
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int cases; int c; int n;
	cin>>cases;
	double table[50],ttable[50];

memset(cnk, 0, sizeof(cnk));
	cnk[0][0] = 1;
	
	for(int i = 1; i<43; i++){
		for(int j = 1; j<=i; j++)
			cnk[j][i] = cnk[j-1][i-1]+cnk[j][i-1];
	    cnk[0][i] = 1;
	}
	for(int tnum = 0; tnum<cases; tnum++)
	{
		cin>>c>>n;
		memset(table,0, sizeof(table));
		table[n] = 1;
		int iter = 200000;
		double time = table[c];
		for(int i = 0; i<iter; i++)
		{
		   memset(ttable, 0, sizeof(ttable));
		   for(int j = n; j<c; j++)
		   {
               double sum = 0; 
			   for(int add = 0; add<=n; add++)
				 sum+=cnk[add][c-j]*cnk[n-add][j];
			   for(int add = 0; add<=n; add++)
				 ttable[j+add]+=table[j]*cnk[add][c-j]*cnk[n-add][j]/sum;
			   
		   }
		   time+=ttable[c]*(i+2);
		   for(int j = n; j<=c; j++)
		   {
			
			   table[j]=ttable[j];
		   }
		 //  for(int ii = 0; ii<=c; ii++){
		//	   cout<<table[ii]<<" ";
		 //  cout<<time;
		   
		 //  cout<<endl;
		}
		cout<<"Case #"<<tnum+1<<": "<<time<<endl;
	}
}


//Powered by [KawigiEdit] 2.0!