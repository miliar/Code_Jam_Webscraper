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


#define PI acos(-1)
#define CLEAR(A) memset(A,0,sizeof(A))
#define SETMAX(A) memset(A,0x7f,sizeof(A))
#define SETM1(A) memset(A,-1,sizeof(A))
#define SQ(A) (A)*(A)

char vs[52][52];
char temp;
int main()
{
	cout << setprecision(9) ;
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int R,C;
		scanf("%d %d\n", &R, &C);
		for(int j=0;j<R;j++)	
		{
			for(int k=0;k<C;k++)
			{
				scanf("%c\n", &vs[j][k]);
			}
		}
		bool wrong = false;
		for(int j=0;j<R;j++)
			for(int k=0;k<C;k++)
			{
				if(vs[j][k] == '#')
				{
					if((j+1) < R && (k+1) < C && (vs[j+1][k]=='#') && (vs[j][k+1]=='#') && (vs[j+1][k+1]=='#'))
					{
						vs[j][k] = '/';
						vs[j][k+1] = '\\';
						vs[j+1][k] = '\\';
						vs[j+1][k+1] = '/';
					}			
					else
					{
						wrong = true;
						goto out;
					}		
				}
			}
out:;
		cout << "Case #" << i << ":" << endl;
    		if(wrong) {
			cout << "Impossible" << endl;
		}
		else
		{
			for(int j=0;j<R;j++)
			{
				for(int k=0;k<C;k++)
				{
					printf("%c", vs[j][k]);
				}
				printf("\n");
			}	
		}
	}

}
