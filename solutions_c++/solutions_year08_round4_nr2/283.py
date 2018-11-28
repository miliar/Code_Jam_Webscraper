#include <iostream>

using namespace std;

int n, m, a;

bool work()
{
	int x1, y1, x2, y2;
	
	for (x1=0; x1<=n; x1++)
		for (x2=0; x2<=n; x2++)
			for (y1=0; y1<=m; y1++)	if (x1!=0 || y1!=0)
				for (y2=0; y2<=m; y2++)	if (x2!=0 || y2!=0)
					if ((x1!=x2 || y1!=y2))
						if (y1*x2-x1*y2==a){
							printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
							return true;
						}
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas=0, t;
	scanf("%d", &t);
	while (t--){
		cas++;
		printf("Case #%d: ", cas);
		scanf("%d%d%d", &n, &m, &a);
		if (!work())
			printf("IMPOSSIBLE\n");
	}
	return 0;	
}
