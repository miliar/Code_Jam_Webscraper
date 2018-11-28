#include<cstdio>
#define MN 104

int test,ntest,n,i,j,b,opp;
int t[MN][MN],win[MN],mat[MN];
double wp[MN],owp[MN],oowp[MN],swp;
char s[MN];

int main()
{
	scanf("%d",&ntest);
	for(test=1; test<=ntest; ++test)
	{
		scanf("%d",&n);
		for(i=0; i<n; ++i) {
			win[i]=mat[i]=0;
			wp[i]=owp[i]=oowp[i]=0.0;
			for(j=0; j<n; ++j) t[i][j]=t[j][i]=-1;
		}
		for(i=0; i<n; ++i)
		{
			scanf("%s",s);
			for(j=0; j<n; ++j)
				if(s[j]!='.') {
					t[i][j]=s[j]-'0';
					t[j][i]=t[i][j]^1;
					++mat[i];
					if(t[i][j]) ++win[i];
				}
		}
		for(i=0; i<n; ++i)
		{
			if(mat[i]) wp[i]=double(win[i])/double(mat[i]);
			for(j=opp=0, swp=0.0; j<n; ++j) 
				if(t[i][j]>=0) {
					swp+=double(win[j]-t[j][i])/double(mat[j]-1);
					++opp;
				}
			if(opp) owp[i]=swp/double(opp);
		}
		for(i=0; i<n; ++i)
		{
			for(j=opp=0, swp=0.0; j<n; ++j)
				if(t[i][j]>=0) { 
					swp+=owp[j]; 
					++opp;
				}
			if(opp) oowp[i]=swp/double(opp);
		}
		printf("Case #%d:\n",test);
		for(i=0; i<n; ++i) {
			printf("%.8lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
}

