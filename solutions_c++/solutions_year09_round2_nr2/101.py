#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char buf[1024];

int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);


	scanf("%s", buf);
        int len = strlen(buf);
	if(next_permutation(buf, buf + len))
	    printf("%s\n", buf);
	else
	{
	    int idx = 0;
	    while(buf[idx] == '0')
                idx++;
	    
	    swap(buf[0], buf[idx]);
	    printf("%c0", buf[0]);
	    
            for(int i = 1; i < len; i++)
		    printf("%c", buf[i]);
           printf("\n");
	}
    }
    return 0;
}
