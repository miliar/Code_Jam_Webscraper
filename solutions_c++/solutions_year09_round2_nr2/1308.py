

#include<string>
#include<iostream>
#include<sstream>
#include<set>
using namespace std;
#define ns(x) scanf("%s",&x)
#define ni(x) scanf("%d",&x)
char buf[128], cnt0[128], cnt1[128];

int main()
{

	
    int nks;
	ni(nks);
    //
    for(int k=1;k<=nks;k++)
    {
    	
		printf("Case #%d: ", k);
		ns(buf);
		memset(cnt1,0,sizeof(cnt1));
		int i;
		for(i=0;buf[i];++i)
			cnt0[buf[i] - '0']++;
		
		cnt1[buf[i-1]-'0'] ++;
		int lowb = 0;
		for(i--; i>0; i--)
		{
			cnt1[buf[i-1]-'0']++;
			if( buf[i]>buf[i-1] )
			{
				lowb = buf[i-1] - '0';
				break;
			}
		}
		
		int j;
		for(j=0;j<i-1;j++)
			printf("%c",buf[j]);

		for(j=1;j<10;j++)
			if(cnt1[j] && j>lowb)
			{
				printf("%d",j);
				cnt1[j]--;
				if (i == 0)	cnt1[0]++;
				break;
			}

		for(j=0;j<10;j++)
			while(cnt1[j])
			{
				printf("%d",j);
				cnt1[j]--;
			}
		puts("");
	}
}
