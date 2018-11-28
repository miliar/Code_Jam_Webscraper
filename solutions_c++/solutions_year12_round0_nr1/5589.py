#include<fstream>
#include<cstring>
using namespace std;
#define SMAX 200

int n;
char s[SMAX];
char translation[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

void read_solve()
{
 int i,j;
 ifstream fin("A-small.in");
 ofstream fout("A-small.txt");

 fin>>n;
 fin.get();
 for (i=1; i<=n; ++i)
	{
	 fin.get(s, SMAX);
	 fin.get();

	 fout<<"Case #"<<i<<": ";
	 for (j=0; j<(int)strlen(s); ++j)
		 if (s[j] == ' ')
			 fout<<" ";
		 else
			 fout<<translation[s[j] - 'a'];
	 fout<<'\n';
	}

 fin.close();
 fout.close();
}

int main()
{
 read_solve();
 return 0;
}
