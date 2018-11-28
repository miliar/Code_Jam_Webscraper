#include <iostream>
using namespace std;

int main(void)
{
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("C-small-attempt0.out.txt","w",stdout);
	int nCase;
	scanf("%d", &nCase);

	for (int i = 1; i <= nCase; ++i)
	{
		int room, cnt, gNum;
		scanf("%d %d %d", &cnt, &room, &gNum);
		int* groups = new int[gNum];
		for (int j = 0; j < gNum; ++j)
		{
			scanf("%d", groups+j);
		}

		int total = 0;
		int head = 0;
		while (cnt--)
		{
			int remain = room;
			int flag = head;
			while (remain >= groups[head])
			{
				remain -= groups[head];
				head = (head+1) % gNum;
				if (head == flag)
					break;
			}
			total += room - remain;
		}

		printf("Case #%d: %d\n", i, total);
	}

	return 0;
}