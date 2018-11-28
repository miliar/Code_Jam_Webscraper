#include <iostream>
#include <algorithm>
using namespace std;

int a[10];
int b[10] , c[10];
int len , ans;

int cmp(const int &a , const int &b)
{
	return a > b;
}

int GetValue(int lenc)
{
	int ret = 0;
	for (int i=len - 1 ; i>=0 ; i--){

		ret *= 10;
		ret += (c[i]);
	}
	return ret;
}

void Cal(int x , int y)
{
	int temp;
	for (int i=0 ; i<len ; i++){

		c[i] = a[i];
	}
	temp = c[x];
	c[x] = c[y];
	c[y] = temp;

	sort(c , c + y , cmp);
	temp = GetValue(len);
	if (ans == -1)
		ans = temp;
	else{

		if (temp < ans)
			ans = temp;
	}
}

int main()
{
	freopen("B-small-attempt0.in" , "r" , stdin);
	freopen("B-small-attempt0.out" , "w"  ,stdout);
	int t , n , temp;
	int cas = 0;
	scanf("%d" , &t);
	while (t--){

		cas++;
		scanf("%d" , &n);
		len = 0;
		temp = n;
		while (temp){

			a[len++] = temp % 10;
			temp /= 10;
		}

		ans = -1;
		for (int i=0 ; i<len ; i++){

			for (int j=i ; j<len ; j++){

				if (a[i] > a[j]){

					Cal(i , j);
				}
			}
		}

		if (ans != -1){

			printf("Case #%d: %d\n" , cas , ans);
		}
		else{

			temp = -1;
			for (int i=0 ; i<len ; i++){

				if (a[i] != 0){

					if (temp == -1)
						temp = a[i];
					else{

						if (temp > a[i])
							temp = a[i];
					}
				}
			}

			for (int i=0 ; i<len ; i++){

				if (a[i] == temp){

					a[i] = 0;
					break;
				}
			}

			for (int i=0 ; i<len ; i++){

				c[i] = a[i];
			}

			sort(c , c + len , cmp);
			c[len] = temp;

			ans = GetValue(len + 1);
			printf("Case #%d: %d\n" , cas , ans);
		}
	}
	return 0;
}