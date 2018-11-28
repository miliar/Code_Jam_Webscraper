

#include "stdio.h"
#include "string.h"
#define MAX 40
int main()
{
	char m[MAX][MAX];
	char temp[MAX];
	bool is=true,find=true;;
	int i,j,k,l,ts,n,c=0,x,y;
	FILE *in;	in=fopen("d:\\A-large.in.txt","rb");
	FILE *out;
	out=fopen("d:\\C-large.out.txt","wb");
	fscanf(in,"%d",&ts);
	fgets(m[0],MAX,in);
	for(k=1;k<=ts;k++)
	{
		fscanf(in,"%d",&n);
		fgets(temp,MAX,in);
		for(i=0;i<n;i++)
		{
			
			fgets(m[i],MAX,in);
	    }
		c=0;
        for(i=0;i<n;i++)
		{
            is=true;
			for(j=i+1;j<n;j++)
			{
                 if(m[i][j]=='1')
				 {
					 is=false;
					 break;
				 }
			}
			if(is==true)
			{
				continue;
			}
			else
			{
				
                for(j=i+1;j<n;j++)//row
				{
					find=true;
					for(l=i+1;l<n;l++)
					{
                    if(m[j][l]=='1')
					{
						find=false;
						break;
					}
					}
					if(find==true)
                       break;
				}
                if(find==true)
				{
					for(x=j-1;x>=i;x--)
					{
						for(y=0;y<n;y++)
						{
							m[x+1][y]=m[x][y];
						}
					}
					c+=(j-i);
				}
			}
		}
		fprintf(out,"Case #%d: %d\n",k,c);
	}
}
