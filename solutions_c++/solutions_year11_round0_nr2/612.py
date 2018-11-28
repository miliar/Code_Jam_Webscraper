#include <iostream>

using namespace std;

char c[50][5],d[50][5],sin[110],sout[110];
int cn,dn;

char judgec(char a,char b)
{
    for(int k=0;k<cn;k++)
    {
        if((a==c[k][0]&&b==c[k][1])||(a==c[k][1]&&b==c[k][0]))
        {
            return c[k][2];
        }
    }
    return 0;
}

bool judged(char a,char b)
{
    for(int k=0;k<dn;k++)
    {
        if((a==d[k][0]&&b==d[k][1])||(a==d[k][1]&&b==d[k][0]))
        {
            return true;
        }
    }
    return false;
}

int main()
{
    int T,n,i,j,k,l;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>cn;
        for(j=0;j<cn;j++)
        {
            cin>>c[j][0]>>c[j][1]>>c[j][2];
        }
        cin>>dn;
        for(j=0;j<dn;j++)
        {
            cin>>d[j][0]>>d[j][1];
        }
        cin>>n;
        scanf("%s",&sin);
        l=0;
        for(j=0;j<n;j++)
        {
            if(l==0)
            {
                sout[l++]=sin[j];
            }
            else
            {
                bool flag=true;
                char ch;
                if(ch=judgec(sin[j],sout[l-1]))
                {
                    sout[l-1]=ch;
                    flag=false;
                }
                else
                {
                    for(k=0;k<l;k++)
                    {
                        if(judged(sin[j],sout[k]))
                        {
                            l=0;
                            flag=false;
                            break;
                        }
                    }
                }
                if(flag)
                {
                    sout[l++]=sin[j];
                }

            }
        }
        printf("Case #%d: [",i);
		for(j=0;j<l;j++)
		{
			if(j==0)
			{
			    printf("%c",sout[j]);
			}
			else
			{
			    printf(", %c",sout[j]);
			}
        }
        printf("]\n");
    }
    return 0;
}
