#include<iostream>
using namespace std;

int in[4];
int ans[10][3];
int ind[4]={0};
int m=0, p;

void special_1(int k, int res)
{
   int i, j=0;
   ans[m][0] = k;
   ans[m][2] = k+2;
   j = k + k + 2;
   for(i=0;i<=2;i++)
    {
       ans[m][1] = k + i;
       j += (k + i);
       if(j == res)
        break;
       else
        j -= (k + i);
    }
   m++;
}
void special_2(int k, int res)
{
     int i, flg=2, j=0, n=k;
while(n<=k+1)
{  
        ans[m][0] = n;
        ans[m][2] = n+2;
        if(n>=p || n+2 >=p)
         flg = 1;
        j = n + n + 2;
        for(i=0;i<=2;i++)
         {
             ans[m][1] = n+i;
             j = j + n+i;
             if(j == res && (flg == 1 || n+i >= p)) 
               break;
             else 
               j -= n+i;
         }
     if(j == res && (flg == 1 || n+i >= p)) 
       break;    
    n++;     
}
      m++;
}
void normal_2(int k, int res)
{
    int i, j=0, flg=2;
        ans[m][0] = k;
        ans[m][2] = k+1;
        if(k>=p || k+1 >=p)
         flg = 1;
        j = k + k + 1;
        for(i=0;i<=1;i++)
         {
             ans[m][1] = k+i;
             j = j + k+i;
             if(j == res && (flg == 1 || k+i >= p)) 
               break;
             else 
               j -= k+i;
         }
    m++;
}     
int main()
{
    int i, j=0, t, n, s, cse=0;
    int tmp, tmp1;
    int hl=0;
    int tmps, cs, ks, km=0, anss=0, jf, z, mn;
    
    scanf("%d", &t);
    while(t--)
    {
      scanf("%d %d %d", &n, &s, &p);
      for(i=0;i<n;i++)
       scanf("%d", &in[i]);
       
    for(i=0;i<n;i++)
     {
        if(in[i] % 3 == 0 && in[i] >= 3 && in[i] != 30)
         {
           tmp = (in[i]/3);
               ans[m][0] = tmp;
               ans[m][1] = tmp;
               ans[m][2] = tmp;
               m++;
               
           tmp = tmp - 1;
           special_1(tmp, in[i]);
         }
        else if(in[i] == 1)
        {
           ans[m][0] = 0;
           ans[m][1] = 0;
           ans[m][2] = 1;
           m++;
           ans[m][0] = -1;
           ans[m][1] = -1;
           ans[m][2] = -1;
           m++;
        }
        else if(in[i] == 0)
        {
           ans[m][0] = 0;
           ans[m][1] = 0;
           ans[m][2] = 0;
           m++;
           ans[m][0] = -1;
           ans[m][1] = -1;
           ans[m][2] = -1;
           m++;
        }
        else if(in[i] == 30)
        {
           ans[m][0] = 10;
           ans[m][1] = 10;
           ans[m][2] = 10;
           m++;
           ans[m][0] = -1;
           ans[m][1] = -1;
           ans[m][2] = -1;
           m++;
        }
        else if(in[i] == 29)
        {
           ans[m][0] = 9;
           ans[m][1] = 10;
           ans[m][2] = 10;
           m++;
           ans[m][0] = -1;
           ans[m][1] = -1;
           ans[m][2] = -1;
           m++;   
        }
        else if(in[i] == 2)
         {
           ans[m][0] = 0;
           ans[m][1] = 1;
           ans[m][2] = 1;
           m++;
           special_1(0, in[i]);
         }
        else if(in[i] % 3 != 0)
         {
            tmp = (in[i]/3);
               normal_2(tmp, in[i]);
               
           tmp = tmp - 1;
           special_2(tmp, in[i]);
         }
     } 
     for(i=0;i<(1<<3);i++)
      {
        tmps = i;
        cs = 0;
        jf = 0;
        km = 0;
        hl = 0;
        while(tmps > 0)
         {
             if(tmps&1)
              {
                 cs++;
                 ind[km] = jf;
                 km++;
              }
              tmps = tmps >> 1;
              jf++;
         }
         if(cs == s)
          {
            for(ks=0;ks<km;ks++)
             {
                if(ind[ks] == 0)
                 z = 1;
                else if(ind[ks] == 1)
                 z = 3;
                else if(ind[ks] == 2)
                 z = 5;
                if(z<m)
                {
                for(int k=0;k<3;k++)
                 {
                    if(ans[z][k] >= p)
                     {
                      j++;
                      hl = hl + z;
                      break;
                     }
                 }
              if(j==s)
               break;
               }
             }
            if(j < n && s < n)
             {
                for(mn=0;mn<m;mn+=2)
                {
                  if(hl == 1 && mn == 0)
                   continue;
                  else if(hl == 3 && mn == 2)
                   continue;
                  else if(hl == 5 && mn == 4)
                   continue;
                  else if(hl == 4 && (mn == 0 || mn == 2))
                   continue;
                  else if(hl == 8 && (mn == 2 || mn == 4))
                   continue;
                  else if(hl == 6 && (mn == 0 || mn == 4))
                   continue;
                
                for(int k=0;k<3;k++)
                 {
                    if(ans[mn][k] >= p)
                     {
                      j++;
                      break;
                     }
                 }
                }  
             }
          }
             if(j>anss)
              anss = j;
              j = 0;
              ind[0] = -1;
              ind[1] = -1;
              ind[2] = -1;
         if(anss==n)
          break;
      }                    
      cse++;
      printf("Case #%d: %d\n", cse, anss);
      m = 0;
      j = 0; 
      anss = 0;
    }
}
