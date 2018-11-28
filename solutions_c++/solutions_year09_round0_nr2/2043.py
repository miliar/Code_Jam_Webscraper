#include <vector>
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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

const int maxn=100000+5;

int h,w;
int L[102][102];
int B[102][102];
char basin_counter;

void init()
{
	scanf("%d %d",&h,&w);
	
	for (int i=0;i<102;i++) 
	{
		for (int k=0;k<102;k++) 
		{
			L[i][k] = 10001;
			B[i][k] = -1;
		}
	}
	
	for (int i=1;i<=h;i++) 
	{
		for (int k=1;k<=w;k++) 
		{
			scanf("%d",&L[i][k]);
		}
	}
	
	basin_counter = 0;
}
void solve()
{
	int max_number = 0;
	for (int i=1; i<=h; i++)
	{
		for(int k=1; k<=w; k++)
		{
			if(L[i][k]>max_number)
			{
				max_number = L[i][k];
			}
		}
	}
	
	int done=0;
	while(done==0)
	{
		int row = -1;
		int col = -1;
		
		for (int i=1; i<=h && row == -1 && col == -1; i++)
		{
			for(int k=1; k<=w && row == -1 && col == -1; k++)
			{
				if(B[i][k] == -1 && L[i][k] == max_number){
					row = i;
					col = k;
				}
			}
		}
		
		if(col==-1 && row ==-1)
		{
			if(max_number == 0)
			{
				break;
			} else
			{
				max_number --;
			}
		}else
		{
			basin_counter ++;
			int sink_or_merged = 0;
			while(sink_or_merged==0)
			{
				int neigh[5][2];
				
				neigh[0][0] = row;		// se stessa - riga
				neigh[0][1] = col;       // se stessa - colonna
				neigh[1][0] = row-1;	// nord - riga
				neigh[1][1] = col;		// nord - colonna
				neigh[2][0] = row;		// west - riga
				neigh[2][1] = col-1;	// west - colonna
				neigh[3][0] = row;		// east - riga
				neigh[3][1] = col+1;	// east - colonna
				neigh[4][0] = row+1;	// south - riga
				neigh[4][1] = col;      // south - colonna
				
				B[row][col] = basin_counter;
				
				int next_row = -1;
				int next_col = -1;
				for(int n1=0; n1<5 && next_row == -1 && next_col == -1;n1++)
				{
					int is_lower = 1;
					for(int n2=0;n2<5;n2++)
					{
						if(L[neigh[n1][0]][neigh[n1][1]] > L[neigh[n2][0]][neigh[n2][1]])
						{
							is_lower = false;
						}
					}
					
					if(is_lower==1)
					{
						next_row = neigh[n1][0];
						next_col = neigh[n1][1];
					}
				}

				if(next_row == row && next_col == col)
				{
					sink_or_merged = 1;
				}else if(B[next_row][next_col] != -1)
				{
					int dest_basin = B[next_row][next_col];
					for (int bi=1; bi<=h; bi++)
					{
						for(int bk=1; bk<=w; bk++)
						{
							if(B[bi][bk] == basin_counter)
							{
								B[bi][bk] = dest_basin;
							}
						}
					}
					basin_counter --;
					sink_or_merged = 1;
				}else
				{
					row = next_row;
					col = next_col;
				}
				
			}
		}
	}
	
	char last_char = 'a';
	for (int i=1; i<=h; i++)
	{
		for(int k=1; k<=w; k++)
		{
			if( B[i][k] < 'a' )
			{
				char basil_to_change = B[i][k];
				for (int bi=1; bi<=h; bi++)
				{
					for(int bk=1; bk<=w; bk++)
					{
						if( B[bi][bk] == basil_to_change ){
							B[bi][bk] = last_char;
						}
					}
				}
				last_char ++;	
			}
		}
	}
		
}

int main()
{
			  
	//	freopen("..\\A.in","r",stdin);
	//  freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	//	freopen("..\\A-small-attempt1.in","r",stdin);freopen("..\\A-small-attempt1.out","w",stdout);
		freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d:\n",caseId);
		init();
		solve();
		
		for (int i=1; i<=h; i++)
		{
			for(int k=1; k<=w; k++)
			{
				printf("%c",B[i][k]);
				if(k+1<=w){
					printf(" ");
				}
			}
			if(i+1<=h || caseId+1<=testcase){
				printf("\n");
			}
		}
		
		fflush(stdout);
	}
	return 0;
}

//ENDSOURCECODE_BY_ACRUSH_TOPCODER

