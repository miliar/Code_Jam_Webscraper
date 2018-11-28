#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

class Snapper
{
    int status;
    int power;
public:
    int getpower()
    {
        return power;
    }
    int getstatus()
    {
        return status;
    }
    void setpower(int p)
    {
        power=p;
    }
    void setstatus(int s)
    {
        status=s;
    }
    Snapper()
    {
        status=0;
        power=0;
    }
    void toggle()
    {
            if(status==1)
                status=0;
            else 
                status=1;
    }
};
int main()
{
    freopen("A-small-attempt1.in","rt",stdin);
	freopen("A.out","wt",stdout);
    int T;
    scanf("%d",&T);
    
   
    for (int ii = 1; ii <= T; ++ii) 
    {
	    int n, k;
	    scanf("%d",&n);
	    scanf("%d",&k);
        Snapper snapper[10001];
        snapper[1].setpower(1);
        for(int kk=1;kk<=k;kk++)
        {
            for(int nn=1;nn<=n;nn++)
            {
                if(snapper[nn].getpower()==1)
                    snapper[nn].toggle();
            }
            for(int nn=1;nn<n;nn++)
            {
                if(snapper[nn].getpower()==1 && snapper[nn].getstatus()==1)
                    snapper[nn+1].setpower(1);
               else
                    snapper[nn+1].setpower(0);
            }
        }
		printf("Case #%d: ",ii);
        
        if(snapper[n].getpower()==1 && snapper[n].getstatus()==1)
            printf("ON\n");
        else
            printf("OFF\n");
	}
	return 0;
}