#include <fstream>
#include <string>

using namespace std;
ifstream fin("input.in");
ofstream fout("output.out");


int main()
{
	int n,s,p;
	int cases;
	int i,j;
    int ans;
	int score,best;
	int on_boundary;
	fin>>cases;
	
	for (i=1;i<=cases;i++)
	{
		fin>>n>>s>>p;
	    ans=0;
		on_boundary=0;

		for (j=1;j<=n;j++)
		{
			fin>>score;
			if (score % 3==0) best=score/3;
			 else if (score % 3==1) best=(score+2)/3;
			 else best=(score+1)/3;
            if (best>=p) ans++;
			if (best+1==p && (score % 3)!=1 && score>=2 && score<=28) on_boundary++;
		}
		if (on_boundary>=s) ans+=s;
		else ans +=on_boundary;

		fout<<"Case #"<<i<<": "<<ans<<endl;
	}

	return 0;
}
