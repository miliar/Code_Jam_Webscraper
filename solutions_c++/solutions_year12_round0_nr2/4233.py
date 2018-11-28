#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void){
	int T,N,S,p,score;
	int xr,yr,zr;
	int xs,ys,zs;
	int quotient=0;
	vector<int> scores;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf("%d %d %d",&N,&S,&p);
		for(int j=0;j<N;j++){
			scanf("%d",&score);
			scores.push_back(score);
		}
		int result = 0;
		for(int k=0;k<scores.size();k++){	// loop through scores
			//if(scores[k] == 0) continue;
			int quotient = (int)scores[k]/3;
			if(scores[k] % 3 == 0){
				//quotient = scores[k]/3;
				xr = yr = zr = quotient;
				xs = xr-1;ys = yr;zs = zr+1;
				if(xr >= p)
					result++;
				else{
					if(S > 0 && (xs > 0) && (zs <= 10) && (xs >= p || ys >= p || zs >= p)){
						result++;
						S--;
					}
				}
			}
			else if(scores[k] % 3 == 1){
				//quotient = (int)scores[k]/3;
				xr=quotient;yr=quotient;zr=quotient+1;
				xs=quotient-1;ys=quotient+1;zs=quotient+1;
				if(zr <= 10 && xr >= p || zr >= p)
					result++;
				else{
					if(S > 0 && ys <= 10 && (xs >= p || ys >= p)){
						result++;
						S--;
					}
				}
			}
			else{
				//quotient = (int)scores[k]/3;
				xr = quotient;yr=quotient+1;zr=quotient+1;
				xs = quotient;ys=quotient;zs=quotient+2;
				if(yr <= 10 && xr >= p || yr >= p)
					result++;
				else{
					if(S > 0 && zs <= 10 && (xs >= p || zs >= p)){
						result++;
						S--;
					}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<result<<endl;
		scores.clear();
	}
	return 0;
}