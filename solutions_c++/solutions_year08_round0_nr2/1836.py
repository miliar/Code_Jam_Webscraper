#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>

#define pb push_back

using namespace std;

void swap(int *a,int i,int j)
{
	int temp = a[i];
	a[i]=a[j];
	a[j]=temp;
	return;
}

int main()
{
	int num,N;
	scanf("%d",&num);
	for(N=0;N<num;N++)
	{
		int av[2]={0},re[2]={0},i,j,k,n[2],arh,arm,deh,dem,t;
		int vi1[1000],vi2[1000],vi3[1000],cnt=0;
		pair<int,int> pi;
		vector<pair<int,int> > vp[2];

		scanf("%d %d %d",&t,&n[0],&n[1]);
//		printf("%d %d %d\n",t,n[0],n[1]);
		for(j=0;j<2;j++)
			for(i=0;i<n[j];i++)
			{
				scanf("%d:%d %d:%d",&arh,&arm,&deh,&dem);
				pi.first = arh*60 + arm;
				pi.second = deh*60 + dem;
//				printf("%d %d %d %d %d %d %d\n",arh,arm,deh,dem,pi.first,pi.second);
				vp[j].pb(pi);
			}
		sort(vp[0].begin(),vp[0].end());
		sort(vp[1].begin(),vp[1].end());
		for(j=0;j<2;j++)
			for(i=0;i<n[j];i++)
			{
				vi1[cnt] = vp[j][i].first;
				vi2[cnt] = j;
				vi3[cnt++] = 0;
				vi1[cnt] = vp[j][i].second+t;
				vi2[cnt] = j;
				vi3[cnt++] = 1;
			}
		for(i=0;i<cnt;i++)
			for(j=i+1;j<cnt;j++)
				if(vi1[i]>vi1[j] || (vi1[i]==vi1[j] && vi3[i]<vi3[j]))
				{
					swap(vi1,i,j);
					swap(vi2,i,j);
					swap(vi3,i,j);
				}
		for(i=0;i<cnt;i++)
		{
//			printf("%d %d %d\n",vi1[i],vi2[i],vi3[i]);
			if(vi3[i]==0)
			{
				if(av[vi2[i]]==0)
					re[vi2[i]]++;
				else av[vi2[i]]--;
			}
			else av[1-vi2[i]]++;
//			printf("%d %d %d %d\n",av[0],av[1],re[0],re[1]);
		}
		printf("Case #%d: %d %d\n",N+1,re[0],re[1]);
	}
	return 0;
}
