
#include <stdio.h>

#include <map>

using namespace std;

int setsize[110][110];
int alt[110][110];
int basin[110][110];
int name[110][110];

int T, H, W;

int num(int h,int w) {

  return h + w* H;
}

int find(int ah,int aw) {
  
  int b = basin[ah][aw];
  
  if (b != num(ah,aw)) {
        
    basin[ah][aw] = find(b % H, b / H);
    
  }

  return basin[ah][aw];
}

    
void unite(int ah, int aw, int bh, int bw) {
    
  int a = basin[ah][aw] = find(ah,aw);
  int b = basin[bh][bw] = find(bh,bw);

  

  if (a != b) {
    // join basins

    ah = a % H;
    aw = a / H;

    bh = b % H;
    bw = b / H;

    
    int nname = a;
    if (b < a)
      nname = b;
    
    if (setsize[ah][aw] < setsize[bh][bw]) {
      // a points to b      
      setsize[bh][bw] += setsize[ah][aw];
      basin[ah][aw] = b;
      name[ah][aw] = nname;
    }
    else {
      setsize[ah][aw] += setsize[bh][bw];
      basin[bh][bw] = a;
      name[ah][aw] = nname;
    }
  }

}


main() {
  



  scanf("%d",&T);

  for (int t = 1; t <= T; t++) {
    
    printf("Case #%d:\n",t);


    scanf("%d %d",&H,&W);

    for (int h = 0; h < H; h++) {
      
      for (int w = 0; w < W; w++) {

	scanf("%d",&alt[h][w]);
      }

    }

    for (int h = 0; h < H; h++) {      
      for (int w = 0; w < W; w++) {
	basin[h][w] = num(h,w);
	name[h][w] = num(h,w);
	setsize[h][w] = 1;
      }
    }

    for (int h = 0; h < H; h++) {      
      for (int w = 0; w < W; w++) {
	// check heights, to figure out unites;
	
	int minalt = alt[h][w];
	int minh = h;
	int minw = w;
	// N
	if (h > 0) {
	  if (alt[h-1][w] < minalt) {
	    minalt = alt[h-1][w];
	    minh = h-1;
	    minw = w;
	  }
	}
	// W

	if (w > 0) {
	  if (alt[h][w-1] < minalt) {
	    minalt = alt[h][w-1];
	    minh = h;
	    minw = w-1;
	  }
	}

	// E
	if (w < W-1) {
	  if (alt[h][w+1] < minalt) {
	    minalt = alt[h][w+1];
	    minh = h;
	    minw = w+1;
	  }
	}

	// S
	if (h < H-1) {
	  if (alt[h+1][w] < minalt) {
	    minalt = alt[h+1][w];
	    minh = h+1;
	    minw = w;
	  }
	}
	
	if (minalt < alt[h][w]) {
	  unite(h,w,minh,minw);
	}


      }
    }
    
    char nextLabel = 'a';
    map<int,char> labels;
    
    for (int h = 0; h < H; h++) {      
      for (int w = 0; w < W; w++) {
	
	int b = find(basin[h][w]%H,basin[h][w]/H);
	
	b = name[b%H][b/H];

	if (labels.find(b) == labels.end()) {
	  labels[b] = nextLabel;
	  nextLabel++;
	}
	
	printf("%c",labels[b]);
	if (w != W-1)
	  printf(" ");
      }
      printf("\n");
    }
    
    
  }

  
  

}


