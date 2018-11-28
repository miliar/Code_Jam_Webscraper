#include<cstdio>
#include<cstring>
using namespace std;

const int maxlen = 10000;
const int sigma = 30;

bool used[sigma * sigma];
int map[sigma * sigma] , i , j , t , t_case;
char a[maxlen], a2[maxlen];

int main()
{
	freopen("tongues.in","r",stdin);
	freopen("tongues.out","w",stdout);
	
	map['q'] = 'z';
	map['z'] = 'q';
	
	for(j = 1; j <= 3; ++j) {
	
		fgets(a, sizeof(a), stdin);
		fgets(a2 , sizeof(a2) , stdin);
		
		for(i = 0; (a[i] >= 'a' && a[i] <= 'z') || a[i] == ' ' ; ++i) {
			map[a[i]] = a2[i];
			used[a2[i]] = true;
		}
	}
	
	scanf("%d\n",&t);
	
	for(t_case = 1; t_case <= t; ++t_case) {
		
		fgets(a, sizeof(a), stdin);
		
		for(i = 0; (a[i] >= 'a' && a[i] <= 'z') || a[i] == ' '; ++i) 
			a[i] = map[a[i]];
			
		printf("Case #%d: %s",t_case, a);
	}
	
return 0;
}