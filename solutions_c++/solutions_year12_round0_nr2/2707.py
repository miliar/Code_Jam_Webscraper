#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    //freopen("t.txt","r",stdin);
    //freopen("t1.txt","w",stdout);
    int t,s,n,p,caseno,temp,cc;
    scanf("%d",&t);
    for(caseno=1;caseno<=t;caseno++)
    {
        scanf("%d%d%d",&n,&s,&p);
        int sum=0;
        while(n--)
        {
            scanf("%d",&temp);
            cc=p*3-2;
            if(p==0) sum++;
            else if(p==1) {if(temp>0) sum++;}
            else if(temp>=cc) sum++;
            else if(s>0&&cc-2==temp&&cc-2>=0) {s--;sum++;}
            else if(s>0&&cc-1==temp&&cc-1>=0) {s--;sum++;}
        }
        printf("Case #%d: %d\n",caseno,sum);
    }
    return 0;
}
