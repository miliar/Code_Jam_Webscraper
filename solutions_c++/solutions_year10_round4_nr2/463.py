#include <cstdio>

#define MAX_P      11
#define MAX_TEAMS  1024

int p;
int t;
int m[MAX_TEAMS];
int price[MAX_P][MAX_TEAMS];

int min_miss[MAX_P][MAX_TEAMS];
int C[MAX_P][MAX_P][MAX_TEAMS];
int infinity;

void read_input()
{
  scanf("%d",&p);
  t = (1 << p);
  for(int i=0; i<t; i++)
    scanf("%d",&m[i]);
  int tt = t / 2;
  int ro = 0;
  infinity = 0;
  while(tt!=0) {
    for(int i=0; i<tt; i++) {
      scanf("%d",&price[ro][i]);
      infinity += price[ro][i];
    }
    ro++;
    tt /= 2;
  }
  infinity += 1;
}

void cal_min_miss()
{
  int rnum = p - 1;
  int tlen = t;
  for(int ro=0; ro<p; ro++) {
    int gr = t/tlen;
    for(int j=0; j<gr; j++) {
      int mm = p + 1;
      for(int i=0; i<tlen; i++)
	if(m[j*tlen + i]<mm)
	  mm = m[j*tlen + i];
      min_miss[rnum][j] = mm;
      //printf("%d ",mm);
    }
    //printf("\n");
    tlen /= 2;
    rnum--;
  }
}

int min(int a, int b)
{
  if(a<b)
    return a;
  else
    return b;
}

void process()
{
  int tt = t / 2;

  // first round
  for(int i = 0; i<tt; i++) {
    for(int mm = 0; mm <p; mm++) {
      int x = min(m[i*2], m[i*2+1]);
      if(mm==x)
	C[mm][0][i] = price[0][i];
      else if(mm > x)
	C[mm][0][i] = infinity;
      else
	C[mm][0][i] = 0;
    }
  }

  // later round
  for(int r=1; r < p; r++) {
    tt /= 2;  // tt nodes
    for(int i=0; i<tt; i++) {
      int cs = 0;
      for(int mm = 0; mm <= p; mm++) {
	// calculating C[mm][r][i]
	
	int left = i*2;
	int right = i*2+1;

	if(mm>min_miss[r][i]) {
	  C[mm][r][i] = infinity;
	  cs = 1;
	}
	else if(mm==min_miss[r][i]) {
	  // can't miss any more
	  C[mm][r][i] = price[r][i] + 
	    C[mm][r-1][left] + 
	    C[mm][r-1][right];
	  cs = 2;
	} else {
	  int c1 = price[r][i] + 
	    C[mm][r-1][left] + 
	    C[mm][r-1][right];   // buy it
	  int c2 = C[mm+1][r-1][left] + C[mm+1][r-1][right];
	  
	  C[mm][r][i] = min(c1,c2);
	  cs = 3;
	}

	//printf("[%d]%d(%d) ",min_miss[r][i],C[mm][r][i],cs);
      }
      //printf("\n");
    }
  }
}

int find_sol()
{
  int mi = infinity;
  for(int mm=0; mm <= p; mm++)
    if(C[mm][p-1][0] < mi)
      mi = C[mm][p-1][0];

  if(mi==infinity)
    fprintf(stderr,"ERRORR!!!!\n");
  return mi;
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++) {
    read_input();
    cal_min_miss();
    process();
    printf("Case #%d: %d\n",tt+1,find_sol());
  }
}
