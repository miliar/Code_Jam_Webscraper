/*
 * B.cpp
 *
 *  Created on: 2010/06/06
 *      Author: jun
 */

#include <stdio.h>

#include <vector>

using namespace std;

typedef struct
{
	int price;
	int needed[10000];
}ticket;

int main()
{
	int i,j,k;
	int t,T;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int P;
		scanf("%d\n",&P);
		int M[1<<P];
		for (i=0;i<(1<<P);i++){
			scanf("%d ",&M[i]);
		}
		vector<ticket> prices[P];
		int m_num=1<<P;
		for (i=0;i<P;i++){
			m_num/=2;
			for (j=0;j<m_num;j++){
				ticket tk;
				scanf("%d ",&tk.price);
				for (k=0;k<(1<<P);k++)tk.needed[k]=0;
				prices[i].push_back(tk);
			}
		}
		//出る試合にマークをつける
		for (i=0;i<(1<<P);i++){
			int p_idx=i;
			for (j=0;j<P;j++){
				p_idx/=2;
				prices[j][p_idx].needed[i]=1;
			}
		}
		//買わないでもいいものにマークをつけていく
		for (i=0;i<(1<<P);i++){
			int p_idx=i;
			for (j=0;j<M[i];j++){
				p_idx/=2;
				prices[j][p_idx].needed[i]=0;
			}
		}
		int result=0;
		for (i=0;i<P;i++){
			for (j=0;j<prices[i].size();j++){
				int buy_flag=0;
				for (k=0;k<(1<<P);k++){
					if (prices[i][j].needed[k]==1){
						buy_flag=1;break;
					}
				}
				if (buy_flag)result+=prices[i][j].price;
			}
		}
		printf("Case #%d: %d\n",t,result);
	}
	return 0;
}
