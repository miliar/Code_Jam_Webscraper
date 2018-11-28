#include<iostream>
#include <algorithm>
using namespace std;
int main()
{
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        int t,x,i,p=0;
        scanf("%d",&t);
        char tmp[40];
        while(t--)
        {
                scanf("%s",tmp);
                int len=strlen(tmp);
                for(i=len;i>0;--i)tmp[i]=tmp[i-1];
                tmp[0]='0';
                tmp[++len]=0;
                next_permutation(tmp,tmp+len);
                printf("Case #%d: ",++p);
                if(tmp[0]!='0')printf("%c",tmp[0]);
                for(i=1;i<len;++i)printf("%c",tmp[i]);
                printf("\n");


        }
        return 0;
}
