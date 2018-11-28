// Furshing Tsai  fstsai@gmail.com
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <assert.h>

//Limits
//T < 100;
//Small dataset

//1 < H, W < 10;
//0 < altitudes < 10.
//There will be at most two basins. 

//Large dataset

//1 < H, W < 100;
//0 < altitudes < 10,000.
//There will be at most 26 basins.


#define DEBUG 1
int debug=0;
int  T,H,W,Gbid=1;
int  alt[100][100];
char basin[100][101];
char bid2basin[27];

int inside(int j,int k)
{ if (j<0 || j>=H) return 0;
  if (k<0 || k>=W) return 0;
  return 1;
}

int find_basin(int j,int k);
void get_basin_id(int j,int k,int eq,int &al,int &bid)
{ 
#if(DEBUG)
  if (debug) printf("get_basin_id(%d,%d,%d)\n",j,k,eq);
#endif
  if (inside(j,k)) {
    if (alt[j][k]<al ||(eq && alt[j][k]==al)) {
      al = alt[j][k]; 
      bid = find_basin(j,k);
    }
  }
}

int find_basin(int j,int k)
{ 
#if(DEBUG)
  if (debug) printf("find_basin(%d,%d)\n",j,k);
#endif
  if (basin[j][k]=='\0') { // not found before
    int al = alt[j][k], my_bid= -1;
    get_basin_id(j-1,k,0,al,my_bid); // North
    get_basin_id(j,k-1,0,al,my_bid); // West
    get_basin_id(j,k+1,0,al,my_bid); // East
    get_basin_id(j+1,k,0,al,my_bid); // South
    if (my_bid<0) // not found
      my_bid=Gbid++;
    basin[j][k]=my_bid;
  }
  return basin[j][k]; 
}

int main(int argc, char **argv)
{ int i,j,k;
  char *p,str[1024];
  if (argc<2) { printf("Usage %s file"); return(1); }
  FILE *fd=fopen(argv[1],"r");
  fscanf(fd,"%d",&T);
#if (DEBUG)
  if (argc>2) {
    debug=1;
    printf("T=%d\n",T);
  }
#endif
  for (i=0;i<T;i++) {
    fscanf(fd,"%d %d",&H,&W);
#if (DEBUG)
  if (argc>2)
    printf("A:%d H=%d W=%d\n",i,H,W);
#endif
 
    // READ input
    for (j=0;j<H;j++)
     for (k=0;k<W;k++) {
      fscanf(fd,"%d",&alt[j][k]);
      basin[j][k]='\0';
     }

    // find basin idx
    Gbid=1;
    for (j=0;j<H;j++)
     for (k=0;k<W;k++) 
       find_basin(j,k);

    // assign basin name
    char next_basin='a';
    for (j=1;j<Gbid;j++) bid2basin[j]='\0';
    for (j=0;j<H;j++)
     for (k=0;k<W;k++) {
       if (bid2basin[basin[j][k]]=='\0') {
         bid2basin[basin[j][k]] = next_basin;
         next_basin++;
       }
     }

    // print result
    printf("Case #%d:\n",i+1);
    for (j=0;j<H;j++) {
      for (k=0;k<W;k++) 
        printf("%c ",bid2basin[basin[j][k]]);
      printf("\n");
    }
  }
  return 0;
}
