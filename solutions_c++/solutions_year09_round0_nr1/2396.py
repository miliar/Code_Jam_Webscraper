#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char **argv)
{

	int L,D, N, cases, match, found;
	char dic[5000][16];

	int i, j, s;
	char str[85000]; //25*10

    freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	scanf("%d %d %d",&L,&D,&cases);

	for(i=0; i<D; i++)
		scanf("%s",&dic[i]);

	for(N=1; N<=cases; N++)
	{
		i=0; j=0; s=0; match=0;
		scanf("%s",str);
		
    	while(i<D)
    	{
	    	while(j<L && i<D)
	    	{
				if(str[s]=='(')	
				{	
					s++; found=0;
					
					while(str[s]!=')')
					{
			    		if(dic[i][j]==str[s])	{ j++; s++; found=1;break; }		// token matched 
			    		else s++ ;
				    }
				    if (found==0)	{ i++; s=0; j=0; break; }
				    else while(str[s++]!=')') ;		// jump to next token
			    }
			    else if(dic[i][j]==str[s])	{ j++; s++; }
			    else { i++; j=0; s=0; }
			}
			if(j==L) { i++; j=0; s=0; match++; }			// Word Match 
    	}
    	
		printf("Case #%d: %d\n",N,match);
	}
	return 0;
}

