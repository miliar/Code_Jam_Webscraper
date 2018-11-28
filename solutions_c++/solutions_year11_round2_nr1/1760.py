#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

char data[105][105];
double wp[105];
double owp[105];
double oowp[105];

int main(int argc, const char* argv[]){
	int caseNum;
	scanf("%d", &caseNum);

	for (int caseId = 1; caseId <= caseNum; ++caseId )
	{
		int teamNum;
		scanf("%d", &teamNum );

		for ( int teamId=0; teamId<teamNum; ++teamId)
		{
			scanf("%s", data[teamId] );
		}

		for ( int i=0; i<teamNum; ++i )
		{
			wp[i]=0;
			double win=0,game=0;
			for ( int j=0; j< teamNum; j++)
			{
				if( data[i][j]=='1' ){
					win++;
					game++;
				}
				else if (data[i][j]=='0'){
					game++;
				}
			}
			wp[i]=win/game;

			//printf( "wp[%d]=%lf\n", i, win/game );
		}

		for ( int i=0; i<teamNum; ++i )
		{
			owp[i]=0;
			int op=0;
			for ( int j=0; j< teamNum; j++)
			{
				if( data[i][j]=='1' || data[i][j]=='0'){
					op++;
					double opowp=0;
					double win=0; 
					double game=0;
					for ( int k=0; k<teamNum; k++) {
						if ( k!=i ){
							if (  data[j][k]=='1'){
								win++;
								game++;

							}
							if ( data[j][k]=='0'){
								game++;
							}
						}
						
					}
					owp[i]+=win/game;
				}
			}
			owp[i]/=(double)op;

			//printf( "owp[%d]=%lf\n", i, owp[i] );
		}

		for ( int i=0; i<teamNum; ++i )
		{
			oowp[i]=0;
			int op=0;
			for ( int j=0; j< teamNum; j++)
			{
				if( data[i][j]=='1' || data[i][j]=='0'){
					op++;
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=op;
			//printf( "oowp[%d]=%lf\n", i, oowp[i] );
		}

		printf( "Case #%d:\n", caseId );
		for ( int i=0; i<teamNum; ++i )
		{
			printf("%.07lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] );
		}
	}
	
	//system("pause");

	return 0;
}