#include<stdio.h>
 void main()
	{
	 int t,tc=1,time,to,tb,tm,m,button,op,bp;
	 char bot;
	  for(scanf("%d",&t);tc<=t;tc++)
		{
		time=0;to=0;tb=0;op=1;bp=1;
		  scanf("%d",&tm);
			 for(m=1;m<=tm;m++)
				{
				  scanf(" %c %d",&bot,&button);
					 switch(bot)
					  {
						 case 'O':
									 while(op!=button)
										{
										 (op<button)?op++:op--;

										 to++;
										}
										if(to>time)
										  {
										  to++;
										  time=to;
										  }
										else
										  {
											time++;
											to=time;
										  }

									 break;
						 case 'B':
									while(bp!=button)
										{
										 (bp<button)?bp++:bp--;
										 tb++;
										}
										if(tb>time)
										  {
										  tb++;
										  time=tb;
										  }
										else
										  {
											time++;
											tb=time;
										  }
									 break;
					  }
				}
				printf("Case #%d: %d\n",tc,time);
		}
	}