#include <fstream>
using namespace std;


ifstream fin("universe.in");
ofstream fout("universe.out");


long s,q,l=0,f[101],a[1001];
string name[101];

void init()
{
    memset(a,0,sizeof(a));
    memset(f,0,sizeof(f));
    fin>>s;
    l=0;
    getline(fin,name[0]);
    for (long i=1;i<=s;i++)
        getline(fin,name[i]);
    string str;
    fin>>q;
    getline(fin,str);
    for (long i=1;i<=q;i++)
    {
        getline(fin,str);
        for (long j=1;j<=s;j++)
            if (str==name[j])
                a[++l]=j;
    }
}

void dp()
{
    f[a[1]]=q+1;
    for (long i=2;i<=l;i++)
    {
        for (long j=1;j<=s;j++)
            if (f[a[i-1]]>f[j]+1)
            {
                f[a[i-1]]=f[j]+1;
            }
        f[a[i]]=q+1;
    }
    long min=(q==0?0:q-1);
    for (long i=1;i<=s;i++)
        if (f[i]<min)
            min=f[i];
    fout<<min<<endl;
}

int main()
{
	long n;
	fin>>n;
	for(long i=1;i<=n;i++)
	{
	    init();
	    fout<<"Case #"<<i<<": ";
	    dp();
	}
	return 0;
}
