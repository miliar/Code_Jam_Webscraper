#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;

int n;
char c[70];
bool list[101][110];
int code[101][110];
int base,secs,nextst;

int main(){
      
  for(int i=0;i<101;i++)
      for(int j=0;j<110;j++)
	code[i][j] = -1;

  scanf("%d", &n);

  for(int zz=0;zz<n;zz++){

    scanf("%s", c);
    //cout << c << endl;
    base = 0;
    for(int i=0;i<strlen(c);i++){
         if(list[c[i]-40][zz] == false){
	   base++;
	   list[c[i]-40][zz] = true;
	 }
    }
    //count
    if(base == 1) base++;
    secs = pow(base,strlen(c)-1);
    code[c[0]-40][zz] = 1;

    nextst = 0;
    
    for(int i=1;i<strlen(c);i++){
      if(code[c[i]-40][zz] == -1){
	
	secs += nextst*pow(base, strlen(c)-1-i);
	code[c[i]-40][zz] = nextst;
	nextst++;
	if(nextst==1) nextst = 2;
      } else {
	
	secs += code[c[i]-40][zz]*pow(base, strlen(c)-1-i);
      }
     
    }
    
    cout << "Case #" << zz+1 << ": " << secs << endl;
    
    
    
    
    
    
  }

  return 0;
}