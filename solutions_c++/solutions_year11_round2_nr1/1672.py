#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

void solve(int t)
{
int i,j,k,l,N;
char str[200];
int R[100][100];
int WC[100];
int GC[100];
double WP[100];
double OWP[100];
double OOWP[100];
cin >> N;
for(i=0;i<N;i++)
{
cin>>str;
for(j=0;j<N;j++)
R[i][j]=str[j];
}

//win count and game count
for(i=0;i<N;i++)
{
	WC[i]=0;
	GC[i]=0;
	for(j=0;j<N;j++)
	{
		if(R[i][j]=='0')GC[i]++;
		else if(R[i][j]=='1'){GC[i]++;WC[i]++;}
	}
}

int OC;
for(i=0;i<N;i++)
{
	WP[i] = GC[i] ? (double)WC[i]/(double)GC[i] : 0;
	OWP[i] = 0;
	OC=0;
	for(j=0;j<N;j++)
	{
		int temp1, temp2;
		if(i==j) continue;
		if(R[i][j]=='.') continue;
		temp1=WC[j];
		temp2=GC[j];
		if(R[j][i]=='1'){temp1--;temp2--;}
		else if(R[j][i]=='0')temp2 = temp2>0?temp2-1:0;
		OWP[i] += temp2 ? (double)temp1/double(temp2) : 0;
		OC++;
	}
	OWP[i] = OWP[i]/OC;
}

for(i=0;i<N;i++)
{
	OOWP[i]=0;
	OC=0;
	for(j=0;j<N;j++)
	{
		if(i==j)continue;
		if(R[i][j]!='.'){OOWP[i]+=OWP[j];OC++;}
	}
	OOWP[i] = OOWP[i]/(double)OC;

}

//#define DEBUG
#ifdef DEBUG
for(i=0;i<N;i++)
cout << WP[i] << " " << OWP[i] << " " << OOWP[i] << endl;
#endif

cout << "Case #" << t << ":" <<endl;
for(i=0;i<N;i++)
cout << (WP[i]*0.25 + OWP[i]*0.5 + OOWP[i]*0.25)<<endl;
//printf("%lf\n",(WP[i]*0.25 + OWP[i]*0.5 + OOWP[i]*0.25));
}

int main()
{
int i, T;
cin >> T;
for(i=1;i<=T;i++)solve(i);
}
