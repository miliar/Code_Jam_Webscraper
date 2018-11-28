#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;

long long ans = 0;
int n, cases;
int pow2[20];
int x,k;
char str[60010];
int len;
char str2[60010];
int y,groups,ming;
int main()
{
    pow2[0]=1;
    for(x=1;x<18;x++)
    {
        pow2[x]=pow2[x-1]*2;
    }
    freopen("D-small-attempt0.in", "rt", stdin);
    freopen("2.out", "wt", stdout);
    scanf("%d",&cases);
    
    for(int t=0; t<cases; t++)
    {
        ming=9999999;
        int myints[] = {0,1,2,3,4,5};
        scanf("%d",&k);
        sort (myints,myints+k);
        //cout<<myints<<endl;
        scanf("%c",&str[x]);
        gets(str);
        //printf("%d %d\n",k,strlen(str));
        //cout<<str<<endl;
        len = strlen(str);
        
        do {
        for(x=0;x<len/k;++x)
        {
            for(y=0;y<k;y++)
            {
            str2[x*k+y]=str[x*k + myints[y]];
            }
        }
        groups = 1;
        for(x=1;x<len;++x)
        {
            if(str2[x]!=str2[x-1])
                groups++;
        }
        if(groups<ming)
        {
            ming=groups;
         //   cout<<groups<<endl;
          //  cout<<str2<<endl;
        }
        } while ( next_permutation (myints,myints+k) );
        
        /*
            scanf("%d",&k);
        x=0;
        
        choices = pow2[k];
        for(x=0;x<choices;x++)
        {
            
        }
    */
        cout<<"Case #"<<t+1<<": "<<ming<<endl;
    }
    return 0;
}
