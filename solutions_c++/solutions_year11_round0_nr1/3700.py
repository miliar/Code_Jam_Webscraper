#include<stdio.h>

struct Mission 
{
	int pos;
	int index;
};

struct Mission orange[200],blue[200];
int to,tb,mo,mb;

int main()
{
	int ncase,tcase,poso,posb,ans,n,current,i,pos,canpress;
	char robot;
	scanf("%d",&ncase);
	for(tcase=1;tcase<=ncase;tcase++)
	{
		scanf("%d",&n);
		getchar();
		mo=0;
		mb=0;
		for(i=0;i<n;i++)
		{
			//scanf("%c%d",&robot,&pos);
			scanf("%c",&robot);
			getchar();
			scanf("%d",&pos);
			getchar();
			if(robot=='B')
			{
				blue[mb].pos=pos;
				blue[mb].index=i;
				mb++;
			}
			else
			{
				orange[mo].pos=pos;
				orange[mo].index=i;
				mo++;
			}
		}
		poso=1;
		posb=1;
		ans=0;
		tb=0;
		to=0;
		current=0;
		while(current<n)
		{
			canpress=1;
			//B
			if(tb<mb)
			{
				if(posb==blue[tb].pos)
				{
					if(canpress==1&&blue[tb].index==current)
					{
						tb++;
						current++;
						canpress=0;
					}
				}
				else
				{
					if(posb<blue[tb].pos)
					{
						posb++;
					}
					else
					{
						posb--;
					}
				}
			}

			//O
			if(to<mo)
			{
				if(poso==orange[to].pos)
				{
					if(canpress==1&&orange[to].index==current)
					{
						to++;
						current++;
						canpress=0;
					}
				}
				else
				{
					if(poso<orange[to].pos)
					{
						poso++;
					}
					else
					{
						poso--;
					}
				}
			}

			ans++;
		}
		printf("Case #%d: %d\n",tcase,ans);
	}
	return 0;
}
