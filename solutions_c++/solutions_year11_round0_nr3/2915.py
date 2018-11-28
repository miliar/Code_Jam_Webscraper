#include <iostream>
#include <cstdio>
#include <list>
#include <map>

int abs(int a){return a<0?-a:a;}
void maxify(int& a,int b){if (b>=a) a=b;}
void minify(int& a,int b){if (b<=a) a=b;}

/*
011 101 110

011 101
011     110
    101 110

*/

int msb(int q)
{
	int r=0;
	while (q)
		q>>=1,
		r++;
	return r;
}

std::list<int> xl[40];
int total;

int best=-1;
void solve(int l,int r,int d=39,int s=0)
{
	if (d<0){
		if (l==r && s!=total)
			maxify(best,s);
		return;}

	if (xl[d].empty()){
		if ( (l&(1<<d))==(r&(1<<d))	)
			solve(l,r,d-1,s);
		return;}

	int q=xl[d].front();
	xl[d].pop_front();
	solve(l^q,r,d,s+q);
	solve(l,r^q,d,s);
	xl[d].push_front(q);
	return;
}

int main(void)
{
	if (freopen("candysplit.in","r",stdin));

	std::map<int,int> dp;
	dp[0]=0;

	int tests;
	std::cin>>tests;
	for (int z=0; z<tests; z++)
	{
		int count;
		std::cin>>count;

		for (int i=0; i<40; i++)
			xl[i].clear();

		best=-1;
		total=0;
		int val[count];
		for (int i=0; i<count; i++){
			std::cin>>val[i];
			total+=val[i];
			xl[msb(val[i])].push_back(val[i]);
		}
		solve(0,0);
		std::cout<<"Case #"<<z+1<<": ";
		if (best==-1)	std::cout<<"NO"<<std::endl;
		else			std::cout<<best<<std::endl;

/*
		int dp[count+1][20][2];
		for (int i=0; i<=count; i++)
			for (int j=0; j<20; j++)
				for (int k=0; k<2; k++)
					dp[i][j][k]=-k;

		for (int i=0; i<count; i++)
			for (int j=0,s=1; j<20; j++,s<<=1)
				if (val[i]&s){
					for (int k=0; k<2; k++)
						if (dp[i][j][k]!=-1)
							maxify(dp[i+1][j][!k],dp[i][j][k]+val[i]),
							maxify(dp[i+1][j][ k],dp[i][j][k]);
				}else{
					for (int k=0; k<2; k++)
						maxify(dp[i+1][j][k],dp[i][j][k]+val[i]);
				}

		std::cout<<dp[count][0][1]<<std::endl;
		std::cout<<dp[count][1][1]<<std::endl;
		std::cout<<dp[count][2][1]<<std::endl;
		std::cout<<dp[count][3][1]<<std::endl;
*/
/*		int xorall=0;
		int total=0;

		int nuhuh=0x8000000;
		int lowest=nuhuh;
		int val[count];
		for (int i=0; i<count; i++)
		{
			std::cin>>val[i];
			xorall^=val[i];
			total+=val[i];

			std::map<int,int> odp=dp;
			for (std::map<int,int>::iterator it=odp.begin(); it!=odp.end(); it++)
				maxify(dp[(*it).first^val[i]],(*it).second+val[i]),
				minify(lowest,dp[(*it).first^val[i]]);
		}

		int best=lowest;
		maxify(best,total-best);

		std::cout<<"Case #"<<z+1<<": ";
		if (xorall!=0 || best==nuhuh)
			std::cout<<"NO"<<std::endl;
		else
			std::cout<<best<<std::endl;
*/
//		std::cout<<best<<std::endl;
	}
}

/*
 0001 0010 0001 0100 0011 0101

 0001      0001      0011 0101
      0010           0011
                0100      0101
*/
