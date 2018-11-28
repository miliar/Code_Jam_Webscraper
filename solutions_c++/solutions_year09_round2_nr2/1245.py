#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <math.h>


using namespace std;

int main()
{
	int s,T,j,i,k,t,n,num,cnt,flag;
	char a[40],b[40];
	FILE * pf = fopen("B-large.in","r");
	FILE * rf = fopen("Bans.in","w");
	fscanf (pf,"%d",&T);
	for (i=0; i<T; i+=1)
	{
		fscanf (pf,"%s",a);
		//printf ("hello    %s  ",a);
		//num=n;
		//a.clear(); b.clear();
		//k=0;
		/*while (num>0)
		{
			a[k++]=(num%10+'0');
			num/=10;
		}*/
		//s=k;
		//k=0;
		s=strlen(a); 
		strcpy(b,a);
		k=strlen(b);
		cnt=0;
		while (cnt<1)
		{
			next_permutation(b,b+k);
			//printf ("%s  ",b);
			cnt++;
			if (strcmp(a,b)<0) {break;}
		}
		if (strcmp(a,b)<0) {fprintf(rf,"Case #%d: %s\n",i+1,b);} 
		else {
			//s=0;t=1;
			a[s++]='0';
			a[s]='\0';
			sort(a,a+s);
			for (j=0; j<s; j+=1)
			{
				if (a[j]!='0') {flag=j; break;}
			}
			if (flag>0) {a[0]=a[flag]; a[flag]='0';}
						//printf("Case #%d: %s\n",i+1,a);
			fprintf(rf,"Case #%d: %s\n",i+1,a);
		}
	}
	return 0;
}

