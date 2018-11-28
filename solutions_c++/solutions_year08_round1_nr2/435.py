#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;
//int customer[2002][2003];
int customer[102][102];

int main()
{
	FILE *in  = fopen("B-small-attempt1.in","r");
	FILE *out = fopen("B-small-attempt1.out","w");
	int tests;
	
	fscanf(in,"%d",&tests);
	int tmpX,tmpY;
	for(int t = 0; t<tests; t++){
		int N,M,T;
		int best = 2147454;
		memset(customer,-1,sizeof(customer));
		fscanf(in,"%d",&N);
		fscanf(in,"%d",&M);
		vector<int> sol(N,-1);
		vector<int> satCust(M+1);
		for(int i = 0; i<M; i++){
			fscanf(in,"%d",&T);	
			for(int j = 0; j<T; j++){
				fscanf(in,"%d %d",&tmpX, &tmpY);	
				customer[i][tmpX-1] = tmpY;
				if(tmpY == 1) satCust[i] = 1;
			}
		}
//con 0 0 estoy hecho
		int client = 0;
		for(int i = 0; i<(1<<N); i++){		//para cada posibilidad
			vector<bool> used(M,false);
			client = 0;
			int cant1 = 0;
			for(int bit = 0; bit<N; bit++)		//para cada gusto
				for(int k = 0; k<M; k++){			//para cada cliente
						if((i & (1<<bit)) != 0 && customer[k][bit] == 1 && !used[k]){	//si el gusto es malted 
							client++;cant1++;
							used[k] = true;
						}
						else if((i & (1<<bit)) == 0 && customer[k][bit] == 0 && !used[k]){	//si el gusto no es malted
							client++;
							used[k] = true;
						}
				}
				
			if(client >= M && cant1 < best)
			{
				best = cant1;
				for(int p = 0; p<N; p++){
					if((i & (1<<p)) != 0) sol[p] = 1;
					else sol[p] = 0;
					//sol[p] = i & (1<<p);
				}
				
			}
	}
		if(sol[0] == -1) 
			fprintf(out,"Case #%d: IMPOSSIBLE\n",t+1);
		else{
			fprintf(out,"Case #%d: ",t+1);
			for(int k = 0; k<sol.size()-1; k++)
				fprintf(out,"%d ",sol[k]);
			fprintf(out,"%d\n",sol[sol.size()-1]);
		}
}
    return EXIT_SUCCESS;
}

