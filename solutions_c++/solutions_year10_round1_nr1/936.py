
#include <stdio.h>
#include <vector>


int main(int argc, char* argv[])
{

	freopen("c:\\A-large.in","r",stdin);
	freopen("C:\\A-large.out","w",stdout);

	
	int T = 0;

	scanf("%d", &T);
	char line[51] = {0};
	char dummy[10] = {0};

	
	for(int t = 0 ; t < T ; t++)
	{
		int N = 0;
		int K = 0;
		std::vector<std::vector<char>> matrix;
		std::vector<int> count_each_line;
		scanf("%d %d", &N, &K);
		gets(dummy);

		matrix.resize(N);
		count_each_line.resize(N, 0);
		int startX = -1;
		int startY = -1;
		int endX = N-1;
		int endY = N-1;
		for(int n = 0 ; n < N ; n++)
		{
			matrix[n].resize(N, '.');
			gets(line);

			for(int c = N-1 ; c >=0 ;c--)
			{
				if(line[c]=='R' || line[c]=='B')
				{
					if(startX == -1 && startY ==-1)
					{
						startX = n;
						startY = 0;
					}
					matrix[n][count_each_line[n]] = line[c];

					endX = n;
					endY = count_each_line[n];

					count_each_line[n]++;
				}
			}
		}
		
		// judge
		bool rwin = false;
		bool bwin = false;

		if(startX == -1 || startY == -1)
			goto END;
		// -
		for(int i = startX ; i <= endX ; i++)
		{
			int RCC = 0;
			int BCC = 0;
			for(int j = 0 ; j < count_each_line[i] ; j++)
			{
				int c = matrix[i][j];
				if(c == 'R')
				{
					RCC++;
					BCC = 0;
					if(RCC == K) rwin = true;
				}
				else if(c=='B')
				{
					RCC=0;
					BCC++;
					if(BCC == K) bwin = true;
				}
				else
				{
					RCC=0;
					BCC=0;
				}

				if(rwin && bwin)
				{
					goto END;
// 					i = endX+1;
// 					break;
				}
			}
		}
		
		if (!rwin || !bwin)
		// |
		for(int j = startY ; j <=endY ; j++)
		{
			int RCC = 0;
			int BCC = 0;
			for(int i = startX ; i <= endX ; i++ )
			{
				int c = matrix[i][j];
				if(c == 'R')
				{
					RCC++;
					BCC = 0;
					if(RCC == K) rwin = true;
				}
				else if(c=='B')
				{
					RCC=0;
					BCC++;
					if(BCC == K) bwin = true;
				}
				else
				{
					RCC=0;
					BCC=0;
				}

				if(rwin && bwin)
				{
					goto END;
// 					i = endX+1;
// 					break;
				}
			}
		}

		if (!rwin || !bwin)
			// \  
			for(int i = startX ; i <= endX ; i++)
			{
				
				for(int j = 0 ; j < count_each_line[i] ; j++)
				{
					int x = i;
					int y = j;
					int RCC = 0;
					int BCC = 0;
					while( 0<= x && x<N && 0<=y && y<N )
					{
						int c = matrix[x][y];
						if(c == 'R')
						{
							RCC++;
							BCC = 0;
							if(RCC == K) rwin = true;
						}
						else if(c=='B')
						{
							RCC=0;
							BCC++;
							if(BCC == K) bwin = true;
						}
						else
						{
							RCC=0;
							BCC=0;
						}

						if(rwin && bwin)
						{
							goto END;
// 							i = endX+1;
// 							j = count_each_line[i]+1;
// 							break;
						}

						x++;
						y--;
					}
				}
			}

		if (!rwin || !bwin)
			// /
			for(int i = startX ; i <= endX ; i++)
			{
				for(int j = 0 ; j < count_each_line[i] ; j++)
				{
					int x = i;
					int y = j;
					int RCC = 0;
					int BCC = 0;
					while( 0<= x && x<N && 0<=y && y<N )
					{
						int c = matrix[x][y];
						if(c == 'R')
						{
							RCC++;
							BCC = 0;
							if(RCC == K) rwin = true;
						}
						else if(c=='B')
						{
							RCC=0;
							BCC++;
							if(BCC == K) bwin = true;
						}
						else
						{
							RCC=0;
							BCC=0;
						}

						if(rwin && bwin)
						{
							goto END;
// 							i = endX+1;
// 							j = count_each_line[i]+1;
// 							break;
						}

						x++;
						y++;
					}
				}
			}

END:
		printf("Case #%d: ", t+1);
		if(rwin && bwin)
			printf("%s\n", "Both");
		else if(rwin)
			printf("%s\n", "Red");
		else if(bwin)
			printf("%s\n", "Blue");
		else
			printf("%s\n", "Neither");
	}

	return 0;
}