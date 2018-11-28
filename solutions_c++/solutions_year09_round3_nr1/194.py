#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std ;

char str[70];
int flag[300];
int srt[50];
int arr[70];

int main()
{
    FILE *in=fopen("war.in","r");
    freopen("war.out","w",stdout);
    int c,c2;
    int tests;
    fscanf(in,"%d",&tests);
    for (int test=1;test<=tests;test++)
    {
        printf("Case #%d: ",test);
        fscanf(in,"%s",str);
        int n=strlen(str);
        memset(flag,-1,sizeof(flag));
        for (c=0;c<50;c++)srt[c]=c;
        swap(srt[0],srt[1]);
        int cnt=0;
        for (c=0;c<n;c++)
        {
            if (flag[str[c]]!=-1){arr[c]=flag[str[c]];continue;}
            arr[c]=srt[cnt];
            flag[str[c]]=srt[cnt];
            cnt++;
        }
        cnt=max(2,cnt);
        long long ret=0;
        long long k=1;
        for (c=n-1;c>=0;c--)
        {
            ret+=arr[c]*k;
            k*=cnt;
        }
        cout<<ret<<"\n";
    }
//    system("pause");
    return 0;
}
