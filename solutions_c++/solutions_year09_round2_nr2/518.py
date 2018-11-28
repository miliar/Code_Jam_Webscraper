#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int main()
{
	char str[1000];
	int n,x,y,z,l,max,min;
	int loc[10];
	FILE *fin=fopen("B-small.in","r"),*fout=fopen("B-small.out","w");
	fscanf(fin,"%d",&n);
	for(x=1;x<=n;++x)
	{
		str[0]='0';
		fscanf(fin,"%s",str+1);
		l=strlen(str);
		max=min=l-1;
		for(y=0;y<10;++y)
			loc[y]=-1;
		loc[str[l-1]-'0']=l-1;
		for(y=l-2;str[y]>=str[max];--y)
		{
			loc[str[y]-'0']=y;
			max=y;
			if(str[y]<str[min])
				min=y;
		}
		for(z=str[y]-'0'+1;loc[z]==-1;++z);
		z=loc[z];
		swap(str[y],str[z]);
		sort(str+y+1,str+l);
		if(str[0]=='0')
			fprintf(fout,"Case #%d: %s\n",x,str+1);
		else
			fprintf(fout,"Case #%d: %s\n",x,str);
	}
	return 0;
}
