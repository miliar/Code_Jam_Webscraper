#pragma warning(disable:4786)
#include<stdio.h>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

vector<string> V;
char word[5002][20];
char line[1000000];

int main()
{
	freopen("Ahard.out","w",stdout);

	string A;
	int L,D,N,i,ks,j,k;

	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;i++)
		scanf("%s",word[i]);
	for(ks=1;ks<=N;ks++)
	{
		V.clear();
		scanf("%s",line);
		for(i=0;line[i];i++)
		{
			A="";

			if(line[i]=='(')
			{
				i++;
				while(line[i]!=')')
					A+=line[i++];
			}
			else
				A += line[i];

			V.push_back(A);
		}

		int cnt=0;
		for(i=0;i<D;i++)
		{
			for(j=0;j<L;j++)
			{
				for(k=V[j].size()-1;k>=0;k--)
					if(V[j][k]==word[i][j])
						break;

				if(k>=0)
					continue;
				else
					break;
			}		

			if(j==L)
				cnt++;
		}

		printf("Case #%d: %d\n",ks,cnt);
	}

	return 0;
}