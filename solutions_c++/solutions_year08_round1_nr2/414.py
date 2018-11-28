#include<iostream>
using namespace std;
#include<stdlib.h>
#include<bitset>
struct node
{
	int index;
	int need;
}map[101][101];
int len[101];
int main()
{
    int i,t,j,w = 0,n,m,k,a,b,r;
	FILE *fp,*fout;
	fp = fopen("t2.in","r");
	fout = fopen("out2.txt","w");
//	ffscanf(fp,fp,"%d",&t);
	fscanf(fp,"%d",&t);
	bitset<10>s;
	while(t--)
	{
		w ++;
		memset(map,-1,sizeof(map));
	//	ffscanf(fp,fp,"%d",&n);
		fscanf(fp,"%d",&n);
	    fscanf(fp,"%d",&m);
	   
		for(i = 0; i< m; i++)
		{
			fscanf(fp,"%d",&len[i]);
			for(j = 0; j < len[i]; j++)
			{
                fscanf(fp,"%d %d",&a,&b);
				map[i][j].index = a -1 ;
				map[i][j].need = b;
			}
		}
		int max = (1<<n) -1,min = 11;
		for(i = 0; i <= max; i++)
		{
			s = i;
			for(j = 0; j < m; j++)
			{
                for(k = 0; k < len[j]; k++)
				{
					if(s[map[j][k].index] == map[j][k].need)
						break;
				}
				if(k==len[j]) 
					break;
			}
			if(j == m)
			{
				 int count = 0;
                 for(j = 0; j < n; j++)
				 {
					 if(s[j]) count ++;
				 }
				 if(count < min)
				 {
					min = count;
					r = s.to_ulong();
				 }
			}
		}
		fprintf(fout,"Case #%d: ",w);
		if(min == 11) fprintf(fout,"IMPOSSIBLE\n");
		else 
		{
			s = r;
			for(i = 0; i < n; i++)
			{
				if(i!=0) fprintf(fout," ");
				if(s[i]) fprintf(fout,"1");
				else fprintf(fout,"0");
			}
		}
		fprintf(fout,"\n");
		
		
	}

}