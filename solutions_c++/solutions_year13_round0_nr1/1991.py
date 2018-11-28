#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
//#include<conio.h>

#define MOD 1000000007

using namespace std;

char str[6][6];

int check()
{
	int i,flag=0;
	int countx,counto,countt,blank;

	countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[i][i]=='.')
		{   flag=1;
			blank++;
		}

		else if(str[i][i]=='X')
		countx++;

		else if(str[i][i]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {
            if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }
	// main diagnol end

	countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[i][3-i]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[i][3-i]=='X')
		countx++;

		else if(str[i][3-i]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {

			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }
	// reverse main diagnol end

    countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[0][i]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[0][i]=='X')
		countx++;

		else if(str[0][i]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {
			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // horizontal 1

         countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[1][i]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[1][i]=='X')
		countx++;

		else if(str[1][i]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {

			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // horizontal 2

    countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[2][i]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[2][i]=='X')
		countx++;

		else if(str[2][i]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {
			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // horizontal 3

         countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[3][i]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[3][i]=='X')
		countx++;

		else if(str[3][i]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {
			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // horizontal 4

     countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[i][0]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[i][0]=='X')
		countx++;

		else if(str[i][0]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {
			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // vertical 1

    countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[i][1]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[i][1]=='X')
		countx++;

		else if(str[i][1]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {

			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // vertical 2

    countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[i][2]=='.')
		{
			flag=1;
            blank++;
		}

		else if(str[i][2]=='X')
		countx++;

		else if(str[i][2]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {

			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // vertical 3

         countx=counto=blank=countt=0;
	for(i=0;i<4;i++)
	{
		if(str[i][3]=='.')
		{
			flag=1;
			blank++;
		}

		else if(str[i][3]=='X')
		countx++;

		else if(str[i][3]=='O')
		counto++;

		else
		countt++;
	}

	 if(blank==0&&countt!=4&&!(countx>0&&counto>0))
	 {

			if((countx+countt)==4)
			return 1;

			else if((counto+countt)==4)
			return 2;
	 }

     // vertical 4

	 if(flag==1)
	 return 0;

	 else
	 return 3;

}

int main()
{
int t,res;

scanf("%d",&t);
for(int i=1;i<=t;i++)
{
	for(int i=0;i<4;i++)
	scanf("%s",&str[i]);

	res=check();

	switch(res)
	{

	  case 0 : printf("\nCase #%d: Game has not completed",i);
			   break;

      case 1 : printf("\nCase #%d: X won",i);
			   break;

	  case 2 : printf("\nCase #%d: O won",i);
			   break;

	  case 3 : printf("\nCase #%d: Draw",i);
			   break;
	}
}

//	getch();
	return 0;
}
