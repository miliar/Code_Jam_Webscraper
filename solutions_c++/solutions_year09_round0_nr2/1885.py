#include <iostream>
using namespace std;

int bin[15000];
int ma[110][110];
int a[110][110];
int hash[100];
char ans[110][110];
int direct[4][2] = {{-1 , 0} , {0 , -1} , {0 , 1} , {1 , 0}};
int n , m;

int Find(int x)
{
	if (x == bin[x])
		return x;
	else
		return bin[x] = Find(bin[x]);
}

void Process(int nowx , int nowy)
{
	int ta , tb = -1 , temp;
	int x , y;
	int fa , fb;
	ta = nowx * m + nowy;
	temp = 100;
	for (int i=0 ; i<4 ; i++){

		x = nowx + direct[i][0];
		y = nowy + direct[i][1];
		if (x >=0 && x <n && y>=0 && y<m){

			if (temp > ma[x][y]){

				tb = x * m + y;
				temp = ma[x][y];
			}
		}
	}
	
	if (temp >= ma[nowx][nowy])
		return ;
	fa = Find(ta);
	fb = Find(tb);

	bin[fa] = fb;
}

int main()
{
	freopen("B-small-attempt0.in" , "r" , stdin);
	freopen("B-small-attempt0.out" , "w" , stdout);
	int T;
	int total , temp , tt;
	int cnt = 0;
	int cas = 0;
	scanf("%d" , &T);
	while (T--){

		cas++;
		scanf("%d %d" , &n , &m);
		for (int i=0 ; i<n ; i++){

			for (int j=0 ; j<m ; j++){

				scanf("%d" , &ma[i][j]);
			}
		}
		
		total = n * m;
		for (int i=0 ; i<total ; i++)
			bin[i] = i;

		for (int i=0 ; i<n ; i++){

			for (int j=0 ; j<m ; j++){

				Process(i , j);
			}
		}
		for(int i=0 ; i<n ; i++){

			for (int j=0 ; j<m ; j++){

				temp = i * m + j;
				tt = Find(temp);
				a[i][j] = tt;
			}
		}

		cnt = 0;
		memset(hash , -1 , sizeof(hash));
		for (int i=0 ; i<n ; i++){

			for (int j=0 ; j<m ; j++){

				temp = a[i][j];
				if (hash[temp] == -1){

					hash[temp] = cnt++;
				}
				ans[i][j] = hash[temp] + 'a';
			}
		}
		
		printf("Case #%d:\n" , cas);
		for (int i=0 ; i<n ; i++){

			for (int j=0 ; j<m ; j++){

				if (j == 0)
					printf("%c" , ans[i][j]);
				else
					printf(" %c" , ans[i][j]);
			}
			printf("\n");
		}
	}
}
