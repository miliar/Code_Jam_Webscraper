#include<iostream>
#include<cstdio>
using namespace std;
char combination[8][8];
char opposition[8][8];
char elementlist[200];
char resultlist[200];
inline int hashpair(char x)
{
    switch(x)
    {
        case 'Q':
        return 0;
        case 'W':
        return 1;
        case 'E':
        return 2;
        case 'R':
        return 3;
        case 'A':
        return 4;
        case 'S':
        return 5;
        case 'D':
        return 6;
        case 'F':
        return 7;
    }
    return -1;
}
void pre()
{
     int C,D,i, j;
     char cmb[10];
     char opp[10];
     for (i = 0; i< 8; i++)
        for (j = 0; j < 8; j++)
        {
           combination[i][j] = '.'; 
           opposition[i][j]= '.';
        }
     scanf ("%d", &C);
     for (i=0; i<C; i++)
     {
         scanf ("%s", cmb);
         combination[hashpair(cmb[0])][hashpair(cmb[1])] =cmb[2];
         combination[hashpair(cmb[1])][hashpair(cmb[0])] =cmb[2];
     }
     scanf ("%d", &D);
     for (i = 0; i < D; i++)
     {
         scanf ("%s", opp);
         opposition[hashpair(opp[0])][hashpair(opp[1])] ='*';
         opposition[hashpair(opp[1])][hashpair(opp[0])] ='*';
        
     }   
}
void cal(int test)
{
     int N,i,j,cnt;
     int x, y;
     scanf ("%d", &N);
     scanf ("%s", elementlist);
     cnt = 0;
     for (i = 0; i < N; i++)
     {
		 if (cnt == 0)
		 {
			 resultlist[cnt++] = elementlist[i];
			 continue;
		 }
         x = hashpair(elementlist[i]);
         y = hashpair(resultlist[cnt-1]);
         if (y!=-1 && combination[x][y] != '.')
         {
             resultlist[cnt-1] = combination[x][y];
             continue;
         }
         resultlist[cnt++] = elementlist[i];
         for (j = 0; j <cnt-1; j++)
         {
             x = hashpair(resultlist[cnt-1]);
             y = hashpair(resultlist[j]);
             if (y != -1 && opposition[x][y] == '*')
             {
                 cnt = 0;
                 break;
             }
         }
     }
     if (cnt == 0)
     {
         printf ("Case #%d: []\n", test);
     }
     else{
          printf ("Case #%d: [", test);
          for (i = 0 ;i < cnt-1; i++)
          {
              printf ("%c, ", resultlist[i]);
          }
          printf ("%c]\n",resultlist[cnt-1]);
   
     }
     
}




int main()
{
   int T,i;
 // freopen("B-large.in", "r", stdin);
 // freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (i = 1; i<= T; i++)
    {
        pre(); 
        cal(i);
    }
   // system("pause");
    return 0;
}
