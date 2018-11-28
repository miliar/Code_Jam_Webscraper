#include<cstdio>

int main()
{
	int L,D,N,res;
	char P[5005][17], S[435];
	scanf("%d %d %d\n",&L,&D,&N);
	for(int i = 0;i < D;++i) scanf("%s\n",P+i);
	for(int ii = 1;ii <= N;++ii)
	{
		scanf("%s\n",S);
		res = 0;
		for(int i = 0; i < D;++i)
		{
			bool match = true;
			int l = 0;
			for(int j = 0;j < L;++j)
			{
				if(S[l] == '(')
				{
					l++;
					bool found = false;
					while(S[l] != ')')
					{
						if(S[l] == P[i][j])  found = true;
						l++;
					}
					l++;
					if(!found)
					{
						match = false;
						break;
					}
				}
				else if(S[l] == P[i][j]) l++;
				else 
				{
					match = false;
					break;
				}
			}
			if(match) res++;
		}
		printf("Case #%d: %d\n",ii,res);
	}
	return 0;
}
