#include<iostream>
#include<stdio.h>
#include<sstream>
#include<vector>
#include<algorithm>
#include<string.h>
#include<bitset>

using namespace std;

int main()
{
	int i,j,k,l,m,n,t,exp,x,o,ldx,ldo,rdx,rdo,flag=0,win=0;
	char a[7][7];
	string s;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
	    flag=0;
	    win=0;
		for(i=0;i<4;i++)
		{
                x=0;
                o=0;
				cin >> s;
                for(j=0;j<s.length();j++)
                {

                    a[i][j]=s[j];
                    if(a[i][j]=='X')
                        x++;
                        else if(a[i][j]=='O')
                        o++;
                        else if(a[i][j]=='T')
                        {
                            x++;
                            o++;
                        }
                        else if(a[i][j]=='.')
                        flag=1;
                }
                a[i][4]=x;
                a[i][5]=o;

		}
		ldx=0;rdx=0;ldo=0;rdo=0;
		for(i=0;i<4;i++)
		{
		    x=0;
		    o=0;

		    for(j=0;j<4;j++)
		    {
		        if(a[j][i]=='X')
                {
                    x++;
                    if(i==j)
                    ldx++;
                    if(i+j==3 && i!=j)
                    rdx++;
                }
                else if(a[j][i]=='O')
                {
                    o++;
                    if(i==j)
                    ldo++;
                    if(i+j==3 && i!=j)
                    rdo++;
                }
                else if(a[j][i]=='T')
                {
                        x++;
                        o++;
                        if(i==j)
                        {
                            ldx++;
                            ldo++;
                        }
                        if(i+j==3 && i!=j)
                        {
                            rdx++;
                            rdo++;
                        }
                }



		    }
		    //printf("\n%d %d\n",x,o);
		    if(x==4 || ldx == 4 || rdx==4)
		    {
		        printf("Case #%d: X won\n",k);
		        win=1;
		        break;
		    }
		    else if(o==4 || ldo== 4 || rdo == 4)
		    {
		        printf("Case #%d: O won\n",k);
		        win=1;
		        break;
		    }

		}
		for(i=0;i<4;i++)
		{
		    if(a[i][4]==4 && win == 0)
		    {
		        printf("Case #%d: X won\n",k);
		        win=1;
                	break;
		    }
		    else if(a[i][5]==4 && win ==0)
		    {
		        printf("Case #%d: O won\n",k);
		        win=1;
                	break;
		    }

		}
		if(win==0 && flag==0)
		printf("Case #%d: Draw\n",k);
		if(win==0 && flag==1)
		printf("Case #%d: Game has not completed\n",k);

		}



	return 0;
}

