#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

char mas[32];
int num[10];

int main()
{
    int t;
    int f;
    scanf("%d",&t);
    char tmp;
    int ind;
    for(int i=1;i<=t;i++)
    {
        memset(mas,0,sizeof(mas));
        scanf("%s",mas);
        int len=strlen(mas);
        f=1;
        for(int j=len-2;j>=0;j--)
        {
            ind=-1;
            for(int k=j+1;k<len;k++)
            {
                if(mas[k]>mas[j])
                {
                    if(ind==-1) ind=k;
                    else
                    {
                        if(mas[ind]>mas[k]) ind=k;
                    }
                }
            }
            if(ind!=-1)
            {
                tmp=mas[j];
                mas[j]=mas[ind];
                mas[ind]=tmp;
                sort(mas+j+1, mas+len);
                printf("Case #%d: %s\n",i,mas);
                f=0;
                break;
            }
        }
        if(f)
        {
            int d;
            sort(mas,mas+len);
            for(int j=len;j>0;j--)
            {
                mas[j]=mas[j-1];
            }
            mas[1]='0';
            if(mas[0]=='0')
            {
                len=strlen(mas);
                ind=-1;
                for(int k=1;k<len;k++)
                {
                    if(mas[k]>mas[0])
                    {
                        if(ind==-1) ind=k;
                        else
                        {
                            if(mas[ind]>mas[k]) ind=k;
                        }
                    }
                }
                tmp=mas[ind];mas[ind]=mas[0];mas[0]=tmp;
                sort(mas+1,mas+len);
            }
            printf("Case #%d: %s\n",i,mas);
        }
    }
}
