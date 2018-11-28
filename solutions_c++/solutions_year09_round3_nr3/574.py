#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <stdio.h>

using namespace std;
vector<vector<int> > dp;
vector<int> pr;

int req(int min, int max)
{
    if(dp[min][max]>0)
    {
        return dp[min][max];
    }
    if(max==min+1)
    {
        return 0;
    }
    int res=pr[max]-pr[min]-1-1;
    int best=32768;
    for(int i=min+1;i<max;++i)
    {
        int tmp=0;
        tmp+=req(min,i);
        tmp+=req(i,max);
        if(tmp<best) best=tmp;
    }
    res+=best;
    dp[min][max]=res;
    return res;
}

int main(int argc, char ** argv)
{
	int N;
	ifstream f(argv[1]);
	f >> N ;
		
	for(int n=0; n<N; ++n)
	{
        int P,Q;
        f>>P;
        f>>Q;
        dp.resize(Q+2);
        for(int i=0; i<dp.size(); ++i)
		{
            dp[i].resize(Q+2);
            for(int j=0; j<Q+2; ++j)
		    {
                dp[i][j]=-1;
            }
        }

        pr.resize(Q+2);
        pr[0]=0;
        pr[Q+1]=P+1;
       for(int i=0; i<Q; ++i)
		{
            f>>pr[i+1];
        }

        printf("Case #%d: %d\n",n+1,req(0,Q+1));

        for(int i=0; i<dp.size(); ++i)
		{
            dp[i].clear();
        }

        dp.clear();

        pr.clear();

	}


	return 0;
}
