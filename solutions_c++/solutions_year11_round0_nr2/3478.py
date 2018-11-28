#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>

using namespace std;



int main() {
//  freopen("a.txt", "rt", stdin);
//#ifdef SMALL
/*  freopen("B-small.in", "rt", stdin);
  freopen("B-small.out", "wt", stdout);
/*#endif
#ifdef LARGE
 */ freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
//#endif

int t;
	cin>>t;
for(int test=0;test<t;test++)
{
int cv=0;
	cin>>cv;
//cout<<cv;
char c[40][3];
for(int i=0;i<cv;i++)
	for(int j=0;j<3;j++)
		{cin>>c[i][j];
			//cout<<c[i][j];
		}

	int dv=0;
 cin>>dv;
//cout<<dv;
char d[40][2];
for(int i=0;i<dv;i++)
	for(int j=0;j<2;j++)
		{cin>>d[i][j];
		//cout<<d[i][j];
		}
int n;
cin>>n;

char r[100];
char add;

cin>>r[0];


cout<<"Case #"<<test+1<<": ["; 
int rk=1;
for(int k=1;k<n;k++,rk++)
{
cin>>add;
//cout<<add;
for(int i=0;i<cv;i++)
{
		if(rk!=0 && r[rk-1]==c[i][0] && add==c[i][1]){rk-=1; add=c[i][2];}
		else if(rk!=0 && r[rk-1]==c[i][1] && add==c[i][0]){rk-=1; add=c[i][2];}
//	else r[rk]=add;
}

r[rk]=add;
//dissolve
			for(int p=0;p<rk;p++)
				for(int q=0;q<dv;q++)
	 				 if((r[p]==d[q][0] && r[rk]==d[q][1]) || (r[p]==d[q][1] && r[rk]==d[q][0])) 
						{
								rk=-1;
//								r[0]='\0';
						}
}
if(rk>0)
{
	cout<<r[0];
	for(int k=1;k<rk;k++)
		cout<<", "<<r[k];
}
cout<<"]\n";
}
return 0;
}
