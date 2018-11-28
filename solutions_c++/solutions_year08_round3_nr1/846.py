#define _CRT_SECURE_NO_DEPRECATE
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

char buf[1024];
char* read(void){return gets(buf);}

int main(void)
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	for(int i=0,e=atoi(read());i<e;i++)
	{
		int p , k , l , tmp;
		scanf("%d %d %d\n\r",&p,&k,&l);

		vector<int> pushcnt;
		for(int x=0;x<l;x++)
		{
			if(x < l-1)
				scanf("%d",&tmp);
			else
				scanf("%d\n\r",&tmp);

			pushcnt.push_back(tmp);
		}

		sort(pushcnt.begin(),pushcnt.end());
		
		int result = 0;
		int cnt = 0;
		for(int z=pushcnt.size()-1;z >= 0 ;z--)		
		{
			int press = (int)(cnt / k) + 1;
			cnt++;

			result += pushcnt[z] * press;
		}
		
		printf("Case #%d: %d\r\n",i+1,result);
	}
	return 0;
}