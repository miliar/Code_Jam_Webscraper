#include<string>
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<vector>
#include<map>
using namespace std;

#define sf scanf
#define pf printf
#define dbg put("OK\n");
#define fo(i,n) for(i=0;i<n;i++)
#define rfo(i,n) for(i=n;i>0;i--)

#define small
//#define large
int main()
{
	#ifdef small
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-out.out","w",stdout);
	#endif
	#ifdef large
	freopen("C-large.in","r",stdin);
	freopen("C-large-out.out","w",stdout);
	#endif
	int i, j,id,t;
	scanf("%d",&t);
	for(id=1;id<=t;id++)
	{
	    int n,l,h;
	    scanf("%d %d %d",&n,&l,&h);
        vector <int> play;
        //play.resize(n);
        for(i=0;i<n;i++)
        {
            cin>>j;
            play.push_back(j);
        }
        printf("Case #%d: ",id);
        sort(play.begin(),play.begin()+n);
        int found=0;
        for(i=l;i<=h;i++)
        {
            //printf("Trying %d\n",i);
            for(j=0;j<n;j++)
            {
                //printf("%d mod %d = %d %d FOUND %d\n",i,play[j],i%play[j],play[j]%i,found);
                if(i%play[j]==0 || play[j]%i==0)
                {found++;}
            }
            if(found==n)
            {
                printf("%d\n",i); break;
            }
            found=0;
            if(i==h)
            {
                printf("NO\n");
            }
        }
    }
    return 0;
}
