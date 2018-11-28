#include <cstdio>
#include <queue>
#define ORANGE true
#define BLUE false

struct Button
{
	bool color;
	int button;
	Button(bool scolor, int sbutton)
	{
		button = sbutton;
		color = scolor;
	}
};

void solve(int N, int tc)
{
	std::queue<Button *> Qo, Qb, Qt;
	int time, b;
	char c;
	bool button_pressed;
	int pos_o, pos_b;
	Button *next;
	Button *next_b, *next_o;
	int i;
	
	//printf("Trying testcase %d\n",tc);

	for(i=0;i<N;i++)
	{
		scanf("%c %d", &c, &b);
		//printf("%c: %d\n", c, b); 
		if(i!=N-1) scanf("%*c");
		if(c=='O') Qo.push(new Button(ORANGE, b));
		else if(c=='B') Qb.push(new Button(BLUE, b));
		Qt.push(new Button(c=='O'?ORANGE:BLUE, b));
	}
	
	pos_o = pos_b = 1;
	time = 0;
	while(!Qt.empty())
	{
		//printf("Time %d, pos_o %d, pos_b %d\n", time, pos_o, pos_b);
		next = Qt.front();
		next_o = Qo.front();
		next_b = Qb.front();

		if(next->button == (next->color==ORANGE?pos_o:pos_b))
		{
			//printf("%c robot can press button %d!\n", next->color==ORANGE?'O':'B', next->button);
			//Press the button
			Qt.pop();
			if(next->color==ORANGE) Qo.pop();
			else Qb.pop();
			//printf("Poped!\n");
			if(Qt.empty()){ time++; continue; }

			//Move the other bot if needed
			if(!Qb.empty() && next->color==ORANGE)
			{
				if(next_b->button != pos_b)
				{
					if((next_b->button - pos_b)>0) pos_b++;
					else pos_b--;
				}
			}
			else if(!Qo.empty() && next->color==BLUE)
			{
				if(next_o->button != pos_o)
				{
					if((next_o->button - pos_o)>0) pos_o++;
					else pos_o--;
				}	
			}
			//printf("Button pressing done!\n");
		}
		else
		{
			//Move bots if needed
			if(!Qb.empty() && next_b->button != pos_b)
			{
				if((next_b->button - pos_b)>0) pos_b++;
				else pos_b--;

			}
			if(!Qo.empty() && next_o->button != pos_o)
			{
				if((next_o->button - pos_o)>0) pos_o++;
				else pos_o--;
			}
		}
		

		time++;
	}

	printf("Case #%d: %d\n", tc, time);
}

int main()
{
	int T, n;

	scanf("%d\n", &T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d ", &n);
		solve(n,i);
	}

	return 0;
}
