#include<stdio.h>



char eng[100][100],vkeng[100];
char que[1000][100],vkque[1000];

int min(int a, int b) {
  if (a<b) {
    return a;
  } else {
    return b;
  }
}


bool isequal(int a, int b) {
  // a represents engine name
  // b represents queue name
  int i;
  bool vrati=true;
  if (vkeng[a]==vkque[b]) {
    
    for (i=0;i<vkeng[a];i++) {
      if (eng[a][i]!=que[b][i]) {
        vrati=false;
        break;
      }
    }
    
    return vrati;
  } else {
    return false;
  }
}  

int main() {
  // the number of test cases
  int total;
  int i,j,k,m,n,p,S,Q,mom;
  char c;
  // the dynamic programming solution
  // for every query, every search engine word as last
  int rez[1000][100];
  
  FILE *f,*fo;
  f=fopen("input.txt","r+");
  fo=fopen("output.txt","w+");
  
  fscanf(f,"%d",&total);
  
  for (k=0;k<total;k++) {
      
      printf("tuka sum %d",k+1);
      
    // 2 reading parts
    fscanf(f,"%d",&S);
    fscanf(f,"%c",&c);
    
    for (i=0;i<S;i++) {
      vkeng[i]=0;
      do {
        fscanf(f,"%c",&c);
        
        if (c!='\n') {
          eng[i][vkeng[i]]=c;
          vkeng[i]++;
        }
      } while (c!='\n');    
    
    
    }
    
    fscanf(f,"%d",&Q);
    fscanf(f,"%c",&c);
    
    for (i=0;i<Q;i++) {
      vkque[i]=0;
      do {
        fscanf(f,"%c",&c);
        if (c!='\n') {
          que[i][vkque[i]]=c;
          vkque[i]++;
        }
      } while (c!='\n');
    }
    
    // the main part
    
    // default parameters
    for (m=0;m<S;m++) {
      if (isequal(m,0)==true) {
        rez[0][m]=5000;  
      } else {
        rez[0][m]=0;
      }
    }
    
    // for every query name
    for (j=1;j<Q;j++) {
      
      // checks for every search engine
      for (m=0;m<S;m++) {
        if (isequal(m,j)==true) {
          rez[j][m]=5000;
        }  else {
          // find min of the previous result about this search word
          // and the rez+1 of
          // the other engines' previouses
          mom=rez[j-1][m];
          
          for (p=0;p<S;p++) {
            if (p!=m) {
              mom=min(mom,rez[j-1][p]+1);
            }  
          }
          rez[j][m]=mom;
        }
      
      } 
    }
    
    // find the min result and print it
    mom=5555;
    for (m=0;m<S;m++) {
      mom=min(mom,rez[Q-1][m]);
    }
    fprintf(fo,"Case #%d: %d\n",k+1,mom);
      
  }
  
  
  
  fclose(f);
  fclose(fo);
  
  scanf("%d",&i);
  
  return 0;
}
