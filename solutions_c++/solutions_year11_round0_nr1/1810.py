#include<cstdio>
#include<cstdlib>
#include<cstring>

int main()
{
	int T, cas;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int i, j, k, N;
		char ch[10];
		int btn[101];
		int pre[2], preRec[101];
		int preId[2], preIdRec[101];
		scanf("%d", &N);
		pre[0] = pre[1] = 1;
		preId[0] = preId[1] = -1;
		memset(preRec, -1, sizeof(preRec));
		for(i = 0; i < N; i ++)
		{
			scanf("%s %d", ch, &btn[i]);
			if(ch[0] == 'B')
			{
				preRec[i] = pre[1];
				preIdRec[i] = preId[1];
				pre[1] = btn[i];
				preId[1] = i;
			}
			else {
				preRec[i] = pre[0];
				preIdRec[i] = preId[0];
				pre[0] = btn[i];
				preId[0] = i;
			}
		}
		
		int ans[101];
		
		for(i = 0; i < N; i ++)
		{
			ans[i] = abs(btn[i] - preRec[i])+1;
			if(preIdRec[i] != -1)
			{
				ans[i] += ans[preIdRec[i]];
			}
			if(i > 0)
			{
				if(ans[i-1]+1 > ans[i])ans[i] = ans[i-1]+1;
			}
		}
		printf("Case #%d: %d\n", cas, ans[N-1]);
	}
	return 0;
}
