#include<stdio.h>
#include<conio.h>

int main()
{
	
	int x, T,N,K,r,c,i,j,cnt;
	char b[55][55],ch,B,R;
	
	FILE * ifp=fopen("A-large.in","r");
	FILE * ofp=fopen("A-large.out","w");
	
	fscanf(ifp,"%d\n",&T);
	for (x=1;x<=T;x++)
	{
		fscanf(ifp,"%d %d\n",&N,&K);

		for(r=0;r<N;r++)
		{
			for(c=0;c<N;c++)
				b[r][c] = fgetc(ifp);
			fgetc(ifp);
		}
		for(r=0;r<N;r++)
		{
			for(c=N-2;c>=0;c--)
			{
				if(b[r][c]!= '.' )
				{
					for(i=c+1;i<N&&b[r][i]=='.';i++);
					if (b[r][i-1] == '.')
					{
						b[r][i-1] = b[r][c];	
						b[r][c] = '.';
					}
				}
			}
		}
			B='N';R='N';
			for(r=0;r<N &&(B=='N' || R=='N');r++)
				for(c=0;c<N && (B=='N' || R=='N');c++)
				{
					if(b[r][c] != '.')
						ch=b[r][c];
					else
						continue;
					if(ch=='B' && B=='Y') continue;
					if(ch=='R' && R=='Y') continue;

					
					for(i=r+1,cnt=1;i<N ;i++)
					{
						if (b[i][c] == ch)
							cnt++;
						else
							break;
						if (cnt==K) break;
					}
					if(cnt==K) 
					{
						if(ch=='B')
							B='Y';
						else
							R='Y';
						continue;
					}

					for(i=c+1,cnt=1;i<N ;i++)
					{
						if (b[r][i] == ch)
							cnt++;
						else
							break;
						if (cnt==K) break;
					}
					if(cnt==K) 
					{
						if(ch=='B')
							B='Y';
						else
							R='Y';
						continue;
					}
					for(i=r+1,j=c+1,cnt=1;i<N && j<N ;i++,j++)
					{
						if (b[i][j] == ch)
							cnt++;
						else
							break;
						if (cnt==K) break;
					}
					if(cnt==K) 
					{
						if(ch=='B')
							B='Y';
						else
							R='Y';
						continue;
					}
					for(i=r+1,j=c-1,cnt=1;i<N && j>=0 ;i++,j--)
					{
						if (b[i][j] == ch)
							cnt++;
						else
							break;
						if (cnt==K) break;
					}
					if(cnt==K) 
					{
						if(ch=='B')
							B='Y';
						else
							R='Y';
						continue;
					}
				}

				if(B=='Y' && R=='Y')
					fprintf(ofp,"Case #%d: Both\n",x);
				else
				{if(B=='Y')
					fprintf(ofp,"Case #%d: Blue\n",x);
				else
				{
					if(R=='Y')
						fprintf(ofp,"Case #%d: Red\n",x);
					else
						fprintf(ofp,"Case #%d: Neither\n",x);

				}
				}


	}

	fclose(ifp);
	fclose(ofp);
	return 0;
	
}
