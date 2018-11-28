#include<iostream>
#include<cstdio>

using namespace std;

int main(){
  int n; cin >> n;

  for(int ii=0;ii<n;ii++){
    int o,b,m; o=b=1;
    cin >> m;
    int odata[1000]={0},bdata[1000]={0},op=0,bp=0;
    int bn=0,on=0;
    char alphabet[1000];
    for(int i=0;i<m;i++){
      char c; int d;;
      cin >> c >> d;
      alphabet[i]=c;
      if(c=='B')bdata[bp++]=d;
      else odata[op++]=d;
    }
    int opos=1,bpos=1,ans=0;
    for(int i=0;i<m;){
      ans++;
      if(alphabet[i]=='B'){
	if(bdata[bn]==bpos){
	  i++; bn++;
	}else if(bdata[bn]>bpos)bpos++;
	else bpos--;
	if(odata[on]>opos)opos++;
	else if(odata[on]<opos)opos--;
      }else{
	if(odata[on]==opos){
	  i++; on++;
	}else if(odata[on]>opos)opos++;
	else opos--;
	if(bdata[bn]>bpos)bpos++;
	else if(bdata[bn]<bpos)bpos--;
      }
      //if(ii==16)printf("%d: %d,%d\n",ans,opos,bpos);
    }
    printf("Case #%d: %d\n",ii+1,ans);
  }
  
  return 0;
}
