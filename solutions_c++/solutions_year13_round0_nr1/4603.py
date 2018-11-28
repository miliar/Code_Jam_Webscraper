


//		ABHINAV SINGI  		//

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<sstream>
#include<cassert>
#include<cmath>
#include<cstdlib>
#include<queue> 		//FIFO
#include<map>
#include<set>
#include<vector>
#include<cstring>
#include<stack>			//LIFO

using namespace std;
#define pop_count(n) __builtin_popcount(n)
#define FOR(i,a,b) for(int i= (int)a; i<= (int)b; i++)
#define FORD(i,a,b) for(int i= (int)a; i>= (int)b; i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define MP make_pair

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;
#define INF 1000000000
#define ALPHABET_SIZE 26


int main() 
{
	int i,j,k;
	int n,noc,T;
	int arr[1000010]={0};
	cin >> T;
	int count = 0;
	while(T--){
		char inp[5][5];
		int x=-1,y=-1,cnt_dot=0;
		int ans = -1;
		FOR(i,1,4){
			FOR(j,1,4){
				cin >> inp[i][j];
				if(inp[i][j]=='T'){
					x = i;
					y = j;
				}
				if(inp[i][j]=='.')
					cnt_dot++;
			}
		}
		count ++;
		cout << "Case #" << count << ": ";
		if(x>0 && y>0)
			inp[x][y] = 'X';
//rows		
		FOR(i,1,4){
			int flag = 0;
			FOR(j,1,4){
				if(inp[i][j]!='X'){
					flag = 1;
					break;
				}
			}
			if(flag == 0){
				ans = 1;
				break;
			}
		}
//columns		
		FOR(i,1,4){
			int flag = 0;
			FOR(j,1,4){
				if(inp[j][i]!='X'){
					flag = 1;
					break;
				}
			}
			if(flag==0){
				ans = 1;
				break;
			}
		}
//diagonals		
		int flag1 = 0;
		FOR(i1,1,1){
			FOR(i,1,4){
				if(inp[i][i]!='X'){
					flag1 = 1;
					break;
				}
			}
			if(flag1 == 0){
				ans = 1;
				break;
			}

			flag1 = 0;
			FOR(i,1,4){
				if(inp[i][5-i]!='X'){
					flag1 = 1;
					break;
				}
			}
			if(flag1 == 0){
				ans = 1;
				break;
			}
		}
		if(ans==1){
			cout << "X won" << endl;
			continue;
		}


		if(x>0 && y>0)
			inp[x][y] = 'O';
//rows		
		FOR(i,1,4){
			int flag = 0;
			FOR(j,1,4){
				if(inp[i][j]!='O'){
					flag = 1;
					break;
				}
			}
			if(flag == 0){
				ans = 0;
				break;
			}
		}
//columns		
		FOR(i,1,4){
			int flag = 0;
			FOR(j,1,4){
				if(inp[j][i]!='O'){
					flag = 1;
					break;
				}
			}
			if(flag==0){
				ans = 0;
				break;
			}
		}
//diagonals		
		flag1 = 0;
		FOR(i1,1,1){
			FOR(i,1,4){
				if(inp[i][i]!='O'){
					flag1 = 1;
					break;
				}
			}
			if(flag1 == 0){
				ans = 0;
				break;
			}

			flag1 = 0;
			FOR(i,1,4){
				if(inp[i][5-i]!='O'){
					flag1 = 1;
					break;
				}
			}
			if(flag1 == 0){
				ans = 0;
				break;
			}
		}
		if(ans==0){
			cout << "O won" << endl;
			continue;
		}
		else{
			if(cnt_dot==0)
				cout << "Draw" << endl;
			else
				cout << "Game has not completed" << endl;
		}

	}
	return 0;
}
