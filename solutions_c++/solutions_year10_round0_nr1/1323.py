#include <stdio.h>
#include <string.h>
#include <bitset>
using std::bitset;
int main()
{

	long long m,n,i,j,T;
	bool judge;
	scanf("%I64d",&T);
	for(i=0;i<T;i++)
	{
        scanf("%I64d%I64d",&m,&n);
        judge=true;
        bitset<64>bitvec(n);
        for(j=0;j<m;j++)
        {
            if(!bitvec[j]){
            judge=false;
            break;
            }
        }
       if(!judge)
       printf("Case #%I64d: OFF\n",i+1);
       else
       printf("Case #%I64d: ON\n",i+1);
    }
	return 0;
}
