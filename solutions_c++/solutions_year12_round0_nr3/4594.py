#include<fstream>
#include<cstring>
using namespace std;
#define SMAX 100

int t,a,b,acopy,bcopy;
int lgs;
char s[SMAX];
long long sol;
int elem[20],nrelem;

void transform_string(int x)
{
 int i;
 char aux;
 lgs = -1;
 s[10] = '\0';

 while (x != 0)
	{
	 lgs++;
	 s[lgs] = x % 10 + '0';
	 x /= 10;
	}
 s[lgs + 1] = '\0';

 for (i=0; i<(lgs+1)/2; ++i)
	{
	 aux = s[i];
	 s[i] = s[lgs - i];
	 s[lgs - i] = aux;
	}
}

void transform_nmb(int x)
{
 int i,nr=0,ok = 1;

 for (i=0; i<=lgs; ++i)
	 nr = nr * 10 + (s[i] - '0');
 if (acopy <= nr && nr <= bcopy && x < nr)
	{
	 for (i=0; i<=nrelem; ++i)
		 if (elem[nrelem] == nr)
			{
			 ok = 0;
			 break;
			}
	 if (ok == 1)
		{
		 nrelem++;
		 elem[nrelem] = nr;
		 sol++;
		}
	}
}

void solve()
{
 int i,j,k;
 char aux;

 for (i=acopy; i<=bcopy; ++i)
	{
	 transform_string(i);
	 nrelem = 0;
	 for (j=0; j<lgs; ++j)
		{
		 aux = s[lgs];
		 for (k=lgs; k>=1; --k)
			 s[k] = s[k-1];
		 s[0] = aux;

		 if (aux != '0')
			 transform_nmb(i);
		}
	}
}

void read()
{
 int i;
 ifstream fin("C.in");
 ofstream fout("C.txt");

 fin>>t;
 for (i=1; i<=t; ++i)
	{
	 fin>>a>>b;
	 acopy = a; bcopy = b;
	 solve();
	 fout<<"Case #"<<i<<": "<<sol<<'\n';
	 sol = 0;
	}

 fin.close();
 fout.close();
}

int main()
{
 read();
 return 0;
}
