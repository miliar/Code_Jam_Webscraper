#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;
int main()
{
    char a[600];
    int n;
    int res[510][20];
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d\n",&n);
    for(int i = 0;i < n; i++)
    {
     cin.getline(a,600);
     for(int j = 0; j< 20; j++)
     {
             res[0][j] = 0;
     }
     if (a[0]=='w') res[0][0] = 1;
     for(int j = 1; j < strlen(a);j++)
     {             
            for(int k = 0; k < 20; k++)
            {
                    res[j][k] = res[j-1][k];
                    //printf("Char %d pos %d: %d\n",j,k,res[j][k]);
            }
            //"welcome to code jam"
             switch (a[j]) 
             {
             case 'w' :
                  res[j][0] = (res[j-1][0]+1)%10000;
                  
                   break;             
             case 'e' :
                  res[j][1] = (res[j-1][0]+res[j-1][1])%10000;
                  res[j][6] = (res[j-1][6]+res[j-1][5])%10000;
                  res[j][14] = (res[j-1][14]+res[j-1][13])%10000;
                   break;                                
             case 'l' :
                  res[j][2] = (res[j-1][2]+res[j-1][1])%10000;
                   break;            
             case 'c' :
                  res[j][3] = (res[j-1][3]+res[j-1][2])%10000;
                  res[j][11] = (res[j-1][11]+res[j-1][10])%10000;
                   break;            
             case 'o' :
                  res[j][4] = (res[j-1][4]+res[j-1][3])%10000;
                  res[j][9] = (res[j-1][9]+res[j-1][8])%10000;
                  res[j][12] = (res[j-1][12]+res[j-1][11])%10000;
                   break;            
             case 'm' :
                  res[j][5] = (res[j-1][5]+res[j-1][4])%10000;
                  res[j][18] = (res[j-1][18]+res[j-1][17])%10000;
                   break;            
             case ' ' :
                  res[j][7] = (res[j-1][6]+res[j-1][7])%10000;
                  res[j][10] = (res[j-1][10]+res[j-1][9])%10000;
                  res[j][15] = (res[j-1][15]+res[j-1][14])%10000;
                   break;            
             case 't' :
                  res[j][8] = (res[j-1][7]+res[j-1][8])%10000;
                   break;                               
             case 'd' :
                  res[j][13] = (res[j-1][13]+res[j-1][12])%10000;
                   break;         
             case 'j' :
                  res[j][16] = (res[j-1][15]+res[j-1][16])%10000;
                   break;                            
             case 'a' :
                  res[j][17] = (res[j-1][17]+res[j-1][16])%10000;
                   break;                            
             default : break;
             }
     }
    // printf("Length: %d\n",strlen(a));
     if ((res[strlen(a)-1][18]/10)==0) printf("Case #%d: 000%d\n",i+1,res[strlen(a)-1][18]);
     else if ((res[strlen(a)-1][18]/100)==0) printf("Case #%d: 00%d\n",i+1,res[strlen(a)-1][18]);
     else if ((res[strlen(a)-1][18]/1000)==0) printf("Case #%d: 0%d\n",i+1,res[strlen(a)-1][18]);
     else printf("Case #%d: %d\n",i+1,res[strlen(a)-1][18]);
    }
    return(0);
}
