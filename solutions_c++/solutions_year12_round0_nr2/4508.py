#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int n,s,p;
int scores[5];
bool used[5];
int maxscore;

int nosurprise(int score)
{
	if(score%3 == 0)
		return score/3;
	else if(score%3 == 1)
		return score/3+1;
	else
		return score/3+1;
}

int surprise(int score)
{
	if(score == 0)
		return 0;
	else if(score == 1)
		return 1;
	else if(score%3 == 0)
		return score/3 + 1;
	else if(score%3 == 1)
		return score/3 + 1;
	else 
		return score/3 + 2;
}

int main()
{
	freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
	int cases;
	cin>>cases;
	for(int i = 1;i<=cases; i++)
	{
		memset(used,0,sizeof(used));
		maxscore = 0;

		cin>>n>>s>>p;
		for(int j = 0; j<n; j++)
			cin>>scores[j];

		for(int j = 0;j<n;j++)
		{
			int tmp = nosurprise(scores[j]);
			if(tmp>=p)
			{
				maxscore++;
				used[j] = true;
			}
		}

		for(int j = 0;j<n;j++)
		{			
			if(s == 0)
				break;
			if(!used[j])
			{
				int tmp = surprise(scores[j]);
				if(tmp>=p)
				{
					maxscore++;
					used[j] = true;
					s--;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<maxscore<<endl;

	}
	return 0;
}