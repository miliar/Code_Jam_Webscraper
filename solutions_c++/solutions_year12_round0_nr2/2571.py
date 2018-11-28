#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int T, n,s,p;
int good, surprise;

void main()
{
	freopen("B-large.in","r",stdin);
	//freopen("B.in","r",stdin);
	freopen("B2.out","w",stdout);

	scanf("%d",&T);
	int c=1;
	while(T--)
	{
		scanf("%d%d%d",&n,&s,&p);
		good = 0; surprise =0;
		while(n--)
		{
			int tmp;
			scanf("%d",&tmp);
			int m = tmp%3;
			int r;
			r=tmp/3;

			if(p==0&&tmp==0) {good++;continue;}
			if(p>0&&tmp==0){continue;}

			if(m==0)
			{
				if(r>=p)
				{good++;continue;}
				if(r+1>=p) surprise++;
				continue;
			}
			if(m==2)
			{
				if(r+1>=p)
				{good++;continue;}
				if(r+2>=p) surprise++;
				continue;
			}
			if(m==1)
			{
				if(r+1>=p) {good++;continue;}
				if(tmp>4)
				{
					r=(tmp-4)/3;
					if(r+2>=p){surprise++;continue;}
				}
			}
		}
		surprise = surprise <= s ? surprise:s;
		good += surprise;

		cout << "Case #" << c++ << ": " << good << endl;
	}
}