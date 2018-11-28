#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int d,c,n,t;
int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);
    int i,j,k,l;
    char stack[105];
    int top;
    bool flag;
    char com[40][5];
    char opp[40][5];
    char str[105];
    scanf("%d",&t);
    int cases = 1;
    char a,b;
    while(t--)
    {
        scanf("%d",&c);
        for(i=0;i<c;i++)
        {
            scanf("%s",com[i]);
        }
        scanf("%d",&d);
        for(i=0;i<d;i++)
        {
            scanf("%s",opp[i]);
        }
        scanf("%d",&n);
        scanf("%s",str);
        top = -1;
        for(i=0;i<n;i++)
        {
            if(top==-1) stack[++top] = str[i];
            else {
                for(j=0;j<c;j++)
                {
                    a = com[j][0];
                    b = com[j][1];
                    if((a==stack[top] && b==str[i]) || (a==str[i] && b==stack[top]))
                    {
                        stack[top] = com[j][2];
                        break;
                    }
                }
                if(j==c)
                {
                    flag = 0;
                    for(k=0;k<d;k++)
                    {
                        a = opp[k][0];
                        b = opp[k][1];
                        for(l=0;l<=top;l++)
                        {
//                            printf("%d %c %c\n",l,stack[l],str[i]);
                            if((a==stack[l] && b==str[i]) || (a==str[i] && b==stack[l]))
                            {
//                                printf("debug\n");
                                top = -1;
                                flag = 1;
                                break;
                            }
                        }
                        if(flag) break;
                    }
                    if(!flag)
                    {
                        stack[++top] = str[i];
                    }
                }
            }
//            cout<<"~~"<<i<<endl;
//                for(l=0;l<=top;l++) cout<<stack[l]<<endl;
        }
        printf("Case #%d: [",cases++);
        for(i=0;i<=top;i++)
        {
            if(i) printf(", ");
            printf("%c",stack[i]);
        }
        printf("]\n");
    }
	return 0;
}
