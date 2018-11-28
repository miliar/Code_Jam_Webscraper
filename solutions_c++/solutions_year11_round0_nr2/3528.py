using namespace std;
#include<cstdio>
#include<cstring>
int T, N, A, B;
char comb[28][28];    
int opposite[28][28];
char st[108];
int vf;
char S[107];
int main()  
{
	freopen("file.in","r",stdin); freopen("file.out","w",stdout);
	scanf("%d\n", &T);
	int i, j; char x, y, z;
	for(int jj = 1;jj <= T; ++jj)
	{
		for(i = 0; i <= 26; ++i)                 
			for(j = 0; j <= 26; ++j)
				opposite[i][j] = comb[i][j] = 0;
		memset(st,0, sizeof(st));
		scanf("%d ", &A);
		for(i = 1; i <= A; ++i)
		{
			scanf("%c%c%c ", &x, &y, &z );
		  //  printf("%c%c%c\n",x,y,z);
			comb[x - 64][y-64] = comb[y-64][x-64] = z;
		}
		scanf("%d ", &B);
		for(i = 1; i <= B; ++i)
		{
			scanf("%c%c ", &x, &y);
			opposite[x-64][y-64] = opposite[y-64][x-64] = 1;
		}
		memset(S,0, sizeof(S)); vf = 0;
		
		int l;
		scanf("%d %s\n",&l, S);
	 //   printf("%s\n", S);
		
		for(i = 0; i < l; ++i)
		{
			if( !vf ) st[++vf] = S[i];
			else
			{
				if( comb[ S[i] - 64 ][ st[vf] - 64 ] ) st[vf] =  comb[ S[i] - 64 ][ st[vf] - 64];
				else            
				{
					int ok = 0;
					for(j = 1; j <= vf && !ok; ++j)
						if( opposite[ S[i] - 64 ][ st[j] - 64 ] ) ok= 1;
					if(ok == 1) vf = 0;
					else st[++vf] = S[i];
				}
			}
		}
		printf("Case #%d: [", jj);
		for(i = 1; i < vf; ++i ) printf("%c, ", st[i] );
		if(vf) printf("%c",st[vf]);
		printf("]\n");
	}
	return 0;
}                                
