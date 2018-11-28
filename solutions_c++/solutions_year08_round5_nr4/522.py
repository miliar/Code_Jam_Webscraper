#include <iostream>
using namespace std;

int main(){
  freopen("D-small-attempt0.in","r",stdin);
  freopen("D-small-attempt0.out","w",stdout);
  int N;
  int cases;
  cin>>N;
  for(cases=1;cases<=N;++cases){
    int H,W,R;
	int i;
	int r,c;
	cin>>H>>W>>R;
	int ans[101][101]={1};
	int rock[101][101]={0};
	for(i=0;i<R;++i){
	  cin>>r>>c;
	  rock[r][c]=1;
	}
	ans[1][1]=1;
	for(r=1;r<=H;++r)
		for(c=1;c<=W;++c){
				int rr=r-1;
				int cc=c-2;
			if(rr>=1&&cc>=1){			
				if(rock[rr][cc]!=1){
				  ans[r][c]=(ans[r][c]+ans[rr][cc])%10007;
				}
			}
            rr=r-2;
			cc=c-1;
				if(rr>=1&&cc>=1){			
				if(rock[rr][cc]!=1){
				  ans[r][c]=(ans[r][c]+ans[rr][cc])%10007;
				}
			}

		}
      cout<<"Case #"<<cases<<": "<<ans[H][W]<<endl;
  }  
  return 0;
}