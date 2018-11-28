#include <cstdio>
#include <cstring>

#define Nmax 256

struct cursa { int start, end, where, ok; };

int T,t,i,j,time;
int NA,NB,N;
int m1,m2,s1,s2,c;
cursa C[Nmax];

void qsort(int st,int dr)
{
 int i=st,j=dr;
 cursa m,aux;
 m = C[(st+dr)>>1];
 
 while (i<=j)
       {
        while (C[i].start < m.start) ++i;
        while (C[j].start > m.start) --j;
        if (i<=j)
           {
            aux = C[i];
            C[i] = C[j];
            C[j] = aux;
            ++i;
            --j;
           }
       }
 if (i<dr) qsort(i,dr);
 if (st<j) qsort(st,j);       
}

void solve()
{
 int i,j,p,curent;
 
 qsort(1,N);

 NA=NB=0;

 for (i=1; i<=N; ++i)
     if (C[i].ok == 0)
        {      
         if (C[i].where == 1) ++NA;
            else ++NB;                
        
         j=i;    
         while (j<=N)
               {
                //bifeaza ca vizitat
                C[j].ok = 1;
                //verifica directia
                curent = C[j].where;
                //fixeaza timpul
                p = C[j].end + time;
                //cauta o cursa                  
                while (j<=N && (C[j].start<p || C[j].ok==1 || C[j].where==curent) ) ++j;                                
               }
        }
 printf("Case #%d: %d %d\n",t,NA,NB);
}

int main()
{
 freopen("b.in","r",stdin);
 freopen("b.out","w",stdout);
 
 scanf("%d\n",&T);
 
 for (t=1; t<=T; ++t)
     {
      scanf("%d\n",&time);
      scanf("%d %d\n",&NA,&NB);
      N = NA+NB;
      
      for (i=1; i<=NA; ++i)
          {
           scanf("%c%c%c%c%c",&m1,&m2,&c,&s1,&s2);
           C[i].start = ( m1*10 + m2 ) * 60 + s1*10 + s2;

           do
              scanf("%c",&m1);
           while (m1 == ' ');
           scanf("%c%c%c%c\n",&m2,&c,&s1,&s2);
           C[i].end = ( m1*10 + m2 ) * 60 + s1*10 + s2;
           
           C[i].where = 1;
           C[i].ok = 0;
          }

      for (i=NA+1; i<=NA+NB; ++i)
          {
           scanf("%c%c%c%c%c",&m1,&m2,&c,&s1,&s2);
           C[i].start = ( m1*10 + m2 ) * 60 + s1*10 + s2;

           do
              scanf("%c",&m1);
           while (m1 == ' ');
           scanf("%c%c%c%c\n",&m2,&c,&s1,&s2);
           C[i].end = ( m1*10 + m2 ) * 60 + s1*10 + s2;
           
           C[i].where = 2;
           C[i].ok = 0;
          }

      solve();

     }
 fclose(stdout); 
 return 0;
}
