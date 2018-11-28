#include<cstdio>
#include<cstring>


char comb[26][26];
bool oppos[26][26];
bool lst[26],bf;

int main()
{

	int T,C,D,i,j,k,N,lenout,kase;
	char str[5000],outs[5000];

	freopen("B-large.in","r",stdin);
	freopen("outBl1.out","w",stdout);
	scanf("%d",&T);

	kase=0;
	while(T--)
	{

		for(i=0;i<26;i++)
		{
			for(j=0;j<26;j++)
			{
				comb[i][j]=NULL;
				oppos[i][j]=false;
			
			}
			lst[i]=false;
		}

		scanf("%d",&C);
		getchar();

		for(i=0;i<C;i++)
		{
			scanf("%s",str);

			comb[str[0]-'A'][str[1]-'A']=str[2];
			comb[str[1]-'A'][str[0]-'A']=str[2];
		}
		scanf("%d",&D);
		getchar();

		for(i=0;i<D;i++)
		{
			scanf("%s",str);
			oppos[str[0]-'A'][str[1]-'A']=true;
			oppos[str[1]-'A'][str[0]-'A']=true;
		}

		scanf("%d",&N);
		getchar();

		for(i=0;i<N;i++)
		{
			scanf("%c",&str[i]);
		}
		str[N]='\0';

		

		lenout=0;
		outs[lenout++]=str[0];

	


		for(i=1;i<N;i++)
		{
	

			if(comb[outs[lenout-1]-'A'][str[i]-'A']!=NULL)
			{
				
				outs[lenout-1]=comb[outs[lenout-1]-'A'][str[i]-'A'];
			}
			else
			{
			
				bf=false;
				for(j=0;j<lenout;j++)
				{
					if(oppos[outs[j]-'A'][str[i]-'A']==true)
					{
						bf=true;
						lenout=0;
						break;
					}
				}

				if(bf==false)
				{
					outs[lenout++]=str[i];
				}
			}


		}

		outs[lenout]='\0';
		printf("Case #%d: [",++kase);

		if(lenout==1) printf("%c]\n",outs[lenout-1]);
		else
		{
		for(i=0;i<lenout;i++)
		{
			if(i==0) printf("%c,",outs[i]);
			else if(i==lenout-1) printf(" %c",outs[i]);
			else printf(" %c,",outs[i]);
		}
		printf("]\n");
		}
		//puts(outs);
		
	}

	return 0;
}