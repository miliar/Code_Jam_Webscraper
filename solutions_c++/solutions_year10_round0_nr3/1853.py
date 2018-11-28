#include <iostream>
#include <fstream>

using namespace std;

typedef __int64 LINT;

void main()
{
	ifstream ifs("C-large.in");
	ofstream ofs("C-large.out");

	int g[1000];
	int v[1000];
	int euro[1000];
	int ord[1001];

	int t,r,n,k;
	int ii,i,j;
	ifs>>t;
	for(ii=0; ii<t; ii++)
	{
		ifs>>r>>k>>n;
		for(i=0; i<n; i++)
			ifs>>g[i];

		LINT gsum=0;
		for(i=0; i<n; i++)
			gsum+=g[i];
		if(gsum<=k)
		{
			ofs<<"Case #"<<ii+1<<": "<<gsum*r<<endl;
			continue;
		}

		for(i=0; i<n; i++)
			ord[i]=v[i]=euro[i]=0;

		ord[0]=0;
		for(i=0; ; i++)
		{
			v[ord[i]]=i+1;
			for(j=ord[i]; ;j++)
			{
				if(j>=n)
					j=0;
				if(euro[i]+g[j]>k)
					break;
				euro[i]+=g[j];
			}
			if(v[j]>0)
				break;
			ord[i+1]=j;
		}
		int ll=v[j]-1;
		int cyc=i-ll+1;
		LINT sum=0;

		if(r<=ll)
		{
			for(i=0; i<r; i++)
				sum+=euro[i];
		}
		else
		{
			for(i=0; i<ll; i++)
				sum+=euro[i];
			r-=ll;

			for(i=ll; i<ll+r%cyc; i++)
				sum+=euro[i];

			LINT lsum=0;
			for(i=ll; i<ll+cyc; i++)
				lsum+=euro[i];
			
			sum+= r/cyc * lsum;
		}
		ofs<<"Case #"<<ii+1<<": "<<sum<<endl;
	}
}
