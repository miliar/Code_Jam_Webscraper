#include <stdio.h>
#include <algorithm>
using namespace std;


char cmd[5];

int main()
{
	int t;
	int n, pos;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test)
	{
		scanf("%d", &n);
		int ans = 0;
		int leftB = 0;
		int leftO = 0;
		int posB = 1;
		int posO = 1;

		//��ǰһ������ִ��ǰ����һ������ֻ�ܵ���ָ��λ�õȴ�
		//Ϊÿ�������˼�¼һ��ʱ��t����ʾ�û����˻���t��û��
		for (int i = 0; i < n; ++i)
		{
			scanf("%s%d", cmd, &pos);
			if ('O' == cmd[0])
			{
				int temp = abs(posO - pos) - leftO;
				//����
				if (temp <= 0)
				{
					ans += 1;
					leftB += 1;
				}
				else
				{
					ans += temp + 1;
					leftB += temp + 1;
				}
				posO = pos;
				leftO = 0;
			}
			else if ('B' == cmd[0])
			{

				int temp = abs(posB - pos) - leftB;
				//����
				if (temp <= 0)
				{
					ans += 1;
					leftO += 1;
				}
				else
				{
					ans += temp + 1;
					leftO += temp + 1;
				}
				posB = pos;
				leftB = 0;
			}

		}

		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}