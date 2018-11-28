#include <cstdio>

int absx(int p)
{
	if (p < 0) return -p; else return p;
}

int main()
{
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int t, n;

    scanf("%d", &t);
	for (int i = 0; i < t; i++) {
        scanf("%d", &n);
		char tmp, robot;
		int p;
		int count = 0;
		int p1 = 1;
     	int p2 = 1;
	    int l1 = 0;
	    int l2 = 0;
	
		for (int j = 0; j < n; j++) {
			scanf("%c%c%d", &tmp, &robot, &p);
			if (robot == 'O') {
				if (absx(p - p1) <= count - l1) {
					count++;
				    l1 = count;
			    } else {
                    count = l1 + absx(p - p1);
					count++;
					l1 = count;
			    } 
				p1 = p;
			} else {
				if (robot == 'B') {
					if (absx(p - p2) <= count - l2) {
						count++;
						l2 = count;
					} else {
						count = l2 + absx(p - p2);
						count++;
						l2 = count;
					}
				}
				p2 = p;
			}
		}
		printf("Case #%d: %d\n", i + 1, count);
	}

	return 0;
}