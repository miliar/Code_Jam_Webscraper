#include <iostream>
#include <vector>

#define NUM_BASE 26

using namespace std;

int combinations[NUM_BASE][NUM_BASE];
bool opposed[NUM_BASE][NUM_BASE];

int trans(char in)
{
	return(in-'A');
}

void explode(vector<int>* stack)
{
	if(stack->size() < 2)
	{
		return;
	}

	int e = (*stack)[stack->size()-1];
	//cout << "EXPLODE STAGE 1" << endl;
	for(int i = stack->size()-2; i >= 0; i--)
	{
		//cout << "CHECK: " << i << endl;
		if(opposed[((*stack)[i])][e])
		{
			stack->clear();
			return;
		}
		//cout << "CHECKDONE" << endl;
	}
}

void resolve(vector<int>* stack)
{
	int tail = (*stack)[stack->size()-1];
	int temp, temp1, temp2;
	while(true)
	{
		if(stack->size() < 2)
		{
			return;
		}
		temp1 = (*stack)[stack->size()-1];
		temp2 = (*stack)[stack->size()-2];
		if((temp = combinations[temp1][temp2]) != -1)
		{
			stack->pop_back();
			stack->pop_back();
			stack->push_back(temp);
		}
		else
		{
			break;
		}
	}

	if(tail == (*stack)[stack->size()-1])
	{
		explode(stack);
	}
}

void output(vector<int> stack, int c)
{
	cout << "Case #" << c << ": [";
	bool first = true;
	for(int i = 0; i < stack.size(); i++)
	{
		if(!first)
		{
			cout << ", ";
		}
		else
		{
			first = false;
		}

		cout << (char)(stack[i]+'A');
	}
	cout << "]" << endl;
}

int main()
{
	int t, c, d, n;
	char temp1, temp2, temp3;
	int t1, t2, t3;
	vector<int> stack;

	cin >> t;
	for(int i = 0; i < t; i++)
	{
		stack.clear();
		for(int j = 0; j < NUM_BASE; j++)
		{
			for(int k = 0; k < NUM_BASE; k++)
			{
				combinations[j][k] = -1;
				opposed[j][k] = false;
			}
		}

		cin >> c;
		for(int j = 0; j < c; j++)
		{
			cin >> temp1 >> temp2 >> temp3;
			t1 = trans(temp1);
			t2 = trans(temp2);
			t3 = trans(temp3);
			combinations[t1][t2] = t3;
			combinations[t2][t1] = t3;
		}

		cin >> d;
		for(int j = 0; j < d; j++)
		{
			cin >> temp1 >> temp2;
			t1 = trans(temp1);
			t2 = trans(temp2);
			opposed[t1][t2] = true;
			opposed[t2][t1] = true;
		}

		cin >> n;
		for(int j = 0; j < n; j++)
		{
			cin >> temp1;
			t1 = trans(temp1);
			stack.push_back(t1);
			resolve(&stack);
		}

		output(stack, i+1);
	}
}
