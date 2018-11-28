#include<stdio.h>
#include<string.h>

char combine[200][200];
bool opposed[200][200];
int hasLetter[200];
char bases[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};


int main()
{
	freopen("B.in","rt",stdin);
	freopen("B.out","wt",stdout);
	int T,kase,C,D,N;
	scanf("%d",&T);
	for (kase=1; kase<=T; kase++)
	{
		for(int a=0;a<200;a++)
		{
			for(int b=0;b<200;b++)
			{
				combine[a][b]=0;
				opposed[a][b]=false;
			}
		}
		char ccc[5],word[103],ans[103];
		scanf("%d", &C);
		for(int i=0;i<C;i++)
		{
			scanf("%s",ccc);			
			combine[ccc[0]][ccc[1]] = ccc[2];
            combine[ccc[1]][ccc[0]] = ccc[2];
		}

		scanf("%d", &D);
		for(i=0;i<D;i++)
		{
			scanf("%s", ccc);
            opposed[ccc[0]][ccc[1]] = true;
            opposed[ccc[1]][ccc[0]] = true;
		}

		scanf("%d",&N);
		scanf("%s",word);
		

		int ap=-1;

		for(i=0;i<8;i++) 
		{ 
			hasLetter[bases[i]] = 0; 
		}
		
		for(i=0;i<N;i++)
		{
			char &nl = word[i];
            if(ap < 0) {
                ans[ap=0] = nl;
                hasLetter[nl]++;
                continue;
            }
            if(combine[ans[ap]][nl]) {
                hasLetter[ans[ap]]--;
                ans[ap] = combine[ans[ap]][nl];
                continue;
            }
            int j;
            for(j=0;j<8;j++) {
                if(opposed[nl][bases[j]] && hasLetter[bases[j]]) {break;}
            }
            if(j<8) {
                ap=-1;
                for(int k=0;k<8;k++) 
				{
					hasLetter[bases[k]] = 0; 
				}
                continue;
            }
            hasLetter[nl]++;
            ans[++ap] = nl;
		}
		

		printf("Case #%d: [",kase);
		for(i=0;i<=ap;i++)
		{
			if(!i) printf("%c",ans[i]);
			else printf(", %c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}