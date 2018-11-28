#include <stdio.h>
#include <math.h>


int main()
{
	FILE* fp=fopen("c:\\a-large.in","r");
	FILE* fp2=fopen("c:\\a-large.txt","w");

	int T;
	fscanf(fp,"%d",&T);
	for (int t=1; t<=T; t++)
	{
		int n;
		int ans = 0;
		int op = 1, bp = 1;
		int ot = 0, bt = 0;
		fscanf(fp, "%d", &n);

		for (int i=0; i<n; i++)
		{
			char robot;
			int pos;
			fscanf(fp, " %c%d", &robot, &pos);

			if (robot == 'O')
			{
				// 예전 위치와 지금 위치가 총 흘러간 시간의 차이보다 작으면
				// 1만 더하면 될듯
				if (ans - ot > abs(pos - op))
				{
					ans++;
				}
				else
				{
					// 갈 수 있는 거리: ans - ot
					ans += abs(pos - op) - (ans - ot) + 1;
				}
				op = pos;
				ot = ans;
			}
			else
			{
				if (ans - bt > abs(pos - bp))
				{
					ans++;
				}
				else
				{
					ans += abs(pos - bp) - (ans - bt) + 1;
				}
				bp = pos;
				bt = ans;
			}
		}
		fprintf(fp2, "Case #%d: %d\n",t, ans);
	}
	return 0;
}