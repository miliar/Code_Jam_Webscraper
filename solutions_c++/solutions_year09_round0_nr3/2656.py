#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

    char data[505];
    int n;
    scanf("%d",&n);
    while(getchar()!='\n');
    for(int i=1;i<=n;i++)
    {
        int s[20]={0};
        s[0]=1;

        gets(data);
        int len=strlen(data);
        for(int j=0;j<len;j++)
        {
            if(data[j]=='e')
            {
               s[15]+=s[14];
               s[7]+=s[6];
               s[2]+=s[1];
            }
            else if(data[j]=='c')
            {
                s[12]+=s[11];
                s[4]+=s[3];
            }
            else if(data[j]=='o')
            {
                s[13]+=s[12];
                s[10]+=s[9];
                s[5]+=s[4];
            }
            else if(data[j]=='m')
            {
                s[19]+=s[18];
                s[6]+=s[5];
            }
            else if(data[j]==' ')
            {
                s[16]+=s[15];
                s[11]+=s[10];
                s[8]+=s[7];
            }
            else if(data[j]=='w')
                s[1]+=s[0];
            else if(data[j]=='l')
                s[3]+=s[2];
            else if(data[j]=='t')
                s[9]+=s[8];
            else if(data[j]=='d')
                s[14]+=s[13];
            else if(data[j]=='j')
                s[17]+=s[16];
            else if(data[j]=='a')
                s[18]+=s[17];
			for(int k=0;k<20;k++)
			{
				if(s[k]>9999)
					s[k]%=10000;
			}
        }
        printf("Case #%d: %04d",i,s[19]%10000);
        printf("\n");
    }

    return 0;
}
