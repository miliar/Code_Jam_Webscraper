#include <stdio.h>
#include <string.h>

int L, D, n, dap;
char data[5010][20];
int check[20][30];

void input()
{
	int i;
	scanf("%d%d%d\n", &L, &D, &n);
	for(i=0; i<D; i++)
		gets(data[i]);
}

void proc()
{
	int i, j, k, cnt, flag;
	char buffer[1000] = {0,}, *ptr;

	for(i=0; i<n; i++) {
		gets(buffer);
		ptr = buffer;

		dap = 0;
		memset(check, 0, sizeof(check));

		for(cnt=0; cnt<L; cnt++) {
			if(*ptr == '(') {
				ptr++;
				while(*ptr != ')') {
					check[cnt][*ptr-'a'] = 1;
					ptr++;
				}
				ptr++;
			}
			else {
				check[cnt][*ptr-'a'] = 1;
				ptr++;
			}
		}

		for(j=0; j<D; j++) {
			flag = 0;
			for(k=0; k<L; k++) {
				if( check[k][ data[j][k] - 'a' ] == 0 ) {
					flag = 1;
					break;
				}
			}

			if(flag == 0)
				dap++;
		}

		printf("Case #%d: %d\n", i+1, dap);
	}
}

int main()
{
	input();
	proc();
	return 0;
}

