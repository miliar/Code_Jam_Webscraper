#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int l,n,d,i,j,k,s,case_Id,length,np;
	int result[5001],pos[40][2];
	char word[5001][20],index[1001];
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",word[i]);
	for(case_Id=1;case_Id<=n;case_Id++)
	{
		memset(result,0,sizeof(result));
		scanf("%s",index);
		length=strlen(index);
		k=i=0;
		while(i<length)
		{
			if(index[i]=='(')
			{
				for(j=i;;j++)
				{
					if(index[j]==')')
					{
						pos[k][0]=i+1;
						pos[k++][1]=j-1;
						break;
					}
				}
				i=j+1;
			}
			else if(index[i]!='(' && index[i]!=')')
			{
				pos[k][0]=pos[k++][1]=i;
				i++;
			}
		}
		np=k;
		for(i=0;i<np;i++)
			for(j=pos[i][0];j<=pos[i][1];j++)
				for(k=0;k<d;k++)
					if(word[k][i]==index[j])
						result[k]++;
		s=0;
		for(i=0;i<d;i++)
			if(result[i]==l)
				s++;
		printf("Case #%d: %d\n",case_Id,s);
	}
	return 0;
}