#include <set>
#include <cstdio>
#include <cstring>
using namespace std;

set <pair <int, int> > s;

int main()
{
    FILE *fin = fopen("C-large.in","r");
    FILE *fout = fopen("C-large.out","w");

    int T;
    int a, b;
    int n, m, sz;

    fscanf(fin, " %d ", &T);
    for(int t = 1; t <= T; t++)
    {
        s.clear();
        fscanf(fin, " %d %d ", &a, &b);

        sz = 1;
        int temp =  a;
        while(temp)
        {
	sz*=10;
	temp/=10;
        }

        int temp2;
        for(n = a; n < b; n++)
        {
	for(temp = 10, temp2 = sz/10; temp < sz; temp*=10, temp2/=10)
	{
	    m = n/temp + (n%temp)*temp2;
	    if(n < m && m <= b)
	        s.insert(pair <int, int>(n, m));
	}
        }

        fprintf(fout, "Case #%d: %d\n", t, s.size());
        printf("Case #%d: %d\n", t, s.size());
 //       for(set<pair<int, int> >::iterator it = s.begin();it!=s.end();it++)
	//fprintf(fout, "%d\t%d\n", it->first,it->second);

    }
    return 0;
}
