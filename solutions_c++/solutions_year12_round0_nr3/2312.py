#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>

using namespace std;

int numlen(int num)
{
	char buf[16];
	sprintf(buf, "%d", num);
	return strlen(buf);
}

int rotate(int num, int len)
{
	int x = num % 10;
	return x*pow(10,len-1) + num/10;
}

int main(int argc, const char *argv[])
{
	int cases, casen=0;
	int A, B, num;
	int answer;

	scanf("%d\n", &cases);
	while(casen<cases){
		scanf("%d%d", &A, &B);
		answer = 0;
		for(num=A; num<B; num++){
			int len = numlen(num), n = num;
			int i;
			set<int> mem;
			set<int>::const_iterator it;
			for(i=0; i<len-1; i++){
				n = rotate(n,len);
				mem.insert(n);
			}
			for(it=mem.begin(); it!=mem.end(); it++){
				n = *it;
				if(num<n && n<=B)
					answer++;
			}
		}
		printf("Case #%d: %d\n", ++casen, answer);
	}
	return 0;
}
