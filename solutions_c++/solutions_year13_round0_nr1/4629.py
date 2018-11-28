#include <vector>
#include <unistd.h>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

using namespace std;

#define PI 3.141592653589
#define DEG2RAD(deg) (deg * PI / 180)
const int INF = 2000000000;

typedef vector <int> VI ;
typedef vector <double> VD ;
typedef pair<int,int> PII;

#define fi(i,a,b) for(int i = a ; i < b ; i++)
#define fd(i,a,b) for(int i = a ; i > = b ; i--)
#define REP(i,n) fi(i,0,n)
#define pb push_back
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
#define SZ(a) (int) (a).size()
#define VS vector <string> 
#define prnt(a,n) REP(i,n) cout<<a[i] << " " ; cout << endl

int main()
{
	int T=0,count=1;
	cin >> T;
	while(T--)
	{
		char **Matrix;
		Matrix = (char **)malloc(sizeof(char *)*4);
		REP(i,4)
		{
			Matrix[i] = (char *)malloc(sizeof(char)*5);
			memset(Matrix[i],'\0',sizeof(Matrix[i]));
		}
		REP(i,4)
			scanf("%s",Matrix[i]);

		/*
		REP(i,4)
		{
			REP(j,4)
				printf("%c",Matrix[i][j]);
			printf("\n");
		}
		printf("\n");
		*/


		int notComplete=0,flagX=0,flagO=0,cou=0,once=0;
		REP(i,4)
		{
			cou=0;
			REP(j,4)
			{
				if(Matrix[i][j]=='T' || Matrix[i][j]=='X')
					cou++;
				if(notComplete==0 && Matrix[i][j]=='.')
				{				
					notComplete=1;
				}
			}
			if(cou==4)
			{
				flagX=1;
				break;
			}
			cou=0;
			REP(j,4)
			{
				if(Matrix[j][i]=='T' || Matrix[j][i]=='X')
					cou++;
			}
			if(cou==4)
			{
				flagX=1;
				break;
			}
			cou=0;
			if(once==0)
			{
				once=1;
				int cou1=0;
				REP(j,4)
				{
					if(Matrix[j][j]=='T' || Matrix[j][j]=='X')
						cou1++;
				}
				if(cou1==4)
				{
					flagX=1;
					break;
				}
				cou1=0;

				REP(j,4)
				{
					if(Matrix[j][3-j]=='T' || Matrix[j][3-j]=='X')
						cou1++;
				}
				if(cou1==4)
				{
					flagX=1;
					break;
				}
			}
		}
		once=0;
		if(flagX==0)
		{
			REP(i,4)
			{
				int cou=0;
				REP(j,4)
				{
					if(Matrix[i][j]=='T' || Matrix[i][j]=='O')
						cou++;
				}
				if(cou==4)
				{
					flagO=1;
					break;
				}
				cou=0;
				REP(j,4)
				{
					if(Matrix[j][i]=='T' || Matrix[j][i]=='O')
						cou++;
				}
				if(cou==4)
				{
					flagO=1;
					break;
				}
				if(once==0)
				{
					once=1;
					int cou1=0;
					REP(j,4)
					{
						if(Matrix[j][j]=='T' || Matrix[j][j]=='O')
							cou1++;
					}
					if(cou1==4)
					{
						flagO=1;
						break;
					}
					cou1=0;
					REP(j,4)
					{
						if(Matrix[j][3-j]=='T' || Matrix[j][3-j]=='O')
							cou1++;
					}
					if(cou1==4)
					{
						flagO=1;
						break;
					}
				}
			}
		}
		if(flagX==1)
		{
			printf("Case #%d: X won\n",count);
		}
		else if(flagO==1)
		{
			printf("Case #%d: O won\n",count);
		}
		else if(flagX==0 && flagO==0 && notComplete==1)		
		{
			printf("Case #%d: Game has not completed\n",count);
		}
		else
		{
			printf("Case #%d: Draw\n",count);
		}
		count++;
	}
	return 0;
}
