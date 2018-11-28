#include <cstdio>
#include <cstring>
#include <algorithm>
#include <numeric>
using namespace std;

char index[25]="@welcome to code jam";

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int nCase,i,j,length,case_Id;
	int result[25][505];
	char input[505];
	scanf("%d",&nCase);
	gets(input);
	for(case_Id=1;case_Id<=nCase;case_Id++)
	{
		memset(result,0,sizeof(result));
		gets(input+1);
		length=strlen(input+1);
		result[0][0]=1;
		for(i=1;i<20;i++)
			for(j=i;j<=length;j++)
				if(index[i]==input[j])
					result[i][j]=accumulate(result[i-1],result[i-1]+j,0)%10000;
		printf("Case #%d: %04d\n",case_Id,accumulate(result[19],result[19]+length+1,0)%10000);
	}
	return 0;
}