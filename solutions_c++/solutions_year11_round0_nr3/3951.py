/*


*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int T;
	int casen = 1;

	freopen("C-small-attempt0.in.txt", "r", stdin);
	freopen("C-small-attempt0.out.txt", "w", stdout);

	scanf("%ld", &T);
	while (T--)
	{
		int n, c[15];
		int i, j;
		int ans, cs, cp, rs, rp;

		scanf("%d", &n);
		for (i=0; i<n; i++)
			scanf("%d", c+i);

		// Process_data(c, n);  //�Ż�1(ȥ����ͬ����,һ����S).����n=15,����������ν�ˡ���
		ans = -1;
		for (i=(1<<n)-2; i>0; i--) //ö�٣����������Ӽ�
		{
			cs = cp = 0;
			rs = rp = 0;
			for (j=0; j<n; j++)
				if ( ((1<<j)&i) != 0) //�ж�i�ĵ�jλ�ǲ���1,�����,��ʾ���ǹ���S
				{
					cs ^= c[j];
					rs += c[j];
				}
				else
				{
					cp ^= c[j];
					rp += c[j];
				}

			if (cs == cp)   // �Ż�2�����öԳ��ԣ���ʵѭ��ֻ��Ҫ��i>=( 1<<(n-1) )���ɣ���ֻ������Ƚϵ�ʱ���rp����
				ans = rs > ans ? rs : ans;
		}

		if (ans == -1) printf("Case #%d: NO\n", casen++);
		else printf("Case #%d: %d\n", casen++, ans);
	}

	return 0;
}

/*
Input:

2
5
1 2 3 4 5
3
3 5 6

*/