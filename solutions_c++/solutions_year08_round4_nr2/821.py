//KIA at Full speed ^_^
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;



#define ll long long
ll tsquare(ll x1, ll  y1, ll x2, ll y2, ll x3, ll y3)
{
	return
		abs((x1 * y2 - x1 * y3) +
		(x2 * y3 - x2 * y1) +
		(x3 * y1 - x3 * y2));
}


int main(){
	FILE* in = fopen("B.in","r");
	FILE* out = fopen("B.out","w");
	int TestCase = 0;
	fscanf(in, "%d\n", &TestCase);
	for(int i = 0; i < TestCase; i++)
	{	
		int N, M;
		ll Area;
		long long x1=0,x2=0,x3=0,y1=0,y2=0,y3=0, sq;
		fscanf(in, "%d%d%lld", &N, &M, &Area);
		int Answer = 0;
		if(Area> (N*M)){
			fprintf(out, "Case #%d: IMPOSSIBLE\n", i+1);
		}
		else{
			
			x1=0;
			y1=0;
			for(int i1 = 0; i1 <= N; i1++){
				for(int j1 = 0; j1 <= M; j1++){
					for(int i2 = 0; i2 <= N; i2++){
						for(int j2 = 0; j2 <= M; j2++){
							sq = tsquare(0,0,i1,j1,i2,j2);
							if(sq == Area){
								x2=i1;
								y2=j1;
								x3=i2;
								y3=j2;
								goto l1;
							}
						}
					}
				}
			}
l1:
			fprintf(out, "Case #%d: %lld %lld %lld %lld %lld %lld\n", i+1, x1, y1, x2, y2, x3, y3);
		}
		
	}
	return 0;
}
