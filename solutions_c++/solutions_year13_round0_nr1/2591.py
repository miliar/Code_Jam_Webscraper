#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
#define REP(i,n)for(int i=0;i<(n);i++)

int nextint()
{
	int t;
	scanf("%d",&t);
	return t;
}

char fld[5][5];

bool isok(int i,int j)
{
	return 0<=i&&i<4&&0<=j&&j<4;
}

bool ismine(char a, char val)
{
	return val!='.'&&a==val||a=='T';
}

bool isempty(int i, int j)
{
	return fld[i][j]=='.';
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		string result="Draw";
		REP(i,4) scanf("%s",fld[i]);
		for(int dx=-1;dx<=1;dx++) for(int dy=-1;dy<=1;dy++)
			if(dx!=0||dy!=0)
			{
				REP(i,4) REP(j,4)
				{
					bool ok=true;
					REP(k,4)
						if(!(isok(i+dx*k,j+dy*k)&&ismine(fld[i+dx*k][j+dy*k],fld[i][j])))
							ok=false;
					if(ok)
					{
						result=string(1,fld[i][j])+" won";
					}
				}
			}
		if(result=="Draw")
		{
			REP(i,4) REP(j,4)
				if(isempty(i,j))
					result="Game has not completed";
		}
		printf("Case #%d: %s\n",test,result.c_str());
	}
}
