#include <cstdio>
#include <queue>
using namespace std;
int test, qt, sec;
queue<int> b, o, number;
queue<char> color;
int bpos, opos;
bool erase;

int main()
{
	scanf("%d", &test);
	for(int t=0; t<test; t++)
	{
		bpos=1;opos=1;
		erase=false;
		scanf("%d", &qt);
		for(int i=0; i<qt; i++)
		{
			char x;
			int y;
			scanf("%c%c%d", &x, &x, &y);
			color.push(x); number.push(y);
			if(color.back() == 'B')			
				b.push(number.back());
			else
				o.push(number.back());
		}
		for(sec=0; !color.empty(); sec++)
		{
			if(bpos>b.front())bpos--;
			else if(bpos<b.front())bpos++;
			else if(color.front()=='B' && number.front()==bpos)
			{
				erase=true;
				b.pop();
			}
			if(opos>o.front())opos--;
			else if(opos<o.front())opos++;
			else if(color.front()=='O' && number.front()==opos)
			{
				erase=true;
				o.pop();
			}
			
			if(erase)
			{
				color.pop();
				number.pop();
			}
			erase=false;
		}
		printf("Case #%d: %d\n", t+1, sec);
	}
	return 0;
}
