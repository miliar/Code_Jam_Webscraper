#include<stdio.h>
#include<iostream.h>
#include<string.h>


FILE *fin, *fout;

int D,L,N, H, W;

int tc[100][100];


int res[100][100];
char alph[] = "abcdefghijklmnopqrstuvwxyz";
int i;
int l,m,n,p,q,r,s,t,nextval,v;
int foun, f;

void init_res();
int findNbr(int r, int c, int *ro, int *co, int *val);
void update_val(int val);
void print_res();

main(int argc, char *argv[])
{
   int j,k;
   fin = fopen(argv[1], "r");
   fout = fopen(argv[2], "w");

   fscanf(fin,"%d\n",&N);
   
   //printf("\ntest case - %d\n",N); 
   
   
   for(i=1; i<=N;i++)
   {
      fscanf(fin,"%d %d\n",&H, &W);
      //printf("%d %d\n",H, W);
      
      nextval = 0;

      for(j=0;j<H;++j)
      {
        for(k=0;k<W;++k)
        {
           fscanf(fin,"%d",&n);
           tc[j][k] = n;
        }
      }

      init_res();

      printf("\n");
      for(j=0;j<H;++j)
      {
        for(k=0;k<W;++k)
        {
//printf("\nout res[%d]%d]=%d\n",j,k,res[j][k]);
          if(res[j][k] == -1)
          {
             s = j;
             t = k;
             while(1)
             {
                p = findNbr(s,t, &l, &m, &v);
                if(p == 1)
                {
                  s = l;
                  t = m;
                }
                else
                {
                  //printf("\nupdate val = %d, j=%d, k=%d\n", v,j,k);
		  update_val(v);
                  break;
                }
                
             }
          }  
        }
      }
     
      
     printf("Case #%d:\n",i);
     fprintf(fout,"Case #%d:\n",i);
     print_res();
   }
}

int findNbr(int r, int c, int *ro, int *co, int *val)
{
  int er, ec, wr, wc, nr, nc, sr, sc;
  int ev =10001,wv=10001,nv=10001,sv=10001;
  int tr,tcc,tv;
  int ttr,ttc,ttv;
  
//printf("\n--res out [r=%d][c=%d] = %d\n",r,c,res[r][c]);
  if(c < W-1)
  {
    er = r;
    ec = c + 1;
    ev = tc[er][ec];
  }
  if(c > 0)
  {
    wr = r;
    wc = c -1;
    wv = tc[wr][wc];
  }
  if(r > 0 ) //< H -1)
  {
    nr = r -1;
    nc = c;
    nv = tc[nr][nc];
  }
  if(r < H -1 ) //> 0 )
  {
    sr = r + 1;
    sc = c;
    sv = tc[sr][sc];
  }
printf("\nev=%d, wv=%d, nv=%d, sv=%d, tc=%d\n",ev,wv,nv,sv,tc[r][c]);
  if(res[r][c] == -1)
  {
    res[r][c] = -2;
  }
  if( (tc[r][c] <= ev) && (tc[r][c] <= wv) && (tc[r][c] <= nv) && (tc[r][c] <= sv) )
  {
    // found sink
    if(res[r][c] == -2)
    {
//printf("\nres[r=%d][c=%d] = %d\n",r,c,res[r][c]);
      res[r][c] = nextval;
      *val = nextval;
      nextval++;
    }
    else
    {
      *val = res[r][c];
    }
    return(0);
  }
  
  if(nv <= wv)
  {
    tr = nr;
    tcc = nc;
    tv = nv;
  }
  else
  {
    tr = wr;
    tcc = wc;
    tv = wv;
  }

  if(ev <= sv)
  {
    ttr = er;
    ttc = ec;
    ttv = ev;
  }
  else
  {
    ttr = sr;
    ttc = sc;
    ttv = sv;
  }

if(ev == 8 && sv == 8 && nv == 8)
{
  printf("\ntv =%d, ttv=%d, tr=%d, tcc=%d,ttr=%d, ttc=%d\n",tv,ttv,tr,tcc,ttr,ttc);
  printf("\nnr=%d, nc=%d, wr=%d, wc=%d, er=%d, ec=%d, sr=%d, sc=%d\n",nr,nc,wr,wc,er,ec,sr,sc);
}
  if(tv <= ttv)
  {
    *ro = tr;
    *co = tcc;
  }
  else
  {
    *ro = ttr;
    *co = ttc;
  }
  
  //res[r][c] = -2;
  if(ev == 8 && sv == 8 && nv == 8)
  printf("\nr=%d, c=%d, res[][]=%d\n",*ro,*co,res[*ro][*co]);  

  if(res[*ro][*co] == -1)
  {
    res[*ro][*co] = -2;
    *val = -2;
    return(1);
  }
  else
  {
    *val = res[*ro][*co];
    return(0);
  }
}


void init_res()
{
  int j,k;
  for(j=0;j<H;++j)
      {
        for(k=0;k<W;++k)
        {
          res[j][k] = -1;
        }
      }
}

void update_val(int val)
{
  int j,k;
  for(j=0;j<H;++j)
  {
    for(k=0;k<W;++k)
    {
       if(res[j][k] == -2)
       {  
         res[j][k] = val;
       }
     }
   }
}

void print_res()
{
  int j,k;
  for(j=0;j<H;++j)
  {
    for(k=0;k<W;++k)
    {
       if(res[j][k] >= 0)
       {  
         printf("%c ",alph[res[j][k]]);
         fprintf(fout,"%c ",alph[res[j][k]]);
       }
     }
     printf("\n");
     fprintf(fout,"\n");
   }
    fprintf(fout,"\n");
}
