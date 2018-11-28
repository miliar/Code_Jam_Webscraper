#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char str[510];
int sol[510][3];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("cjlarge03.out","w",stdout);

	int i, j, l, now, cas, sum;
	scanf("%d\n",&cas);

	for(now=1; now<=cas; now++) {
		cin.getline(str, 501);
		l = strlen(str);
		sum = 0;

		for(i=0; i<l; i++) {
			sol[i][0] = sol[i][1] = sol[i][2] = 0;

			if(str[i] == 'w') {
				sol[i][0] = 1;
			}
		}

		for(i=0; i<l; i++) {
			if(str[i] == 'w') {
				for(j=i+1; j<l; j++) {
					if(str[j] == 'e') sol[j][0] = (sol[j][0]+sol[i][0])%10000;
				}
			}
			else if(str[i] == 'e') {
				for(j=i+1; j<l; j++) 
					if(str[j] == 'l') sol[j][0] = (sol[j][0]+sol[i][0])%10000;
					else if(str[j] == ' ') {
						sol[j][0] = (sol[j][0]+sol[i][1])%10000;
						sol[j][2] = (sol[j][2]+sol[i][2])%10000;
					}
			}
			else if(str[i] == 'l') {
				for(j=i+1; j<l; j++) {
					if(str[j] == 'c') sol[j][0] = (sol[j][0]+sol[i][0])%10000;
				}
			}
			else if(str[i] == 'c') {
				for(j=i+1; j<l; j++) {
					if(str[j] == 'o') {
						sol[j][0] = (sol[j][0]+sol[i][0])%10000;
						sol[j][2] = (sol[j][2]+sol[i][1])%10000;
					}
				}
			}
			else if(str[i] == 'o') {
				for(j=i+1; j<l; j++) 
					if(str[j] == 'm') sol[j][0] = (sol[j][0]+sol[i][0])%10000;
					else if(str[j] == ' ') sol[j][1] = (sol[j][1]+sol[i][1])%10000;
					else if(str[j] == 'd') sol[j][0] = (sol[j][0]+sol[i][2])%10000;
			}
			else if(str[i] == 'm') {
				for(j=i+1; j<l; j++) 
					if(str[j] == 'e') sol[j][1] = (sol[j][1]+sol[i][0])%10000;
				sum = (sum+sol[i][1])%10000;
				sol[i][1] = 0;
			}
			else if(str[i] == ' ') {
				for(j=i+1; j<l; j++) 
					if(str[j] == 't') sol[j][0] = (sol[j][0]+sol[i][0])%10000;
					else if(str[j] == 'c') sol[j][1] = (sol[j][1]+sol[i][1])%10000;
					else if(str[j] == 'j') sol[j][0] = (sol[j][0]+sol[i][2])%10000;
			}
			else if(str[i] == 't') {
				for(j=i+1; j<l; j++) {
					if(str[j] == 'o') sol[j][1] = (sol[j][1]+sol[i][0])%10000;
				}
			}
			else if(str[i] == 'd') {
				for(j=i+1; j<l; j++) {
					if(str[j] == 'e') sol[j][2] = (sol[j][2]+sol[i][0])%10000;
				}
			}
			else if(str[i] == 'j') {
				for(j=i+1; j<l; j++) {
					if(str[j] == 'a') sol[j][0] = (sol[j][0]+sol[i][0])%10000;
				}
			}
			else if(str[i] == 'a') {
				for(j=i+1; j<l; j++) {
					if(str[j] == 'm') sol[j][1] = (sol[j][1]+sol[i][0])%10000;
				}
			}

		}

		printf("Case #%d: %04d\n",now,sum);
	}


	return 0;
}