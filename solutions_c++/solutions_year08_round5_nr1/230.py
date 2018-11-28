using namespace std;
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

struct line{ int lx1,lx2,ly1,ly2; };

int N,nn;
int x,y,T,i,j,cx,cy,L,lung,nrv,nrh;
int maxx,maxy,minx,miny;
line h[50000],v[50000];
char S[10000],d;

void citire()
{
        scanf("%d\n",&L);
                     maxx=maxy=0;
             minx=miny=3000;
             nrh=nrv=0;
             d='N';
        for (i=1; i<=L; ++i)
            {
             scanf("%s",&S);
             while (S[0]=='\n')
                   scanf("%s",&S);
             scanf("%d",&T); 
             
             lung = strlen(S);

             while (T)
                   {
                    --T;
                    for (j=0; j<lung; ++j)
                       {
                        if (S[j]=='F')
                           {
                            if (cy)
                               {
                                v[++nrv].lx1 = x;
                                v[nrv].lx2 = x;
                                v[nrv].ly1 = y;
                                v[nrv].ly2 = y+cy;
                               }
                            if (cx)
                               {
                                h[++nrh].lx1 = x;
                                h[nrh].lx2 = x+cx;
                                h[nrh].ly1 = h[nrh].ly2 = y;
                               }
  
                            x+=cx;
                            y+=cy;
                            
                           }
                        else if (S[j]=='L')
                             {
                              if (d=='N')
                                {
                                 d='E';
                                 cx=-1;
                                 cy=0;
                                }
                              else
                              if (d=='E')
                                {
                                 d='S';
                                 cx=0;
                                 cy=-1;
                                }
                              else
                              if (d=='S')
                                {
                                 d='V';
                                 cx=1;
                                 cy=0;
                                }
                              else
                              if (d=='V')
                                {
                                 d='N';
                                 cx=0;
                                 cy=1;
                                }
                             }
                          else if (S[j]=='R')
                               {
                              if (d=='S')
                                {
                                 d='E';
                                 cx=-1;
                                 cy=0;
                                }                                
                              else
                              if (d=='V')
                                {
                                 d='S';
                                 cx=0;
                                 cy=-1;
                                }
                              else
                              if (d=='N')
                                {
                                 d='V';
                                 cx=1;
                                 cy=0;
                                }
                              else
                              if (d=='E')
                                {
                                 d='N';
                                 cx=0;
                                 cy=1;
                                }
                               }
                    if (x>maxx) maxx=x;
                    if (y>maxy) maxy=y;
                    if (x<minx) minx=x;
                    if (y<miny) miny=y;
                    }
                   }
}
}

void pocket()
{
 int i,j,k,up,down,st,dr,nr;
 nr=0;
 for (i=minx-2;i<=maxx+2;++i)
     for (j=miny-2;j<=maxy+2;++j)
         {
          //consider patratul ( i,j , i+1,j+1 )
          up=down=st=dr=0;          
          //cate linii horizontale sunt
          for (k=1;k<=nrh;++k)
              if ( (h[k].lx1==i && h[k].lx2 == i+1) || (h[k].lx1==i+1 && h[k].lx2 == i) )
                 if (h[k].ly1 <=j) ++down;
                    else ++up;
          //cate linii verticale sunt
          for (k=1; k<=nrv; ++k)
              if ( (v[k].ly1 == j && v[k].ly2 == j+1) || (v[k].ly1 ==j+1 && v[k].ly2 ==j) )
                 if (v[k].lx1 <=i) ++st;
                    else ++dr;
          if ( (st>0 && dr>0 && (st%2==0) && (dr%2==0) ) || ( up>0 && down>0 && (up%2==0) && (down%2==0) ) ) ++nr;
         }
 printf("Case #%d: %d\n", nn, nr);    
}

int main()
{
 freopen("a.in","r",stdin);
 freopen("a.out","w",stdout);
 
 scanf("%d\n",&N);
 
 for (nn=1; nn<=N; ++nn)
     {
        x=y=3000;
        cx=0;
        cy=1;
        
        citire();    
        pocket();            
     }
 
 return 0;
}
