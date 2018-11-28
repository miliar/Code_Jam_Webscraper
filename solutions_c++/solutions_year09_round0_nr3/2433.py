#include <stdio.h>
#include <list>

char *legend = "welcome to code jam";

class node
{
private:
	int m_Index;
	std::list <node *> m_Nodes;

public:	
	node(int index)
	{
		this->m_Index = index;
	}

	void insert(char* buffer, int index = 0)
	{
		if(index <= this->m_Index)
			return;

		int i, m = strlen(buffer);
		node *anode;

		for(i = 0;i < m;++i)
		{
			if(buffer[i] == legend[index])
			{
				anode = new node(index);
				anode->insert(buffer + i + 1, index + 1);
				this->m_Nodes.push_back(anode);
			}
		}
	}

	int count(int value)
	{
		int total = 0;
		std::list<node *>::iterator i;

		for(i = this->m_Nodes.begin();i != this->m_Nodes.end();++i)
		{
			total += (*i)->count(value);
			total %= 10000;
		}
		if((total == 0) && (this->m_Index == value))
			++total;
		return total;
	}
};

int main(int argc, char* argv[])
{
	long i, m;
	char buffer[1024];

	scanf("%ld\n", &m);
	for(i = 0;i < m;++i)
	{
		node anode(-1);

		fgets(buffer, 1024, stdin);
		anode.insert(buffer);
		printf("Case #%d: %04ld\n", i + 1, anode.count(strlen(legend) - 1));
	}
	return 0;
}
