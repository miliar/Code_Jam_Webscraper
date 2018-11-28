#include<cstdio>
#include<vector>
#include<algorithm>
#include<utility>

using namespace std;

#define PB push_back
#define ST first
#define ND second
#define MP make_pair

int kolejka[1001];
long long sumy[2002];
pair<int,long long> vst[1001];

int main()
{
	int z, asdf;
	scanf("%d",&z);
	asdf=z;
	while(z--)
	{
		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);
		for(int i=0;i<N;i++)
			scanf("%d",kolejka+i);
		for(int i=0;i<N;i++)
			vst[i].ST=vst[i].ND=0;
		if(N==1)
		{
			printf("Case #%d: %Ld\n", asdf-z, R*kolejka[0]);
		}
		else
		{
			sumy[0]=0;
			for(int i=1;i<2*N;i++)
				sumy[i]=sumy[i-1]+kolejka[(i-1)%N];
			long long count=0;
			int left=1, right=N, p;
			int X=R;
			while(R>0)
			{
				p=(left-1)%N;
				if (vst[p].ST!=0)
				{
					int zostalo = R;
					int ile = X - zostalo - vst[p].ST + 1;
					long long koszt = count - vst[p].ND;
					int lol = (zostalo-zostalo%ile);
					//printf("KRASZ na %d %d %d %d %d",p,zostalo, ile, koszt, lol);
					R-=lol;
					count+=lol/ile*koszt;
					break;
				}
				else
				{
					R--;
					vst[p]=MP(X-R,count);
					int index = lower_bound(sumy+left, sumy+right, k+sumy[left-1]) - sumy;
					if ( sumy[index]>k+sumy[left-1]) index--;
					//printf("%d %d %d %d\n",index,left,right,count);
					count+=sumy[index]-sumy[left-1];
					left=index+1;
					right=left+N;
					while(right-1>2*N)
					{
						left-=N;
						right-=N;
					}
				}
			}
			while(R>0)
			{
				int index = lower_bound(sumy+left, sumy+right, k+sumy[left-1]) - sumy;
				if ( sumy[index]>k+sumy[left-1]) index--;
				count+=sumy[index]-sumy[left-1];
				left=index+1;
				right=left+N+1;
				while(right-1>2*N)
				{
					left-=N;
					right-=N;
				}
				R--;
			}
			printf("Case #%d: %Ld\n", asdf-z, count);
		}
	}
	return 0;
}
