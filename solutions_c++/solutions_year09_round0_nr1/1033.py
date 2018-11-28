#include<iostream>
using namespace std;
char dic[6000][1000],str[100000];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    
    int l,d,n;
    scanf("%d%d%d\n",&l,&d,&n);
    int i,j,k,m,ctr,F;
    
    for (i=0;i<d;i++)
    {
        gets(dic[i]);
    }
    for (i=0;i<n;i++)
    {
        gets(str);
        ctr=0;
        for (j=0;j<d;j++)
        {
            F=1;
            for (k=0,m=0;k<l && F==1;k++,m++)
            {
                F=0;
                //printf("Checking %c\n",dic[j][k]);
                if (str[m]=='(')
                {
                   m++;
                   while (str[m]!=')')
                   {
                        if (str[m]==dic[j][k])
                           F=1; 
                        m++;
                   }
                }
                else if (str[m]==dic[j][k])
                     F=1;
            }
            if (F==1)
               ctr++;
            //cout<<str<<"  "<<dic[j]<<"  "<<F<<"  "<<ctr<<endl;
        }
        printf("Case #%d: %d\n",i+1,ctr);
    }
}
