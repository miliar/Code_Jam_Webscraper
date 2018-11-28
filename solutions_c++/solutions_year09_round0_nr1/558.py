#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

class Word
{
public:
	Word() {memset(word,0,sizeof(word));}
	void clear() {memset(word,0,sizeof(word));}
	int word[15];
};

int L,D,N;
Word word[5000];

void init()
{
	char str[1024];
	scanf("%d %d %d",&L,&D,&N);
	for(int i = 0; i < D; i++)
	{
		scanf("%s",str);
		for(int j = 0; j < L; j++)
			word[i].word[j] = 1<<(str[j]-'a');
	}
}

void solve()
{
	char str[1024];
	int i,j,k;
	int s, t, cnt;
	Word now;
	for(i = 0; i < N; i++)
	{
		scanf("%s",str);
		now.clear();
		cnt = 0;
		s = t = 0;
		for(j = 0; j < L; j++)
		{
			t = s;
			if(str[s]=='(')
			{
				while(str[++t]!=')')
					now.word[j] |= 1<<(str[t]-'a');
				s = t+1;
			}
			else
				now.word[j] |= 1<<(str[t]-'a'), s = t+1;
		}
		for(j = 0; j < D; j++)
		{
			for(k = 0; k < L; k++)
				if((word[j].word[k]&now.word[k])==0)
					break;
			if(k==L)
				cnt++;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
}

void print()
{
}

int main(void)
{
    init();
    solve();
    print();
    return 0;
}

