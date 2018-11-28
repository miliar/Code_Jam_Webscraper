/*
Author:CydorniaKnight@Gmail.com
Blog:http://hi.baidu.com/cydorniaknight
*/

#include<iostream>
#include<list>
using namespace std;

int t,n,m;

struct CARD{
	int c,s,t;
};

list<CARD> hand,deck;

CARD score;

void usehand(CARD card)
{
	score.c+=card.c;
	score.s+=card.s;
	score.t+=card.t-1;
}

void usedeck(CARD card)
{
	score.c+=card.c-1;
	score.s+=card.s;
	score.t+=card.t-1;
}

int simple_solve()
{
	int ret=0;
	int i,j,k;
	list<CARD>::iterator itr,tmp;

	list<CARD>::iterator draw[80];
	int drawlen=0;

	score.c=score.s=0;score.t=1;

	while(score.t){
		for(itr=hand.begin();itr!=hand.end();)
		{
			if(itr->t){
				usehand(*itr);
				tmp=itr;
				++itr;
				hand.erase(tmp);
			}else ++itr;
		}
		if(score.c&&score.t){
			for(itr=deck.begin();itr!=deck.end();)
			{
				if((itr->c)&&(itr->t)){
					usedeck(*itr);
					tmp=itr;
					++itr;
					deck.erase(tmp);
				}else ++itr;
			}
		}
	}

	return score.s;
}

int main()
{
	int ti,i;
	CARD tmp;
	scanf("%d",&t);
	for(ti=1;ti<=t;++ti)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf("%d%d%d",&tmp.c,&tmp.s,&tmp.t);
			hand.push_back(tmp);
		}
		scanf("%d",&m);
		for(i=0;i<m;++i)
		{
			scanf("%d%d%d",&tmp.c,&tmp.s,&tmp.t);
			deck.push_back(tmp);
		}
		printf("Case #%d: %d\n",ti,simple_solve());
	}
	return 0;
}