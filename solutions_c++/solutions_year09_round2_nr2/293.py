#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <memory.h>
#define N 22
long ntests;
char a[N];



int main(void) {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d\n",&ntests);
	for (long _=1;_<=ntests;_++) {
		memset(a,0,sizeof(a));
		long len = 0;
		for (char c=getchar();c!='\n';c=getchar()) a[len++] = c;


		long f = 0;
		for (long j=len-1;j;j--) 
			if (a[j-1]<a[j]) {
				f = 1;
				for (long i=len-1;i>j-1;i--)
					if (a[i]>a[j-1]) {
						f = i;
						break;	
					}

				char c = a[j-1];
				a[j-1] = a[f];
				a[f] = c;
				std::sort(a+j,a+len);
				break;
			}

       		printf("Case #%d: ",_);
		if (!f) {
                	std::sort(a,a+len);

                	if (a[0]=='0') {
                		for (long i=1;i<len;i++)
                			if (a[i]>'0') {
						a[0] = a[i];
						a[i] = '0';
                				break;
                			}
                	}

                	printf("%c",a[0]);
                	printf("0");
                	for (long i=1;i<len;i++) printf("%c",a[i]);
                	printf("\n");				
		} else printf("%s\n",a);


	}

	return 0;
}
