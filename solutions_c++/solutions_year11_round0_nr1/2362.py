#include <fstream>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.out");
//#include<iostream>

int t,o,e,a[102],b[102],f[102][102][102],n,m,maxx=1000000000,q[2000000][3],qe,qb;
string s;
int main()
{
    cin >> t;
    o=0;
    while (o<t)
	{
	    o++;
	    cin >> n;
	    m=0;
	    for (int i=0; i<n; i++)
		{
		    cin >> s >> e;
		    a[m]=e;
		    if (s[0]=='B') b[m]=1; else b[m]=0;
		    m++;
		}
	    for (int i=0; i<101; i++)
		for (int j=0; j<101; j++) 
		    for (int k=0; k<101; k++)
			f[i][j][k]=maxx;
	    f[1][1][0]=0;
	    q[0][0]=1;
	    q[0][1]=1;
	    q[0][2]=0;
	    qe=1;
	    qb=0;
	    int i,j,k;
	    while (qe>qb)
		{
		    i=q[qb][0];
		    j=q[qb][1];
		    k=q[qb][2];
		    e=f[i][j][k];
		    qb++;
		    if (i>100 || j>100 || k>=m || i<1 || j<1) continue;
		    if (f[i+1][j][k]>e+1) {f[i+1][j][k]=e+1; q[qe][0]=i+1; q[qe][1]=j; q[qe][2]=k; qe++;};
		    if (f[i][j+1][k]>e+1) {f[i][j+1][k]=e+1; q[qe][0]=i; q[qe][1]=j+1; q[qe][2]=k; qe++;}
		    if (f[i+1][j+1][k]>e+1) {f[i+1][j+1][k]=e+1; q[qe][0]=i+1; q[qe][1]=j+1; q[qe][2]=k; qe++;}
		    if (f[i+1][j-1][k]>e+1) {f[i+1][j-1][k]=e+1; q[qe][0]=i+1; q[qe][1]=j-1; q[qe][2]=k; qe++;}
		    if (f[i-1][j+1][k]>e+1) {f[i-1][j+1][k]=e+1; q[qe][0]=i-1; q[qe][1]=j+1; q[qe][2]=k; qe++;}
		    if (f[i-1][j][k]>e+1) {f[i-1][j][k]=e+1; q[qe][0]=i-1; q[qe][1]=j; q[qe][2]=k; qe++;}
		    if (f[i][j-1][k]>e+1) {f[i][j-1][k]=e+1; q[qe][0]=i; q[qe][1]=j-1; q[qe][2]=k; qe++;};
		    if (f[i-1][j-1][k]>e+1) {f[i-1][j-1][k]=e+1; q[qe][0]=i-1; q[qe][1]=j-1; q[qe][2]=k; qe++;}
		    if (b[k]==0 && a[k]==i)
			{
			    if (f[i][j][k+1]>e+1) {f[i][j][k+1]=e+1; q[qe][0]=i; q[qe][1]=j; q[qe][2]=k+1; qe++;}
			    if (f[i][j+1][k+1]>e+1) {f[i][j+1][k+1]=e+1; q[qe][0]=i; q[qe][1]=j+1; q[qe][2]=k+1; qe++;}
			    if (f[i][j-1][k+1]>e+1) {f[i][j-1][k+1]=e+1; q[qe][0]=i; q[qe][1]=j-1; q[qe][2]=k+1; qe++;}
			}
		    if (b[k]==1 && a[k]==j)
			{
			    if (f[i][j][k+1]>e+1) {f[i][j][k+1]=e+1; q[qe][0]=i; q[qe][1]=j; q[qe][2]=k+1; qe++;}
			    if (f[i+1][j][k+1]>e+1) {f[i+1][j][k+1]=e+1; q[qe][0]=i+1; q[qe][1]=j; q[qe][2]=k+1; qe++;}
			    if (f[i-1][j][k+1]>e+1) {f[i-1][j][k+1]=e+1; q[qe][0]=i-1; q[qe][1]=j; q[qe][2]=k+1; qe++;}
			}
		}
	    e=maxx;
	    for (int i=1; i<101; i++)
		for (int j=1; j<101; j++)
		    if (e>f[i][j][m]) e=f[i][j][m];
	    cout << "Case #" << o << ": " << e << endl;
	}
    return 0;
}
