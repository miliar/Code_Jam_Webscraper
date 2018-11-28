#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
#include<stack>

using namespace std;

char arr[52][52];

bool iseq(char s1[2][2], char s2[2][2])
{
    for(int i = 0; i<2; i++)
    {
        for(int j = 0; j<2; j++)
        {
            if(s1[i][j] != s2[i][j])
                return false;
        }
    }
    
    return true;
}

int main(void){
    int T;
    
    freopen("A-large.in", "r",stdin);
    freopen("A-large.out", "w",stdout);
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int r,c;
        scanf("%d%d",&r,&c);
        
        for(int i = 0; i<r; i++)
        {
            scanf("%s",arr[i]);
        }
        
        char b = '#', w = '.';
        
        char red[2][2];
        red[0][0] = '/';
        red[0][1] = '\\';
        red[1][0] = '\\';
        red[1][1] = '/';
        char blue[2][2];
        blue[0][0] = b;
        blue[0][1] = b;
        blue[1][0] = b;
        blue[1][1] = b;
        
        for(int i = 0; i<r-1; i++)
        {
            for(int j = 0; j<c-1; j++)
            {
                char tmp[2][2];
                int x = 0,y = 0;
                for(int k = i; k<i+2; k++)
                {
                    y = 0;
                    for(int l = j; l<j+2; l++)
                    {
                        tmp[x][y++] = arr[k][l];
                    }
                    x++;
                }
                
                if(iseq(tmp,blue))
                {
                    //puts("**");
                    x = 0,y = 0;
                    for(int k = i; k<i+2; k++)
                    {
                        y = 0;
                        for(int l = j; l<j+2; l++)
                        {
                            arr[k][l] = red[x][y++];
                        }
                        x++;
                    }      
                }
            }
        }
        
        int bc = 0;
        for(int i = 0; i<r; i++)
        {
            for(int j = 0; j<c; j++)
            {
                if(arr[i][j] == b)
                {
                    bc++;
                    break;
                }
            }
            if(bc)
            {
                break;
            }
        }
        
        printf("Case #%d:\n",t+1);
        if(bc)
        puts("Impossible");
        else
        {
            for(int i = 0; i<r; i++)
            {
                puts(arr[i]);
            }
        }  
    }
    return 0;
}
