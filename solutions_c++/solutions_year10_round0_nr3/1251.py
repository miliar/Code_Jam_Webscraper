#include<stdio.h>
#include<memory.h>
int R, K, N;
int group[1001];
int CutLine_Time[1001];
__int64 CutLine_Cost[1001];
__int64 total;
int main()
{
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int T, t;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		total = 0;
		memset(CutLine_Time,0,sizeof(CutLine_Time));
		memset(CutLine_Cost,0,sizeof(CutLine_Cost));

		scanf("%d %d %d",&R,&K,&N);
		int pt = 1;
		int i, people = 0;
		__int64 sum = 0;
		for(i=1;i<=N;i++){
			scanf("%d",&group[i]);
			sum += group[i];
		}
		if( sum <= K )
			total = sum * R;
		else
		{
			for(i=1;i<=R;i++)
			{
				while(1)
				{
					if(people + group[pt] <= K){
						people += group[pt];
						pt ++;
						if(pt > N) pt = 1;
					}

					else {
						total += people;
						people = 0;
						if(CutLine_Time[pt] != 0)
						{
							__int64 times = (R-i) / (i-CutLine_Time[pt]);
							total += times * (total - CutLine_Cost[pt]);
							i += (i-CutLine_Time[pt]) * times;
						}
						else{
							CutLine_Time[pt] = i;
							CutLine_Cost[pt] = total;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %I64d\n",t, total);
	}
	return 0;
}