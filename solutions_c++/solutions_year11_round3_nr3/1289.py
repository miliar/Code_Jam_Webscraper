#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int T;
	scanf("%d",&T);
	int case_num=0;
    int play[10001];
    int N,L,R;
	while(case_num<T)
	{
	    case_num++;
	    scanf("%d%d%d",&N,&L,&R);
	    for(int i=1;i<=N;i++)
	    {
	        scanf("%d",&play[i]);
	    }
	    bool ok=true;
	    int res;
	    for(int i=L;i<=R;i++)
	    {
	        ok=true;
	        for(int j=1;j<=N;j++)
	        {
	            if(play[j]%i!=0 && i%play[j]!=0)
	            {
	                ok=false;
	            }
	            if(!ok)
	            break;
	        }
	        if(ok)
	        {
	            res=i;
	            break;
	        }
	    }
	    if(!ok)
	    {
	        printf("Case #%d: NO\n",case_num);
	    }
	    else
	    {
	        printf("Case #%d: %d\n",case_num,res);
	    }
	}
	return 0;
}
