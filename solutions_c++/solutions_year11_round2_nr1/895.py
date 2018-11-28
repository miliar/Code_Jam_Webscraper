#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

const int MaxT = 105;

char board[MaxT][MaxT];
double WP[MaxT] , OWP[MaxT] , OOWP[MaxT];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int cs,N;
	scanf("%d",&cs);
	for(int c=1;c<=cs;c++)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%s",board[i]);

		// count WP
		for(int i=0;i<N;i++)
		{
			double win = 0.0 ,  total = 0.0;
			for(int j=0;j<N;j++)
				if(board[i][j] == '0')
					total+=1.0;
				else if(board[i][j] == '1')
					total+=1.0 , win+=1.0;
			WP[i] = win / total;
		}
		// count OWP
		for(int i=0;i<N;i++)
		{
			int op_cnt = 0; double total_WP = 0.0;

			for(int j=0;j<N;j++)
				if(board[i][j] != '.')
				{
					double win = 0.0; int op_cnt2 = 0;
					for(int k=0;k<N;k++)
						if( k!=i && board[k][j] != '.')
						{
							if(board[k][j] == '0')
								win += 1.0;
							op_cnt2++;
						}
					//printf("op_cnt2: %d , win: %.0lf\n",op_cnt2,win);
					op_cnt++ , total_WP += (win / op_cnt2);
				}
			OWP[i] = total_WP / (double)op_cnt;
			//printf("%d: OWP:%lf\n",i,OWP[i]);
		}
		// count OOWP
		for(int i=0;i<N;i++)
		{
			double total = 0.0; int cnt = 0;
			for(int j=0;j<N;j++)
				if(board[i][j] != '.')
					cnt++ , total += OWP[j];
			OOWP[i] = (double)total / cnt;
		}

		printf("Case #%d:\n",c);
		/*for(int i=0;i<N;i++)
			printf("WP: %lf OWP: %lf OOWP: %lf\n",WP[i],OWP[i],OOWP[i]);*/
		for(int i=0;i<N;i++)
			printf("%.12lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25*OOWP[i] );
	}
	return 0;
}
