#include <algorithm>
using namespace std;
 
main()
{
    int tn, ti, i;
    char s[1024], s2[1024];
    scanf("%d\n", &tn);
    for (ti = 1; ti <= tn; ti++) {
    	gets(s);
    	strcpy(s2, s);
		int l;
		for (l = 0; s[l] >= '0' && s[l] <= '9'; l++);		
		printf("Case #%d: ", ti);
		if (next_permutation(s, s+l)) {
			puts(s);	
		} else {
			for (i = l+3; i >= 0; i--) s2[i+1] = s2[i];
			s2[0] = '0';
			next_permutation(s2, s2+l+1);
			puts(s2);
		}
    }
    return 0;
}