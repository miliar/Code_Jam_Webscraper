#include<stdio.h>
#include<conio.h>

void main()
{
FILE *f,*f1;
int n,it,i,j,k,l,m1,c,d,n1;
char e[100],r[100],m[36][3],o[28][2],ch;
f = fopen("input.txt","r");

f1 = fopen("output.txt","w");

fscanf(f,"%d",&n);
for(i=0;i<n;i++)
{
fscanf(f,"%d ",&c);
for(j=0;j<c;j++)
{
m[j][0] = fgetc(f);
m[j][1] = fgetc(f);
m[j][2] = fgetc(f);
ch = fgetc(f);
fflush(f);
}
fscanf(f,"%d ",&d);
for(j=0;j<d;j++)
{
o[j][0] = fgetc(f);
o[j][1] = fgetc(f);

ch = fgetc(f);
fflush(f);
}

fscanf(f,"%d ",&n1);
for(j=0;j<n1;j++)
{
e[j] = fgetc(f);

fflush(f);
}

l=1;
r[0] = e[0];


for(j=1;j<n1;j++)
{
	r[l] = e[j];

	for( k=0;k<c;k++)
	{
		if((r[l-1]==m[k][0] && r[l]==m[k][1])||(r[l-1]==m[k][1] && r[l]==m[k][0]))
		{
		r[l -1] = m[k][2];
		l--;
		break;
		}
	}
	l++;
	for(k=0;k<d;k++)
	{
		if(r[l-1]==o[k][1])
		{
			for(m1=0;m1<l-1;m1++)
			{
				if(r[m1] == o[k][0])
				{
				l=0;
				break;
				}
			}
		}
		else if(r[l-1]==o[k][0])
		{
			for(m1=0;m1<l-1;m1++)
			{
				if(r[m1] == o[k][1])
				{
				l=0;
				break;
				}
			}

		}
	}
}


fprintf(f1,"Case #%d: [",i+1);
for(j=0;j<l;j++)
{
if(j==0)
fprintf(f1,"%c",r[j]);
else
fprintf(f1,", %c",r[j]);
}
fprintf(f1,"]\n");
}

}






