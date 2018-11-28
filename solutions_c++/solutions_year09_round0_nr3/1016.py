#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
using namespace std;

int main(){
  int N;
  char line[600];
  int a[600][20];
  scanf("%d",&N);
  fgets(line,510,stdin);
  for(int tc=1;tc<=N;tc++){
    memset(a,0,sizeof(a));
    fgets(line,510,stdin);
    for(int i=1;i<strlen(line);i++){
      for(int j=i-1;j>=0;j--){
	if(line[i]=='e'){
	  if(line[j]=='w'){
	    a[i][1]++;
	  }
	  else if(line[j]=='m'){
	    a[i][6]+=a[j][5]%10000;
	  }
	  else if(line[j]=='d'){
	    a[i][14]+=a[j][13]%10000;
	  }
	}
	else if(line[i]=='l'){
	  if(line[j]=='e'){
	    a[i][2]+=a[j][1]%10000;
	  }
	}
	else if(line[i]=='c'){
	  if(line[j]=='l'){
	    a[i][3]+=a[j][2]%10000;
	  }
	  else if(line[j]==' '){
	    a[i][11]+=a[j][10]%10000;
	  }
	}      
	else if(line[i]=='o'){
	  if(line[j]=='c'){
	    a[i][4]+=a[j][3]%10000;
	    a[i][12]+=a[j][11]%10000;
	  }
	  else if(line[j]=='t'){
	    a[i][9]+=a[j][8]%10000;
	  }
	} 
	else if(line[i]=='m'){
	  if(line[j]=='o'){
	    a[i][5]+=a[j][4]%10000;
	  }
	  else if(line[j]=='a'){
	    a[i][18]+=a[j][17]%10000;
	  }
	}
	else if(line[i]==' '){
	  if(line[j]=='e'){
	    a[i][7]+=a[j][6]%10000;
	    a[i][15]+=a[j][14]%10000;
	  }
	  else if(line[j]=='o'){
	    a[i][10]+=a[j][9]%10000;
	  }
	}
	else if(line[i]=='t'){
	  if(line[j]==' '){
	    a[i][8]+=a[j][7]%10000;
	  }
	}
	else if(line[i]=='d'){
	  if(line[j]=='o'){
	    a[i][13]+=a[j][12]%10000;
	  }
	}
	else if(line[i]=='j'){
	  if(line[j]==' '){
	    a[i][16]+=a[j][15]%10000;
	  }
	}
	else if(line[i]=='a'){
	  if(line[j]=='j'){
	    a[i][17]+=a[j][16]%10000;
	  }
	}
      }
    }
    printf("Case #%d: ",tc);
    int ans=0;
    for(int i=0;i<strlen(line);i++)ans+=a[i][18]%10000;
    printf("%04d\n",ans%10000);
  }
  return 0;
}
