#include<stdio.h>
#include<vector>
#include<utility>
#include<stack>
using namespace std;

int x[300][300],w[300][300];
int counts[300];
char word[200];
vector<char> X;

int main()
{
	int T, ks, i, C, L, j,ok;
	char a;
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		for(i='A';i<='Z';i++)
		{
			counts[i]=0;
			for(j='A';j<='Z';j++)
				x[i][j]=w[i][j]=0;
		}

		scanf("%d",&C);
		while(C--)
		{
			scanf("%s",word);
			w[word[0]][word[1]]=word[2];
			w[word[1]][word[0]]=word[2];
		}

		scanf("%d",&C);
		while(C--)
		{
			scanf("%s",word);
			x[word[0]][word[1]]=1;
			x[word[1]][word[0]]=1;
		}

		scanf("%d",&L);
		scanf("%s",word);

		stack<char> S;
		for(i=0;i<L;i++)
		{
			if(S.empty()) 
			{
				S.push( word[i] );
				counts[ word[i] ] ++;
			}
			else
			{
				a = S.top();

				if(w[a][ word[i] ])
				{
					S.pop();
					S.push( w[a][word[i]] );
					counts[a]--;
					counts[w[a][word[i]]]++;
				}
				else
				{
					ok = 0;
					for(j='A';j<='Z';j++)
						if(counts[j] && x[j][word[i]])
						{
							ok = 1;
							break;
						}

					if(ok)
					{
						for(j='A';j<='Z';j++) counts[j]=0;
						while(!S.empty()) S.pop();
					}
					else
					{
						S.push( word[i] );
						counts[ word[i] ] ++;
					}
				}
			}
		}

		printf("Case #%d: [",ks);
		X.clear();
		while(!S.empty()) 
		{
			X.push_back( S.top() ); 
			S.pop();
		}

		if(X.size()==0)
		{
			printf("]\n");
			continue;
		}
		for(i=X.size()-1;i>=0;i--)
		{
			printf("%c",X[i]);
			if(i) printf(", ");
		}
		printf("]\n");

	}

	return 0;
}