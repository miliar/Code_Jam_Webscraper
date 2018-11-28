#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;

void init();
void solve();
void print();
int Orange[101],Black[101],num[101];
char co[101];
int n,ans;

int main()
{
    freopen("button.in","r",stdin);
    freopen("button.out","w",stdout);
    
    int tt;
    scanf("%d", &tt);
    for(int i=0; i<tt; i++)
    {
        init();
        solve();
        printf("Case #%d: ", i+1);
        print();
    }
    
    return 0;    
}

void init()
{
	memset(co,0,sizeof(co));
	memset(Orange,0,sizeof(Orange));
	memset(Black,0,sizeof(Black));
	memset(num,0,sizeof(num));
	scanf("%d", &n);
	for(int i=0; i<n; i++)
	{
		scanf("%c%c%d", &co[i], &co[i], &num[i]);
		if(co[i]=='O') Orange[++Orange[0]]=i;
		else Black[++Black[0]]=i; 
	}
}

void solve()
{
	int pBlack=1,pOrange=1,nBlack=1,nOrange=1;
	ans=0;
	for(int i=0; i<n; i++)
	{
		if(pBlack<=Black[0] && (pOrange>Orange[0] || Black[pBlack]<Orange[pOrange]))
		{
			int now=abs(nBlack-num[Black[pBlack]])+1;
			nBlack=num[Black[pBlack]]; pBlack++; 
			if(pOrange<=Orange[0])
			{
				if(abs(nOrange-num[Orange[pOrange]])>now)
				{
					if(num[Orange[pOrange]]-nOrange>0) nOrange+=now;
					else nOrange-=now;
				}
				else nOrange=num[Orange[pOrange]];
			}
			ans+=now;
		}
		else if(pOrange<=Orange[0] && (pBlack>Black[0] || Black[pBlack]>Orange[pOrange]))
		{
			int now=abs(nOrange-num[Orange[pOrange]])+1;
			nOrange=num[Orange[pOrange]]; pOrange++; 
			if(pBlack<=Black[0])
			{
				if (abs(nBlack-num[Black[pBlack]])>now)
				{
					if(num[Black[pBlack]]-nBlack>0) nBlack+=now;
					else nBlack-=now;
				}
				else nBlack=num[Black[pBlack]];
			} 
			ans+=now;
		}
	}
}

void print()
{
	printf("%d\n", ans);
}
