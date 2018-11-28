#include<iostream>
#include<algorithm>

using namespace std;

struct node
{
	int get;
	int num;
	int x[105];
	int pos;

}save[305]; 

struct node1
{
	int p;
	char rot;
}a[105];

int main()
{	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas;
	int k =1;
	int i,j;

	scanf("%d",&cas);

	int n;

	while(cas --)
	{
		scanf("%d",&n);
		
		for(i=0;i<n;i++)
		{
			save['O'].num = 0;
			save['B'].num = 0;
			save['O'].get = save['B'].get = 0;
		}
		for(i=0;i<n;i++)
		{
			getchar();
			scanf("%c%d",&a[i].rot,&a[i].p);

			int len = save[a[i].rot ].num;

			save[a[i].rot].x[len] = a[i].p;
			
			save[a[i].rot].num ++;

		}


		int ans = 0;

		int target = 1;

		save['O'].pos = 1;
		save['B'].pos = 1;
		
		for(i=0;i<n;i++)
		{
			char t = a[i].rot;

			while(save[t].pos <= a[i].p || save[t].pos >=a[i].p)
			{
				ans ++;
				
				
				if(t == 'O')
				{
					target = save['B'].get ;

					if(save['B'].pos < save['B'].x[target])

						save['B'].pos ++;

					if(save['B'].pos > save['B'].x[target])

						save['B'].pos --;
				}
				else
				{
					target = save['O'].get ;

					if(save['O'].pos < save['O'].x[target])
					
						save['O'].pos ++ ;

					if(save['O'].pos > save['O'].x[target])
					
						save['O'].pos -- ;
				}	
			
				if(save[t].pos == a[i].p)
					break;

				if(save[t].pos < a[i].p)
				
					save[t].pos ++;

				if(save[t].pos > a[i].p)

					save[t].pos --;
				
			}
			save[t].get ++;
		}

		printf("Case #%d: %d\n",k++,ans);
			

	}

	return 0;
}

/*
3
2 B 2 B 1
*/