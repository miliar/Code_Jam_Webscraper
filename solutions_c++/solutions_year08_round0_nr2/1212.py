#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <queue>
#include <vector>

using namespace std;

bool maxFlow[300][300];
int prevNode[300];

bool FindPath(int end)
{
	queue<int> q;
	int val, i;

	q.push(0);
	while(!q.empty()) // BFS
	{
		val = q.front();
		for(i=end; i>=1; i--)
		{
			if(maxFlow[val][i] && prevNode[i]==-1) // 길이 있고 지나온 길이 아니면
			{
				q.push(i);
				prevNode[i] = val; // 바로 앞 노드 번호 저장
				if(i == end) return true; // 끝 노드에 도달했으면 true
			}
		}
		q.pop();
	}
	
	return false;
}

int main(void)
{
	int tc;
	int stA[110], stB[110], edA[110], edB[110];
	int na, nb, a, b, c, d, turn;
	int i, j, t;
	int cntA, cntB;
	FILE *in, *out;
	in = fopen("B.in", "r");
	out = fopen("B.out", "w");

	fscanf(in, "%d", &tc);

	for(t=1; t<=tc; t++)
	{
		fscanf(in, "%d", &turn);
		fscanf(in, "%d %d", &na, &nb);

		for(i=0; i<na; i++)
		{
			fscanf(in, "%d:%d %d:%d", &a, &b, &c, &d);
			stA[i] = a*60 + b;
			edA[i] = c*60 + d;
		}
		for(i=0; i<nb; i++)
		{
			fscanf(in, "%d:%d %d:%d", &a, &b, &c, &d);
			stB[i] = a*60 + b;
			edB[i] = c*60 + d;
		}

		memset(maxFlow, false, sizeof(maxFlow));
		memset(prevNode, -1, sizeof(prevNode));


		for(i=1; i<=na; i++) maxFlow[0][i] = true;
		for(i=1; i<=nb; i++) maxFlow[na+i][na+nb+1] = true;

		for(i=1; i<=na; i++)
		{
			for(j=1; j<=nb; j++)
			{
				if(stB[j-1] >= edA[i-1]+turn) maxFlow[i][na+j] = true;
				else maxFlow[i][na+j] = false;
			}
		}

		cntA = 0;
		while(FindPath(na+nb+1) == true) // 첫 노드에서 끝 노드까지 가는 길이 있으면
		{
			cntA++; // 결과값 하나 증가시켜주고
			
			i = na+nb+1;
			while(i > 0) // 그 길을 없애고 반대길을 만든다.
			{
				maxFlow[prevNode[i]][i] = false;
				maxFlow[i][prevNode[i]] = true;
				i = prevNode[i];
			}
			memset(prevNode, -1, sizeof(prevNode));
		}

		
		memset(maxFlow, false, sizeof(maxFlow));
		memset(prevNode, -1, sizeof(prevNode));
		for(i=1; i<=nb; i++) maxFlow[0][i] = true;
		for(i=1; i<=na; i++) maxFlow[nb+i][nb+na+1] = true;
		for(i=1; i<=nb; i++)
		{
			for(j=1; j<=na; j++)
			{
				if(stA[j-1] >= edB[i-1]+turn) maxFlow[i][nb+j] = true;
				else maxFlow[i][nb+j] = false;
			}
		}
		
		cntB = 0;
		while(FindPath(nb+na+1) == true) // 첫 노드에서 끝 노드까지 가는 길이 있으면
		{
			cntB++; // 결과값 하나 증가시켜주고
			
			i = nb+na+1;
			while(i > 0) // 그 길을 없애고 반대길을 만든다.
			{
				maxFlow[prevNode[i]][i] = false;
				maxFlow[i][prevNode[i]] = true;
				i = prevNode[i];
			}
			memset(prevNode, -1, sizeof(prevNode));
		}


	
		fprintf(out, "Case #%d: %d %d\n", t, na-cntB, nb-cntA);
	}
	return 0;
}