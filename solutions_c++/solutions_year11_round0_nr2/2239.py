#include<iostream>
#include<cstdio>
#include<cstring>
#define MAXL 40
#define MAXN 110
using namespace std;

int main()
{
	int t = 0;
	int i,j,k,T;
	int C,D,N;
	int cnt;
	bool flag1,flag2,find;
	char s1[MAXL][5];
	char s2[MAXL][5];
	char s3[MAXN];
	char ans[MAXN];
	FILE *fin = fopen("B-large.in","r");
	FILE *fout = fopen("B-large.txt","w");
	fscanf(fin,"%d",&T);
	while(T--)
	{
		memset(s1,0,sizeof(s1));
		memset(s2,0,sizeof(s2));
		memset(s3,0,sizeof(s3));
		memset(ans,0,sizeof(ans));
		cnt = 0;
		fscanf(fin,"%d",&C);
		for(i=0;i<C;i++)
			fscanf(fin,"%s",s1[i]);
		fscanf(fin,"%d",&D);
		for(i=0;i<D;i++)	
			fscanf(fin,"%s",s2[i]);
		fscanf(fin,"%d",&N);
		fscanf(fin,"%s",s3);
		for(i=0;i<N;i++)
		{
			flag1 = false;
			flag2 = false;
			find = false;
			if(cnt != 0)
			{
				for(j=0;j<C;j++)
				{
					if( (ans[cnt-1] == s1[j][0] && s3[i] == s1[j][1]) || (ans[cnt-1]) == s1[j][1] && s3[i] == s1[j][0]  )
					{
						cnt--;
						ans[cnt++] = s1[j][2];
						flag1 = true;
						break;
					}
				}
				if(flag1)
				{
					for(j=0;j<D;j++)
					{
						if( ans[cnt-1] == s2[j][0]) 
						{
							for(k=0;k<cnt-1;k++)
							{
								if(ans[k] == s2[j][1])
								{
									find = true;
									cnt = 0;
									break;
								}
							}	
						}
						else if( ans[cnt-1] == s2[j][1] )
						{
							for(k=0;k<cnt-1;k++)
							{
								if(ans[k] == s2[j][0])
								{
									find = true;
									cnt = 0;
									break;
								}
							}	
						}
						if(find)
						{
							flag2 = true;
							break;
						}
					}
				}
				else
				{
					for(j=0;j<D;j++)
					{
						if( s3[i] == s2[j][0]) 
						{
							for(k=0;k<cnt;k++)
							{
								if(ans[k] == s2[j][1])
								{
									find = true;
									cnt = 0;
									break;
								}
							}	
						}
						else if( s3[i] == s2[j][1] )
						{
							for(k=0;k<cnt;k++)
							{
								if(ans[k] == s2[j][0])
								{
									find = true;
									cnt = 0;
									break;
								}
							}	
						}
						if(find)
						{
							flag2 = true;
							break;
						}
					}
				}
				if(!flag1 && !flag2)
					ans[cnt++] = s3[i];
			}
			else
				ans[cnt++] = s3[i];
		}
		fprintf(fout,"Case #%d: [",++t);
		for(i=0;i<cnt;i++)
		{
			if(i == 0)
				fprintf(fout,"%c",ans[i]);
			else
				fprintf(fout,", %c",ans[i]);
		}
		fprintf(fout,"]\n");
	}
	return 0;
}
