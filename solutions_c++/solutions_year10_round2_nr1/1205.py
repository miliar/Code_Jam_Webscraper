#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <stdio.h>
#include <stdlib.h>

struct tree
{
	tree() : value("") {}
	tree(char* str) : value(str) {}
	
	int add(char* val)
	{
		std::vector<tree*>::iterator it = children.begin();
		
		for (; it != children.end(); it++)
		{
			if ((*it)->value == val) // Already exists -> No new node created
			{
				char* next = strtok(NULL, "/");
				int res = 0;
				
				if (next)
					res += (*it)->add(next);
				return res;
			}
		}
		
		struct tree* node = new tree(val);
		children.push_back(node);
			
		char* next = strtok(NULL, "/");
		int res = 1;
		
		if (next)
			res += node->add(next);		
		
		return res;
	}
	
	void print(std::string space)
	{
		std::cout << space << "/" << value << std::endl;
		std::vector<tree*>::iterator it = children.begin();
		for (; it != children.end(); it++)
			(*it)->print(space + " ");
	}
		
	std::string value;
	std::vector<tree*> children;
};



int main()
{
	int nb_input = 0;
	std::cin >> nb_input;
	
	for (int input = 1; input <= nb_input; ++input)
	{
		int n, m;
		std::cin >> n >> m;

		struct tree root;
		
		for (int i = 0; i < n; ++i)
		{
			char val[128];
			std::cin >> val;
			
			char* tok = strtok(val, "/");
			
			root.add(tok);
		}
		
		int res = 0;
		
		for (int i = 0; i < m; ++i)
		{
			char val[128];
			std::cin >> val;
			
			char* tok = strtok(val, "/");
			
			res += root.add(tok);
		}
		
		std::cout << "Case #" << input << ": " << res << std::endl;
	}
	
	return 0;
}