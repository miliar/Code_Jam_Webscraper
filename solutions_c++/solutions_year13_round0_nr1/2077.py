#include<bits/stdc++.h>
using namespace std;
#define x getchar()
#define y putchar

inline void out(int k)
{
    int n=k,i=0;
    char ch[15];
    if(n<=0)
    {
        if(n==0)
            y('0');
        else
            y('-');
        n=n*-1;
    }
    while(n>0)
    {
        ch[i]=(n%10)+'0';
        n=n/10;
        i++;
    }
    while(i>0)
    {
        y(ch[i-1]);
        i--;
    }
    y('\n');
}
inline void inp(int &n)
{
    n=0;
    int ch=x,sign=1;
    while( ch < '0' || ch > '9' )
    {
        if(ch=='-')
            sign=-1;
        ch=x;
    }
    while( ch >= '0' && ch <= '9' )
        n=(n<<3)+(n<<1)+ ch-'0', ch=x;
    n=n*sign;
}

int main()
{
	int T;
	inp(T);
	int C = 1;
	while(T--)
	{
		char A[4][5];
		int i,j;
		
		for(i=0;i<4;i++)
			scanf("%s",A[i]);
			
		//printf("hi\n");
		int flag = 0;
		for(i=0;i<4;i++)
		{
			if(strcmp(A[i],"XXXX")==0 ||strcmp(A[i],"TXXX")==0 || strcmp(A[i],"XTXX")==0 || strcmp(A[i],"XXTX")==0 || strcmp(A[i],"XXXT")==0)
			{
				printf("Case #%d: X won\n",C);
				flag = 1;
				C++;
				getchar();
				break;
			}
			else if(strcmp(A[i],"OOOO")==0 || strcmp(A[i],"TOOO")==0 || strcmp(A[i],"OTOO")==0 || strcmp(A[i],"OOTO")==0 || strcmp(A[i],"OOOT")==0)
			{
				printf("Case #%d: O won\n",C);
				flag = 1;
				C++;
				getchar();
				break;
			}
		}
		if(flag==1)
			continue;
		
		char S[5];
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				S[j] = A[j][i];
			}
			S[j] = '\0';
			
			if(strcmp(S,"XXXX")==0 ||strcmp(S,"TXXX")==0 || strcmp(S,"XTXX")==0 || strcmp(S,"XXTX")==0 || strcmp(S,"XXXT")==0)
			{
				printf("Case #%d: X won\n",C);
				flag = 1;
				getchar();
				C++;
				break;
			}
			else if(strcmp(S,"OOOO")==0 || strcmp(S,"TOOO")==0 || strcmp(S,"OTOO")==0 || strcmp(S,"OOTO")==0 || strcmp(S,"OOOT")==0)
			{
				printf("Case #%d: O won\n",C);
				flag = 1;
				C++;
				getchar();
				break;
			}
		}
		if(flag==1)
			continue;
		
		S[0] = A[0][0];
		S[1] = A[1][1];
		S[2] = A[2][2];
		S[3] = A[3][3];
		S[4] = '\0';
		
		if(strcmp(S,"XXXX")==0 ||strcmp(S,"TXXX")==0 || strcmp(S,"XTXX")==0 || strcmp(S,"XXTX")==0 || strcmp(S,"XXXT")==0)
		{
			printf("Case #%d: X won\n",C);
			flag = 1;
			getchar();
			C++;
		}
		else if(strcmp(S,"OOOO")==0 || strcmp(S,"TOOO")==0 || strcmp(S,"OTOO")==0 || strcmp(S,"OOTO")==0 || strcmp(S,"OOOT")==0)
		{
			printf("Case #%d: O won\n",C);
			flag = 1;
			C++;
			getchar();
		}
		
		if(flag==1)
			continue;
			
		S[0] = A[0][3];
		S[1] = A[1][2];
		S[2] = A[2][1];
		S[3] = A[3][0];
		S[4] = '\0';
		
		if(strcmp(S,"XXXX")==0 ||strcmp(S,"TXXX")==0 || strcmp(S,"XTXX")==0 || strcmp(S,"XXTX")==0 || strcmp(S,"XXXT")==0)
		{
			printf("Case #%d: X won\n",C);
			flag = 1;
			C++;
			getchar();
		}
		else if(strcmp(S,"OOOO")==0 || strcmp(S,"TOOO")==0 || strcmp(S,"OTOO")==0 || strcmp(S,"OOTO")==0 || strcmp(S,"OOOT")==0)
		{
			printf("Case #%d: O won\n",C);
			flag = 1;
			C++;
			getchar();
		}
		
		if(flag==1)
		{
			//printf("hey\n");
			continue;
		}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)	
			{
				if(A[i][j]=='.')
				{
					printf("Case #%d: Game has not completed\n",C);
					flag = 1;
					C++;
					getchar();
					break;
				}
			}
			if(flag==1)
				break;
		}
		
		if(flag==1)
			continue;
		printf("Case #%d: Draw\n",C);
		C++;
		getchar();
	}
	
	return 0;
}