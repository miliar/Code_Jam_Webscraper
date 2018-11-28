#include <stdio.h>
#include <algorithm>

int data[10000];

int main()
{
#if 1
	FILE* fp=fopen("c:\\b-small.in","r");
	FILE* fp2=fopen("c:\\b-small.txt","w");
#else
	FILE* fp=stdin;
	FILE* fp2=stdout;
#endif
	int T;
	fscanf(fp,"%d",&T);
	for (int tt=1; tt<=T; tt++)
	{
		printf("%d\n", tt);
		long long L,N,C;
		long long t;
		fscanf(fp,"%lld%lld%lld%lld",&L,&t,&N,&C);

		for (int i=0; i<C; i++)
		{
			fscanf(fp,"%d",&data[i]);
		}
		for (int i=C; i<N; i++)
		{
			data[i] = data[i-C];
		}

		// simulate
		long long rans = 0x7fFFffFFffFFffFF;
		long long ans = 0;
		long long tmp = 0;

		if (L == 2)
		{
			for (int l1 = 1; l1 < N; l1++)
			{
				for (int l2 = 0; l2 < l1; l2++)
				{
					ans = 0;
					for (int i=0; i<N; i++)
					{
						if (i == l1 || i == l2)
						{
							long long completed = std::max(t, ans);

							// completed - ans 시간만큼은 1/2로 달린다.
							// 그 외의 시간은 1로 달린다.

							if (completed - ans >= data[i] * 2) // 달릴동안 완성 안되면
							{
								ans += data[i] * 2;
							}
							else if (completed == ans) // 이미 완성되었으면
							{
								ans += data[i];
							}
							else
							{
								long long tmpans = ans;
								tmpans += (completed - ans); // 시간을 더한다
								if ((completed - ans) & 1) // 홀수면 1/2거리가 남는다.
								{
									tmp++;
									completed++;
								}
								tmpans += data[i] - (completed - ans) / 2;
								ans = tmpans;
							}
						}
						else
						{
							ans += data[i] * 2;
						}
					}
					ans += tmp / 2;
					rans = std::min(rans, ans);
					tmp = 0;
				}
			}
		}
		else if (L == 1)
		{
			for (int l2 = 0; l2 < N; l2++)
			{
				ans = 0;
				for (int i=0; i<N; i++)
				{
					if (i == l2)
					{
						long long completed = std::max(t, ans);

							// completed - ans 시간만큼은 1/2로 달린다.
							// 그 외의 시간은 1로 달린다.

							if (completed - ans >= data[i] * 2) // 달릴동안 완성 안되면
							{
								ans += data[i] * 2;
							}
							else if (completed == ans) // 이미 완성되었으면
							{
								ans += data[i];
							}
							else
							{
								long long tmpans = ans;
								tmpans += (completed - ans); // 시간을 더한다
								if ((completed - ans) & 1) // 홀수면 1/2거리가 남는다.
								{
									tmp++;
									completed++;
								}
								tmpans += data[i] - (completed - ans) / 2;
								ans = tmpans;
							}
					}
					else
					{
						ans += data[i] * 2;
					}
				}
				ans += tmp / 2;
				rans = std::min(rans, ans);
				tmp = 0;
			}
		}
		else
		{
			rans = 0;
			for (int i=0; i<N; i++)
			{
				rans += data[i] * 2;
			}
		}
		fprintf(fp2,"Case #%d: %lld\n", tt, rans);
	}
	return 0;
}