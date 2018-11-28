#include <iostream>
#include <algorithm>
using namespace std;
char ans[25];
int hash[11];
void cmpans(char *a)
{
	int i;
	int len = strlen(a);
	for (i = 0; i < len; i ++) {
		if (a[i] ==ans[i])
			continue;
		if (a[i] < ans[i]){
			for (int k = 0; k < len; k ++)
				ans[k] = a[k];
			//memcpy(ans, a, sizeof (a));
			return;
		}
		if (a[i] > ans[i])
			return;
	}
}
void comp(char *a, char *b)
{
	int i;
	int len = strlen(a);
	for (i = 0; i < len; i ++) {
		if (a[i] == b[i])
			continue;
		if (a[i] < b[i]){
			cmpans(b);
			return;
		}
		if (a[i] > b[i])
			return;
	}
}

int main ()
{
	int test, i, j, cas = 1, len;
	char num[25], tmp[25];
	char tnum[25];
freopen("B-large.in","r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf ("%d", &test);
	while (test --){
		memset(num, 0, sizeof (num));
		memset(tnum, 0, sizeof (tnum));
		memset(hash, 0, sizeof (hash));
		memset(ans, 0, sizeof(ans));
		scanf ("%s", num);
		len = strlen(num);
		for (i = 0; i < len; i ++)
			ans[i] = '9';
		hash[num[0] - '0'] ++;
		for (i = 1; i < len; i ++){
			hash[num[i] - '0'] ++;
			if (num[i] > num[i - 1])
				break;
		}
		printf("Case #%d: ", cas ++);
		if (i >= len){
			sort(num, num + len);
			int k = 0;
			while (num[k] == '0')
				k ++;
			printf("%d0", num[k] - '0');
			hash[num[k] - '0'] --;
			for (j = 0; j < len; j ++){
				if (hash[num[j] - '0']){
					printf("%d", num[j] - '0');
					hash[num[j] - '0'] --;
				}
				
			}
			printf("\n");
			continue;
		}
		int cnt = 0;
		
		for (int k = 0; k < len; k ++)
			tnum[k] = num[k];
		//memcpy(tnum, num, sizeof (tnum));
		while(true){
			for (i = len - 1; i >= 0; i --){
				for (int k = 0; k < len; k ++)
					tmp[k] = tnum[k];
				//memcpy(tmp, tnum, sizeof(tnum));
				for (j = len - 1; j >= 0; j --){
					char temp = tmp[j];
					tmp[j] = tmp[i];
					tmp[i] = temp;
					/*tmp[j] ^= tmp[i];
					tmp[i] ^= tmp[j];
					tmp[j] ^= tmp[i];*/
					comp(num, tmp);
				}
			}
			cnt ++;
			if(cnt == 5)
				break;
			for (int k = 0; k < len; k ++)
				tnum[k] = ans[k];
			//memcpy(tnum, ans, sizeof(ans));
		}
		ans[len] = '\0';
		printf("%s\n", ans);
	}
	return 0;
}
//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//char key[30];
//
//int main()
//{
//	freopen("B-small-attempt1.in","r",stdin);
//	freopen("B-small-attempt1.txt","w",stdout);
//	int T;
//	scanf("%d",&T);
//
//	gets(key);
//
//	int b=1;
//
//	while (T--)
//	{
//		gets(key+1);
//
//		printf("Case #%d: ",b++);
//
//		int i;
//		for(i=1;key[i]!='\0';++i);
//
//		key[0]='0';
//
//		int now=atoi(key);
//		int mm=INT_MAX;
//		int ag=INT_MAX;
//		sort(key,key+i);
//		while (next_permutation(key,key+i))
//		{
//			int x=atoi(key);
//
//			if (x>now)
//			{
//				if (x<mm)
//				{
//					mm=x;
//				}
//			}
//
//			if (x<ag)
//			{
//				ag=x;
//			}
//		}
//
//		printf("%d\n",mm);
//
//	}
//	return 0;
//}
