#include <iostream>
#include <queue>
using namespace std;

class node
{
    public:
    int g;
    int last;
    node(int _g,int _l){g=_g,last=_l;}
};
queue <node> Q;
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
	int T,r,k,n;
	int g[20];
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
	    scanf("%d %d %d",&k,&r,&n);
	    while(!Q.empty())Q.pop();
	    for(int i=0;i<n;i++)
	    {
	        scanf("%d",&g[i]);
	        Q.push(node(g[i],-1));
	    }
	    int ans=0;
	    for(int i=0;i<k;i++)
	    {
	        int now=0;
	        while(true)
	        {
	            node tmp=Q.front();
	            if(tmp.last==i)
	            break;
	            else if(now+tmp.g>r)
	            break;
	            else
	            {
	                Q.pop();
	                now+=tmp.g;
	                Q.push(node(tmp.g,i));
                }
            }
            ans+=now;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}
