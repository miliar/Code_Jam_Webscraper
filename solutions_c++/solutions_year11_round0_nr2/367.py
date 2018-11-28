#include<stdio.h>
#include<string.h>
#include<vector.h>
FILE *in,*out,*dbg;

char i[1024][3];
char j[1024][2];
char b[16384]; int c;
char v[256];
int main()
{
	in =fopen("b.in" ,"r");
	out=fopen("b.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	int k,m,n,a,s;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d",&k);
		for(a=0;a<k;a++) fscanf(in," %c%c%c",&i[a][0],&i[a][1],&i[a][2]);
		fscanf(in,"%d",&m);
		for(a=0;a<m;a++) fscanf(in," %c%c",&j[a][0],&j[a][1]);
		fscanf(in,"%d",&n);
		c=0;
		for(a=0;a<256;a++) v[a]=0;
		for(a=0;a<n;a++)
		{
			fscanf(in," %c",&b[c]);
			v[b[c]-'A']++;
			for(s=0;s<k;s++)
			{
				if( ( b[c]==i[s][0] && b[c-1]==i[s][1] ) || ( b[c]==i[s][1] && b[c-1]==i[s][0] ) )
				{
					v[b[c]-'A']--;
					v[b[c-1]-'A']--;
					c--;
					b[c]=i[s][2];
					v[b[c]-'A']++;
					break;
				}
			}
			c++;
			for(s=0;s<m;s++)
			{
				if( ( b[c-1]==j[s][0] && v[j[s][1]-'A']>0 ) || ( b[c-1]==j[s][1] && v[j[s][0]-'A']>0 ) )
				{
					while( c>0 )
					{
						c--;
						v[b[c]-'A']=0;
					}
				}
			}
		}
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,"[");
		if( c>0 ) fprintf(out,"%c",b[0]);
		for(a=1;a<c;a++) fprintf(out,", %c",b[a]);
		fprintf(out,"]\n");
	}
	return 0;
}