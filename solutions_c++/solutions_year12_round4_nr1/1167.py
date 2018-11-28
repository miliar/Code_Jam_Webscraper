#include<fstream>
#include<iomanip>
using namespace std;

const int maxn=10000;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("s.in");
	fout.open("s.out");
	int tr,rnd;

	int d[maxn],L[maxn],h[maxn];
	int n,m,i,j;

	fin>>tr;
	for (rnd=1;rnd<=tr;rnd++)
	{
	    fin>>n;
	    for (i=0;i<n;i++)
	    {
	        fin>>d[i]>>L[i];
	    }
	    fin>>m;
	    for (i=0;i<n;i++)
            h[i]=-1;
        h[0]=d[0];
        j=1;
        for (i=0;i<n;i++)
        {
            if (i>=j)
                break;
            while (j<n && h[i]+d[i]>=d[j])
            {
                if (L[j]<d[j]-d[i])
                    h[j]=L[j];
                else
                    h[j]=d[j]-d[i];
                j++;
            }
        }
        i=0;
        while (i<n && d[i]+h[i]<m)
            i++;
        fout<<"Case #"<<rnd<<": ";
        if (i>=n)
            fout<<"NO"<<endl;
        else
            fout<<"YES"<<endl;
    }

	fin.close();
	fout.close();
	return 0;
}
