#include <stdio.h>
#include <string.h>

#include <vector>
#include <string>
using namespace std;

char a[17][28],str[1000];
char d[5005][28];
int L,D,N;	
string s;

int main ()
{
	FILE *in = fopen ("a.in","r");
	FILE *out = fopen ("a.out","w");
	int i,j,p,q,ret = 0;
	
	fscanf (in,"%d %d %d",&L,&D,&N);
	for (i=0;i<D;i++)
		fscanf (in,"%s",d[i]);
	
	bool f = 0;
	for (i=0;i<N;i++)
	{
		int c = 0;
		s = "";
		fscanf (in,"%s",str);
		for (j=0;j<strlen(str);j++)
		{
			if (str[j] == '(') f = 1;
			if (str[j] != '(' && str[j] != ')')
			{
				if (f == 0) a[c][0] = str[j] , a[c][1] = '\0' , c ++;
				else  s += str[j];	
			}
			if (str[j] == ')')
			{
		 		sprintf (a[c],"%s",s.c_str());
		 		s = "";
				c ++;
				f = 0;
			}
		}
		
		for (j=0;j<D;j++)
		{
			bool fl = 0;
			for (p=0;p<L;p++)
			{
				for (q=0;q<strlen(a[p]);q++)
				{
					if (d[j][p] == a[p][q])
					{
						fl = 1;
						break;
					}
				}
				
				if (fl == 0) 
					break;
				fl = 0;
			}	
			
			if (p == L) ret ++;
		}
		
		fprintf (out,"Case #%d: %d\n",i+1,ret);
		ret = 0;
	}
}
