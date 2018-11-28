#include <deque>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;

deque<int> b_order;
deque<int> o_order;
deque<pair<int,int> > order;

struct State_t {
    int t,b_pos,o_pos;
};

State_t state;

void get_input()
{
    int n;
    {
	b_order.clear();
	o_order.clear();
	order.clear();
	state.t = 0;state.b_pos=1;state.o_pos=1;
    }
    cin >> n;
    for(int i=0;i<n;++i)
    {
	char robo;
	int pos;
	cin >> robo >> pos;
	if(robo == 'B')
	{
	    order.push_back(make_pair(0,pos));
	    b_order.push_back(pos);
	}
	else if(robo == 'O')
	{
	    order.push_back(make_pair(1,pos));
	    o_order.push_back(pos);
	}
	else
	    assert(false);
    }
}

int step(int cur,int dest,int lim)
{
    if(dest == cur)return dest;
    else if(dest < cur)
	return max(dest,cur-lim);
    else if(cur < dest)
	return min(dest,cur+lim);
    else
	assert(false);
}

void step_blue(int lim)
{
    state.b_pos = step(state.b_pos,b_order.front(),lim);
}

void step_orange(int lim)
{
    state.o_pos = step(state.o_pos,o_order.front(),lim);
}

void go_next()
{
    pair<int,int> now = order.front();order.pop_front();
    switch(now.first)
    {
    case 0:{
	int spent = abs(now.second - state.b_pos) + 1;

	assert(now.second == b_order.front());

	step_orange(spent);

	state.t += spent;
	state.b_pos = now.second;

	b_order.pop_front();
	break;
    }
    case 1:{
	int spent = abs(now.second - state.o_pos) + 1;

	assert(now.second == o_order.front());

	step_blue(spent);

	state.t += spent;
	state.o_pos = now.second;

	o_order.pop_front();
	break;
    }
    default:
	assert(false);
    }
}

int main()
{
    int n;cin >> n;
    for(int i=1;i<=n;++i)
    {
	get_input();
	for(;!order.empty();)
	    go_next();
	printf("Case #%d: %d\n",i,state.t);
    }
    return 0;
}
