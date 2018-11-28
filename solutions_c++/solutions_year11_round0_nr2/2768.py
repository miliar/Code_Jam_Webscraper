#include<stdio.h>

 int n;
 void del(int pos,char regint[])
	{
	 int t=pos;
	  while(t<n)
		{
		 regint[t]=regint[t+1];
		 t++;
		}
		n--;
	}

 void replace(int pos1,int pos2,char replace,char regint[])
	{
		 while(pos1!=pos2)
		  {
			del(pos2,regint);
			pos2--;
		  }
		 regint[pos1]=replace;
	}



 void main()
	{
	 int t,tc=1,c,d,cc;
	 char base[37][3],opp[29][2],inp[101];

	  for(scanf("%d",&t);tc<=t;tc++)
		{
		  scanf("%d",&c);

			 for(cc=1;cc<=c;cc++)
				{
				  scanf(" %c%c%c",&base[cc][0],&base[cc][1],&base[cc][2]);
				}
			scanf(" %d",&d);
			 for(cc=1;cc<=d;cc++)
				{
				  scanf(" %c%c",&opp[cc][0],&opp[cc][1]);
				}
			scanf(" %d ",&n);
			 for(cc=1;cc<=n;cc++)
				{
				  scanf("%c",&inp[cc]);
				}



			for(int i=2;i<=n;i++)
				  {
				for(cc=1;cc<=c;cc++)
					{
					 if(((base[cc][0]==inp[i])&&(base[cc][1]==inp[i-1]))||((base[cc][1]==inp[i])&&(base[cc][0]==inp[i-1])))
					 {

						replace(i-1,i,base[cc][2],inp);
						i--;
					 }
				  }


			for(cc=1;cc<=d;cc++)
			{

				  if(opp[cc][0]==inp[i])
					 {
						  int temp=1;
						  while(temp<i&&(inp[temp]!=opp[cc][1]))
							temp++;

						  if(temp<i)
							{
							 temp=1;
							  while(temp<=i)
								{
								 del(temp,inp);
								 i--;
								}

							}
					 }
					 else if(opp[cc][1]==inp[i])
					 {
						  int temp=1;
						  while(temp<i&&(inp[temp]!=opp[cc][0]))
							temp++;

						  if(temp<i)
							{
                      temp=1;
							  while(temp<=i)
								{
								 del(temp,inp);

								 i--;
								}
							}
					 }


				 }



				}

			  cc=1;
			  printf("Case #%d: [",tc);
			  if(n>0)
				 {
				 printf("%c",inp[cc]);
				 cc++;
				  }
			 for(;cc<=n;cc++)
				{
				  printf(", %c",inp[cc]);
				}
				printf("]\n");

		}
	}
