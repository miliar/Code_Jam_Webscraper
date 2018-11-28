#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
char s[110][110];
double wp[110];
int win[110];
int tot[110];
double owp[110];
double oowp[110];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,n,i,j,k,c;
    double sum;
    int ca=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
          scanf("%s",s[i]);
        for(i=0;i<n;i++)
        {
            int s1=0,s0=0;
            for(j=0;j<n;j++)
            {
                if(s[i][j]=='1')
                  s1+=1;
                if(s[i][j]=='0')
                  s0+=1;
            }
            win[i]=s1;
            tot[i]=s1+s0;
            if(s0+s1==0)
             wp[i]=0;
            else
             wp[i]=(double)s1/(double)(s0+s1);
        }


        for (j = 0; j < n; j++)
		{
            c = 0, sum = 0;
			for (k = 0; k < n; k++)
			{
				if (j == k || s[k][j] == '.')
					continue;
				else
				{
					c++;
					if (s[k][j] == '1')
						sum += double(win[k] - 1) / double(tot[k] - 1);
					else
						sum += double(win[k]) / double(tot[k] - 1);

				}
			}
			owp[j] = sum / double(c);
		}

        for(i=0;i<n;i++)
        {
            oowp[i]=0;
            sum=0;
            for(j=0;j<n;j++)
            {
                if(s[i][j]!='.')
                   oowp[i]+=owp[j],sum+=1;
            }
            if(sum==0)
             oowp[i]=0;
            else
             oowp[i]=oowp[i]/(double)sum;
        }

        printf("Case #%d:\n",ca++);
        for(i=0;i<n;i++)
            printf("%.6f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
    return 0;
}
