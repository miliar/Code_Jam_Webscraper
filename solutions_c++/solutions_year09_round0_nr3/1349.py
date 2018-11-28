#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
	int T,t;
	cin>>T;
	char str[1000]={0};
	const char ob[] = " welcome to code jam";
	cin.getline(str,1000);
	for(t=1;t<=T;++t)
	{
		cin.getline(str+1,1000);
		str[0]=' ';
		int d[501][21]={0};
		int i,j;
		int N= strlen(str);
		for(i=1;i<N;i++)
			for(j=1;j<strlen(ob);j++)
				if(str[i]==ob[j])
					d[i][j]=(d[i-1][j]+d[i-1][j-1]+(j==1?1:0))%10000;
				else 
					d[i][j]=d[i-1][j];
		printf("Case #%d: %0.4d\n",t,d[N-1][strlen(ob)-1]);
	}
	return 0;
}