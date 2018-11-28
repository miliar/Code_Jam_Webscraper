#include <cstdio>

int main(){
  int L, D, N;
  char dic[6000][20], str[1000];
  
  scanf("%d%d%d",&L,&D,&N);
  for(int i=0;i<D;i++)
    scanf("%s",dic[i]);
  for(int i=0;i<N;i++){
    int cnt=0;
    scanf("%s",str);
    for(int j=0;j<D;j++){
      int p1=0;
      int p2=0;
      bool flag1=true;
      for(int k=0;k<L;k++,p2++,p1++){
	bool flag2=false;
	if(str[p1]=='('){
	  p1++;
	  while(str[p1]!=')'){
	    if(dic[j][p2]==str[p1])flag2=true;
	    p1++;
	  }
	}
	else{
	  if(dic[j][p2]==str[p1])flag2=true;
	}
	if(flag2==false){
	  flag1=false;
	  break;
	}
      }
      if(flag1==true)cnt++;
    }
    printf("Case #%d: %d\n",i+1,cnt);
  }
  return 0;
}
