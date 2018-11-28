#include <fstream>
#include <vector>
#include <string>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int t;
int r,c,d;
vector <string> s;
int k;
vector <vector <long long int> > m,nr,nc;
long long int x,yr,yc;
int main()
{
	in >> t;
	for (int nt=1;nt<=t;nt++)
	{
		k=-1;
		in >> r >> c >> d;
		s.resize(r);
		for (int i=0;i<r;i++) in >> s[i];
		m.resize(r);
		nr.resize(r);
		nc.resize(r);
		for (int i=0;i<r;i++)
		{
			m[i].assign(c,0);
			nr[i].assign(c,0);
			nc[i].assign(c,0);
		}
		m[0][0]=s[0][0]-'0';
		nr[0][0]=0;
		nc[0][0]=0;
		for (int i=1;i<c;i++)
		{
			m[0][i]=m[0][i-1]+s[0][i]-'0';
			nr[0][i]=0;
			nc[0][i]=nc[0][i-1]+i*(s[0][i]-'0');
		}
		for (int i=1;i<r;i++)
		{
			m[i][0]=m[i-1][0]+s[i][0]-'0';
			nr[i][0]=nr[i-1][0]+i*(s[i][0]-'0');
			nc[i][0]=0;
		}
		for (int i=1;i<r;i++) for (int j=1;j<c;j++)
		{
			m[i][j]=m[i-1][j]+m[i][j-1]-m[i-1][j-1]+s[i][j]-'0';
			nr[i][j]=nr[i-1][j]+nr[i][j-1]-nr[i-1][j-1]+i*(s[i][j]-'0');
			nc[i][j]=nc[i-1][j]+nc[i][j-1]-nc[i-1][j-1]+j*(s[i][j]-'0');
		}
		for (int h=3;h<=min(r,c);h++) for (int i=0;i<=r-h;i++) for (int j=0;j<=c-h;j++)
		{
			x=m[h+i-1][h+j-1];
			if (i>0) x-=m[i-1][h+j-1];
			if (j>0) x-=m[h+i-1][j-1];
			if (i>0 && j>0) x+=m[i-1][j-1];
			x-=s[i][j]-'0'+s[i+h-1][j]-'0'+s[i][j+h-1]-'0'+s[i+h-1][j+h-1]-'0';
			yr=nr[h+i-1][h+j-1];
			if (i>0) yr-=nr[i-1][h+j-1];
			if (j>0) yr-=nr[h+i-1][j-1];
			if (i>0 && j>0) yr+=nr[i-1][j-1];
			yr-=i*(s[i][j]-'0')+(i+h-1)*(s[i+h-1][j]-'0')+i*(s[i][j+h-1]-'0')+(i+h-1)*(s[i+h-1][j+h-1]-'0');
			yc=nc[h+i-1][h+j-1];
			if (i>0) yc-=nc[i-1][h+j-1];
			if (j>0) yc-=nc[h+i-1][j-1];
			if (i>0 && j>0) yc+=nc[i-1][j-1];
			yc-=j*(s[i][j]-'0')+j*(s[i+h-1][j]-'0')+(j+h-1)*(s[i][j+h-1]-'0')+(j+h-1)*(s[i+h-1][j+h-1]-'0');
			if (x*(2*i+h-1)==yr*2 && x*(2*j+h-1)==yc*2) k=h;
		}
		out << "Case #" << nt << ": ";
		if (k==-1) out << "IMPOSSIBLE";
		else out << k;
		out << "\n";
	}
	return 0;
}
