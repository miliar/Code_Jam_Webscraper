#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;

int cards[5001];
int cards2[5001];

void shift(int num_cards, int amount)
{
	for(int a=0;a<num_cards;a++)
		cards2[(a+amount)%num_cards]=cards[a];

	memcpy(cards,cards2,sizeof(cards2));
}
void insert(int num_cards, int card, int pos)
{
	for(int a=num_cards-1;a>=pos;a--)
		cards[a+1]=cards[a];
	cards[pos]=card;
}

int main()
{
	int a,b,c,d,tests;
	int K,n;
	int D[101];

	freopen("c-small.in", "rt", stdin);
	freopen("c-small.out", "wt", stdout);

	scanf("%d", &tests);

for(int test=1;test<=tests;test++)
{

	scanf("%d%d",&K,&n);
	fo(a,n) scanf("%d", &D[a]);

	insert(0,K,0);
	int num_cards=1, pos;
	for(a=K-1;a>=1;a--)
	{
		if(a>num_cards+1)
		{
			pos=(a-1)%(num_cards+1);
			shift(num_cards,pos);
			insert(num_cards,a,pos);
		}
		else if(a==num_cards+1)
			insert(num_cards,a,num_cards);
		else
		{
			// a <= num_cards
			pos=a-1;
			shift(num_cards,pos);
			insert(num_cards,a,pos);
		}

		num_cards++;
	}

	printf("Case #%d:", test);
	fo(a,n)
		printf(" %d", cards[D[a]-1]);

	printf("\n");

}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
