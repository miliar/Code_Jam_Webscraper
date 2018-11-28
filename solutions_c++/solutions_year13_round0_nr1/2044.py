/* codejam first problem
Programmer:sandesh kumar singh */

#include<stdio.h>
#include<string.h>

int main()
{
     int t,x,o,cnt,i,cases=0;;
     char str[6][6];
     freopen("c.in","r",stdin);
     freopen("cc.out","w",stdout);
     scanf("%d",&t);
     while(t--)
     {
	       cases++;
	       printf("Case #%d: ",cases);
	       x=0;o=0;
	       gets(str[0]);
	       for(i=0;i<4;i++)
	       gets(str[i]);
	       for( i=0;i<4;i++)
	       {
		       if((str[i][0]=='X'||str[i][0]=='T')&&(str[i][1]=='X'||str[i][1]=='T')&&
		       (str[i][2]=='X'||str[i][2]=='T')&&(str[i][3]=='X'||str[i][3]=='T'))
		       {x=1;break;}
		       if((str[i][0]=='O'||str[i][0]=='T')&&(str[i][1]=='O'||str[i][1]=='T')&&
		       (str[i][2]=='O'||str[i][2]=='T')&&(str[i][3]=='O'||str[i][3]=='T'))
		       {o=1;break;}
	       }

	       for( i=0;i<4;i++)
	       {
		       if((str[0][i]=='X'||str[0][i]=='T')&&(str[1][i]=='X'||str[1][i]=='T')&&
		       (str[2][i]=='X'||str[2][i]=='T')&&(str[3][i]=='X'||str[3][i]=='T'))
		       {x=1;break;}
		       if((str[0][i]=='O'||str[0][i]=='T')&&(str[1][i]=='O'||str[1][i]=='T')&&
		       (str[2][i]=='O'||str[2][i]=='T')&&(str[3][i]=='O'||str[3][i]=='T'))
		       {o=1;break;}
	       }



			if((str[0][0]=='X'||str[0][0]=='T')&&(str[1][1]=='X'||str[1][1]=='T')&&
		       (str[2][2]=='X'||str[2][2]=='T')&&(str[3][3]=='X'||str[3][3]=='T'))
		       {x=1;}
		       if((str[0][0]=='O'||str[0][0]=='T')&&(str[1][1]=='O'||str[1][1]=='T')&&
		       (str[2][2]=='O'||str[2][2]=='T')&&(str[3][3]=='O'||str[3][3]=='T'))
		       {o=1;}

		       if((str[0][3]=='X'||str[0][3]=='T')&&(str[1][2]=='X'||str[1][2]=='T')&&
		       (str[2][1]=='X'||str[2][1]=='T')&&(str[3][0]=='X'||str[3][0]=='T'))
		       {x=1;}
		       if((str[0][3]=='O'||str[0][3]=='T')&&(str[1][2]=='O'||str[1][2]=='T')&&
		       (str[2][1]=='O'||str[2][1]=='T')&&(str[3][0]=='O'||str[3][0]=='T'))
		       {o=1;}

	       if(x==1)
	       {printf("X won\n");continue;}
	       if(o==1)
	       {printf("O won\n");continue;}
	       cnt=0;


	       for( i=0;i<4;i++)
	       {
		       for(int j=0;j<4;j++)
		       if(str[i][j]=='.')
		       cnt++;
	       }
	       if(cnt)
	       printf("Game has not completed\n");
	       else
	       printf("Draw\n");


     }
     scanf("%d",&t);
     return 0;
}
