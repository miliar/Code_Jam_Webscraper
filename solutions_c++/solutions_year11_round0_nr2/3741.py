#include <stdio.h>
#include <string.h>

#include <map>
#include <iostream>
#include <string>

using namespace std;

const int MAX = 104;
int stack[MAX];
int top;

map<int, int> combine;
map<int, int> oppose;

// which letter appeared.
int flag[256];

int is_oppose()
{
	memset(flag, 0, sizeof(flag));
	for(int i = 0;i<top;i++)
	{
		// oppose.
		if(flag[oppose[stack[i]]])
			return 1;

		flag[(int)stack[i]] = 1;
	}
	return 0;
}

void output()
{
	static int cas = 1;
	printf("Case #%d: [", cas++);

	if(top)
	{
		printf("%c", stack[0]);
		for(int i = 1;i<top;i++)
		{
			printf(", %c", stack[i]);
		}
	}

	printf("]\n");
}

void work()
{
	combine.clear();
	oppose.clear();

	int n;
	
	cin >> n;
	string tmp;
	for(int i = 0;i<n;i++)
	{
		cin >> tmp;
		combine[(tmp[0] << 8) + tmp[1]] = tmp[2];
		combine[(tmp[1] << 8) + tmp[0]] = tmp[2];
	}

	cin >> n;
	for(int i = 0;i<n;i++)
	{
		cin >> tmp;
		oppose[tmp[0]] = tmp[1];
		oppose[tmp[1]] = tmp[0];
	}

	cin >> n;
	cin >> tmp;

	// clear stack and start.
	top = 0;

	stack[top++] = tmp[0];
	for(int i = 1;i<n;i++)
	{
		stack[top++] = tmp[i];
		//while(top >= 2 && combine[(stack[top-1] << 8) + stack[top-2]])
		int ii;
		if(top >= 2 && (ii = combine[(stack[top-1] << 8) + stack[top-2]]))
		{
			top -= 2;
			stack[top++] = ii;
		}		
		
		if(is_oppose())
		{
			top = 0;
		}
	}

	output();
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for(int i = 0;i<t;i++)
	{
		work();
	}
	return 0;
}