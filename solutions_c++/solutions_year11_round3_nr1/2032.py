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
#include <ctime> 

using namespace std;


int main()
{
	freopen("A-small.in" ,"r", stdin);
	freopen("A-small.out","w", stdout);
	int case_num =0;
	bool done = false;
	scanf("%d\n" , &case_num);
	for(int i = 1 ;i<=case_num ; i++)
	{
		int R_num=0;
		int C_num = 0;
		char matri[60][60] = {0};
		bool matri_need[60] = {false};
		bool impos = false;
		scanf("%d %d\n" , &R_num , &C_num);
		for(int n = 0 ; n<R_num ; n++)
		{
			scanf("%s\n",matri[n] );
		}
		printf("Case #%d:\n",i );
		for(int j= 0 ; j<R_num ; j++)
		{
			int tmp_count =0;
			for(int l = 0 ; l<C_num ; l++)
			{
				if(matri[j][l] == '#')
				{
					tmp_count ++;
				}
			}
			if((tmp_count %2) !=0 )
			{
				impos = true;
				break;
			}
			int tmp_ = 0; //·½Ïò
			
			for(int k = 0; k < C_num ; k++)
			{
				if(matri[j][k] == '#' )
				{
					if(matri_need[k] == true)
					{
						matri_need[k] = false;//µÖÏû
						if(tmp_ ==0)
						{
							matri[j][k] = '\\';
							tmp_ =1;
						}
						else
						{
							matri[j][k] = '/';
							tmp_ =0;
						}
					}
					else
					{
						if(j == (R_num -1))
						{
							impos = true;
							break; break;
						}
						matri_need[k] = true;//
						if(tmp_ ==0)
						{
							matri[j][k] = '/';
							tmp_ =1;
						}
						else
						{
							matri[j][k] = '\\';
							tmp_ =0;
						}
					}
				}
				else
				{
					if(matri_need[k] == true)
					{
						impos = true ;
						break;break;
					}
				}

			}
		}
		if(impos == false)
		{
			for(int m = 0 ;m<R_num ;m++)
			{
				printf("%s\n" , matri[m]);
			}
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}