#include<stdio.h>
char str1[53][53],str[53][53],str2[53];
int t[53];
int main()
{
    freopen("ina.txt","r",stdin);
    freopen("outa.txt","w",stdout);
    int test,cas,n,k,i,j,l,m,i1,j1,c1;
    char temp;
    bool d1,d2;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d%d",&n,&k);
        for (i=0;i<n;i++) scanf("%s",str[i]);
        for (j=0;j<n;j++)
        {
            for (i=n-1;i>=0;i--) str1[j][n-1-i]=str[i][j];
            str1[j][n]=0;
        }
        for (i=0;i<n;i++)
        {
            for (j=n-2;j>=0;j--)
            {
                if (str1[j][i]!='.')
                {
                    for (l=j+1;l<n&&str1[l][i]=='.';l++) ;
                    temp=str1[j][i];
                    str1[j][i]='.';
                    str1[l-1][i]=temp;
                }
            }
        }
        //for (i=0;i<n;i++) printf("%s\n",str1[i]);
        d1=d2=0;
        t[0]=-1;
        t[1]=0;
        for (l=2;l<k;l++) t[l]=t[l-1]+1;
        for (i=0;i<n;i++)
        {
            m=0;
            j=0;
            while (m+j<n)
            {
                if (str1[i][m+j]=='R')
                {
                    j++;
                    if (j==k) break;
                }
                else
                {
                    m=m+j-t[j];
                    if (t[j]>-1) j=t[j];
                    else j=0;
                }
            }
            if (j==k)
            {
                d1=1;
                break;
            }
        }
        for (j=0;j<n;j++)
        {
            m=0;
            i=0;
            while (m+i<n)
            {
                if (str1[m+i][j]=='R')
                {
                    i++;
                    if (i==k) break;
                }
                else
                {
                    m=m+i-t[i];
                    if (t[i]>-1) i=t[i];
                    else i=0;
                }
            }
            if (i==k)
            {
                d1=1;
                break;
            }
        }
        for (i=0;i<n;i++)
        {
            i1=i;
            c1=0;
            for (j=0;i1>=0&&j<n;i1--,j++) str2[c1++]=str1[i1][j];
            m=j=0;
            while (m+j<c1)
            {
                if (str2[m+j]=='R')
                {
                    j++;
                    if (j==k) break;
                }
                else
                {
                    m=m+j-t[j];
                    if (t[j]>-1) j=t[j];
                    else j=0;
                }
            }
            if (j==k)
            {
                d1=1;
                break;
            }
            i1=i;
            c1=0;
            for (j=0;i1<n&&j<n;i1++,j++) str2[c1++]=str1[i1][j];
            m=j=0;
            while (m+j<c1)
            {
                if (str2[m+j]=='R')
                {
                    j++;
                    if (j==k) break;
                }
                else
                {
                    m=m+j-t[j];
                    if (t[j]>-1) j=t[j];
                    else j=0;
                }
            }
            if (j==k)
            {
                d1=1;
                break;
            }
        }
        for (j=0;j<n;j++)
        {
            j1=j;
            c1=0;
            for (i=n-1;i>=0&&j1<n;i--,j1++) str2[c1++]=str1[i][j1];
            m=i=0;
            while (m+i<c1)
            {
                if (str2[m+i]=='R')
                {
                    i++;
                    if (i==k) break;
                }
                else
                {
                    m=m+i-t[i];
                    if (t[i]>-1) i=t[i];
                    else i=0;
                }
            }
            if (i==k)
            {
                d1=1;
                break;
            }
            j1=j;
            c1=0;
            for (i=0;i<n&&j1<n;i++,j1++) str2[c1++]=str1[i][j1];
            m=i=0;
            while (m+i<c1)
            {
                if (str2[m+i]=='R')
                {
                    i++;
                    if (i==k) break;
                }
                else
                {
                    m=m+i-t[i];
                    if (t[i]>-1) i=t[i];
                    else i=0;
                }
            }
            if (i==k)
            {
                d1=1;
                break;
            }
        }

        for (i=0;i<n;i++)
        {
            m=0;
            j=0;
            while (m+j<n)
            {
                if (str1[i][m+j]=='B')
                {
                    j++;
                    if (j==k) break;
                }
                else
                {
                    m=m+j-t[j];
                    if (t[j]>-1) j=t[j];
                    else j=0;
                }
            }
            if (j==k)
            {
                d2=1;
                break;
            }
        }
        for (j=0;j<n;j++)
        {
            m=0;
            i=0;
            while (m+i<n)
            {
                if (str1[m+i][j]=='B')
                {
                    i++;
                    if (i==k) break;
                }
                else
                {
                    m=m+i-t[i];
                    if (t[i]>-1) i=t[i];
                    else i=0;
                }
            }
            if (i==k)
            {
                d2=1;
                break;
            }
        }
        for (i=0;i<n;i++)
        {
            i1=i;
            c1=0;
            for (j=0;i1>=0&&j<n;i1--,j++) str2[c1++]=str1[i1][j];
            m=j=0;
            while (m+j<c1)
            {
                if (str2[m+j]=='B')
                {
                    j++;
                    if (j==k) break;
                }
                else
                {
                    m=m+j-t[j];
                    if (t[j]>-1) j=t[j];
                    else j=0;
                }
            }
            if (j==k)
            {
                d2=1;
                break;
            }
            i1=i;
            c1=0;
            for (j=0;i1<n&&j<n;i1++,j++) str2[c1++]=str1[i1][j];
            m=j=0;
            while (m+j<c1)
            {
                if (str2[m+j]=='B')
                {
                    j++;
                    if (j==k) break;
                }
                else
                {
                    m=m+j-t[j];
                    if (t[j]>-1) j=t[j];
                    else j=0;
                }
            }
            if (j==k)
            {
                d2=1;
                break;
            }
        }
        for (j=0;j<n;j++)
        {
            j1=j;
            c1=0;
            for (i=n-1;i>=0&&j1<n;i--,j1++) str2[c1++]=str1[i][j1];
            m=i=0;
            while (m+i<c1)
            {
                if (str2[m+i]=='B')
                {
                    i++;
                    if (i==k) break;
                }
                else
                {
                    m=m+i-t[i];
                    if (t[i]>-1) i=t[i];
                    else i=0;
                }
            }
            if (i==k)
            {
                d2=1;
                break;
            }
            j1=j;
            c1=0;
            for (i=0;i<n&&j1<n;i++,j1++) str2[c1++]=str1[i][j1];
            m=i=0;
            while (m+i<c1)
            {
                if (str2[m+i]=='B')
                {
                    i++;
                    if (i==k) break;
                }
                else
                {
                    m=m+i-t[i];
                    if (t[i]>-1) i=t[i];
                    else i=0;
                }
            }
            if (i==k)
            {
                d2=1;
                break;
            }
        }
        if (d1&&d2) printf("Case #%d: Both\n",cas);
        else if (d1) printf("Case #%d: Red\n",cas);
        else if (d2) printf("Case #%d: Blue\n",cas);
        else printf("Case #%d: Neither\n",cas);
    }
    return 0;
}
