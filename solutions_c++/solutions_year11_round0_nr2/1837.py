#include<iostream>
#include<stdio.h>

using namespace std;
int pa[26][26];
int rem[26][26];
char input[101];
char output[101];
int set[26];
void calculate(int ,int);

void init()
{
    for(int i=0;i<26;i++)
    {
      for(int j=0;j<26;j++)
        pa[i][j]=rem[i][j]=0;
      set[i]=0;
    }
    for(int i=0;i<101;i++)
        input[i]=output[i]=0;
}

int main()
{
	int T,C,D,N;
	char c1,c2,c3,c;
    int j=0;
	scanf("%d",&T);
	while(T--)
	{
        j++;
		scanf("%d",&C);
		for(int i=0;i<C;i++)
		{
			scanf("%c",&c);
			scanf("%c",&c1);
			scanf("%c",&c2);
			scanf("%c",&c3);
			pa[c1-'A'][c2-'A']=c3-'A';
			pa[c2-'A'][c1-'A']=c3-'A';
           // printf("C %c %c %d\n",c1,c2,pa[c1-'A'][c2-'A']);
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++)
		{
			scanf("%c",&c);
			scanf("%c",&c1);
			scanf("%c",&c2);
			rem[c1-'A'][c2-'A']=1;
            rem[c2-'A'][c1-'A']=1;
          //  printf("D %c %c %d\n",c1,c2,rem[c1-'A'][c2-'A']);
		}
		scanf("%d",&N);
		scanf("%c",&c);
		for(int i=1;i<=N;i++)
		{
			scanf("%c",&input[i]);
		}
		calculate(j,N);
        init();
	}
}

void calculate(int count,int N)
{
	int o=1;
	char c = input[1];
	char c1,c2;
	output[1]=c;
	output[0]='a';
	set[c-'A']=1;
	bool cp = false;
	for(int i=2;i<=N;i++)
	{
		c1=input[i];
		cp=false;
      //  printf("%c %c %d\n",c1,c,pa[c1-'A'][c-'A']);
		while(pa[c1-'A'][c-'A']!=0)
		{
			c2=pa[c1-'A'][c-'A']+'A';
			c1=c2;
			o--;
            set[c-'A']--;
           // printf("yes");
			c=output[o];	
		}
        
		for(int j=0;j<26;j++)
		if(rem[c1-'A'][j]&&set[j]!=0&&(int)(c1-'A')!=j)
		{
           // printf("y\n");
            cp=true;
			if(i<N){
			o=1;
			output[1]=input[i+1];
			c=input[i+1];i++;
              break;
			}
			else
			{
				o=0;
			}
			
		}
		if(!cp)
        {
		 output[++o]=c1;
         set[c1-'A']++;
            c=c1;
        }
        else
        {
            for(int i=0;i<26;i++)
                set[i]=0;
            set[c-'A']=1;
        }		
	}
    printf("Case #%d: [",count);
	for(int i=1;i<o;i++)
	printf("%c, ",output[i]);
       if(o!=0)
    printf("%c",output[o]);
   	printf("]\n");
   
}
