#include <stdio.h>
#include <stdlib.h>

char s[102400];
char dict[5000][20];

int main() {

int i,j,counter;
int l,d,n;
gets(s);
sscanf(s, "%d %d %d", &l, &d, &n);	

for (i=0; i<d; i++)
	gets(dict[i]);
for (int c=0; c<n; c++)
{
	gets(s);
	counter=0;
	for (i=0; i<d; i++)
{
	int k=0;
	j=0;
	bool found;
	while(s[j]!=0 && k<l)
	{
		if (s[j]==')')
			printf ("ERROR\n");
		else if (s[j]!='(')
			{if (s[j]!=dict[i][k]) break;}
		else  
		{
			found = false;
			for (j++ ;s[j]!=0 && s[j]!=')'; j++) 
			{
				if (s[j] == dict[i][k]){  
					found = true;
				}
			}
			if (!found) break;
		}
		k++;
		j++;
	}
	if (k==l) counter++;		
	//printf ("Case %d: %d\n", c+1, counter);
}
	printf ("Case #%d: %d\n", c+1, counter);
}
return 0;
}
