#include<fstream>
#include<string.h>
#define lmax 20
#define nrmax 5005
#define dmax 10000
using namespace std;
ifstream in("alien.in");
ofstream out("alien.out");
int n,l,m,ln,crt=1,nrl[nrmax],sol;
char cuv[nrmax][lmax],temp[lmax],test[dmax],mat[nrmax][5000];
int bun[lmax];
void conv()
{	int lg,i,j,ok=0;
	lg=strlen(test);
	for(i=0;i<lg;i++)
	{	if(test[i]=='(')
		{	ok=1;	
		}	
		if(test[i]==')')
		{	ok=0;
			crt++;
		}	
		if((ok==0)&&(test[i]!='(')&&(test[i]!=')'))
		{	nrl[crt]++;
			mat[crt][nrl[crt]]=test[i];
			crt++;
		}
		if((ok==1)&&(test[i]!='(')&&(test[i]!=')'))
		{	nrl[crt]++;
			mat[crt][nrl[crt]]=test[i];
		}	
	}
}
void solve()
{	int i,j,k,ok,z;
	for(k=1;k<=n;k++)
	{	ok=0;
		for(i=1;i<=l;i++)
		{	z=0;
			for(j=1;j<=nrl[i];j++)
			{	if((cuv[k][i-1]==mat[i][j])&&((i==1)||(ok==1)))
					z=1;
			}	
			if(z==1)ok=1;
			if(z==0)ok=0;
		}
		//out<<ok<<" ";
		if(ok==1)sol++;
	}
	out<<sol<<'\n';	
}
int main()
{	int i,j;
	in>>l>>n>>m;
	for(i=0;i<=n;i++)
	{	in.getline(cuv[i],lmax,'\n');
	}
	for(i=1;i<=m;i++)
	{	in.getline(test,dmax,'\n');
		conv();
		out<<"Case #"<<i<<": ";
		solve();
		crt=1;
		for(j=1;j<=nrmax;j++)
			nrl[j]=0;
		for(j=1;j<=lmax;j++)
			bun[j]=0;
	}	
	out.close();
	return 0;
}	