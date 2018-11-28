#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("debug\\A-large.in","r",stdin); 
    freopen("debug\\out.txt","w",stdout); 
    int i=0,T;
    scanf("%d",&T);
    while((i++)!=T){
        long N,K;
        scanf("%ld%ld",&N,&K);
		_int64 j=1;
		for(int z=0;z<N;z++)
			j*=2;
        if((K+1)%j==0)
        printf("Case #%d: ON\n",i);
        else
        printf("Case #%d: OFF\n",i);
    }
    fclose(stdin);//关闭文件 
    fclose(stdout);//关闭文件
    return 0;
}
