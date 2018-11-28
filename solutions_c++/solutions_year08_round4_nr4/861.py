#include<stdio.h>
#include<string.h>

int a[17];
int b[17];
long ans;
int k;
long temp;
long l;
char str[50001];
char ch1,ch2;

void find(int p)
{
	int i,j,q;
	for (i = 0 ; i < k ; i++) {
		if (b[i] == 0) {
			
			a[p] = i;
			if (p > 0) {
				b[i] = 1;
				find(p-1);
				b[i] = 0;
			} else {
				temp = 0;
				
				for ( j = 0 ; j < l/k ; j++) {
					for (q = 0 ; q < k ; q++) {
						ch2 = str[j*k + a[q]];
						if (ch1!= ch2) {
							temp ++;
							if (temp >= ans) goto c1;
							ch1 = ch2;
						}
					}
				}
				ans = temp;
c1:				ch1 = '0';
			}
		}
	}
}

int main()
{
	long i,CaseNum,t;

	scanf("%d",&t);
	CaseNum = 1;
	FILE *fp = fopen("d1.txt","w");
	while (CaseNum <= t) {
		scanf("%d",&k);
		scanf("%s",str);
		//scanf("%s",str);

		l = strlen(str);

		for (i = 0 ; i < k ; i++) b[i] = 0;
		ans = l;
		ch1 = '0';
		find(k-1);

		fprintf(fp,"Case #%d: %d\n",CaseNum,ans);

		CaseNum++;
	}
	fclose(fp);
	return 0;
}