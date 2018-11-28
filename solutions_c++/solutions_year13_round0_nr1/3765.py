#include <iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;


char s[100][100];
int temp[10][10];
int main()
{
    FILE *f = fopen("A-large.in","r");
    FILE *w = fopen("outA.txt","w");
    int n;
    fscanf(f,"%d",&n);
    //fprintf(w,"%d\n",n);
    int z = 0;
    //fgetchar();
    while(n--)
    {

        memset(temp,0,sizeof(temp));
        int res=-1000;
        for(int i=0;i<4;i++){fscanf(f,"%s",s[i]);printf("%s",s[i]);}
        if(strcmp(s[0],"") == 0){n++;continue;}
        int counte = 0;
        bool gg = false;
        for(int i=0;i<4;i++)
        {
            counte = 0;
            for(int j=0;j<4;j++)
            {
                if(s[i][j] == 'X' || s[i][j] == 'T')
                {
                    counte ++;
                }

                if(s[i][j] == '.')gg = true;
            }
            if(counte == 4)res = -1;
            counte = 0;
            for(int j=0;j<4;j++)
            {
                if(s[i][j] == 'O' || s[i][j] == 'T')
                {
                    counte ++;
                }
            }
            if(counte == 4)res = 1;
        }

        printf("%dres1\n",res);

        for(int j=0;j<4;j++)
        {
            counte = 0;
           for(int i=0;i<4;i++)
            {
                if(s[i][j] == 'X' || s[i][j] == 'T')
                {
                    counte ++;
                }
            }
            if(counte == 4){printf("%dii<<<\n",j);res = -1;}
            counte = 0;
            for(int i=0;i<4;i++)
            {
                if(s[i][j] == 'O' || s[i][j] == 'T')
                {
                    counte ++;
                }
            }
            if(counte == 4)res = 1;
        }
        printf("%dres2<<\n",res);

        counte = 0;
        for(int j=0;j<4;j++)
        {
            if(s[j][j] == 'X' || s[j][j] == 'T')counte ++;
        }
        if(counte == 4)res = -1;
        printf("%dres3\n",res);


        counte = 0;
        for(int j=0;j<4;j++)
        {
            if(s[j][j] == 'O' || s[j][j] == 'T')counte ++;
        }
        if(counte == 4)res = 1;
        printf("%dres4\n",res);

        counte = 0;
        for(int j=3;j>=0;j--)
        {
            if(s[3-j][j] == 'X' || s[3-j][j] == 'T')counte ++;
        }
        if(counte == 4)res = -1;
        printf("%dres5\n",res);

        counte = 0;
        for(int j=3;j>=0;j--)
        {
            if(s[3-j][j] == 'O' || s[3-j][j] == 'T')counte ++;
        }
        if(counte == 4)res = 1;
        printf("%dres6\n",res);

        if(res == -1000 && gg )fprintf(w,"Case #%d: Game has not completed\n",++z);
        else if(res == -1000 )fprintf(w,"Case #%d: Draw\n",++z);
        else if(res == -1)fprintf(w,"Case #%d: X won\n",++z);
        else if(res == 1)fprintf(w,"Case #%d: O won\n",++z);

    }
    //getchar();
    return 0;
}
