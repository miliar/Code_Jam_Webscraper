#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <crtdbg.h>

char inputLines[100][100];
int nInputLines;
int curLine;
char *cur;

class Node
{
public:
	Node()
	{
		children[0] = children[1] = NULL;
	};
	double weight;
	char feature[20];
	Node *(children[2]);
};

Node rootNode;

char nextChar()
{
	if (*cur == '\0')
	{
		curLine++;
		if (curLine >= nInputLines)
		{
			return '\0';	// no more lines
		}
		cur = inputLines[curLine];
	}
	return *cur++;
}

void putback()
{
	cur--;
	if (cur < inputLines[curLine])
	{
		curLine--;
		cur = inputLines[curLine] + strlen(inputLines[curLine]) - 1; // last char
	}
}

void getNextToken(char *s)
{
	char c;
	while (1)
	{
		c = nextChar();
		if (c == '\0')
		{
			*s = '\0';
			return;
		}
		if (c != ' ' && c != '\n')
		{
			break;
		}
	}
	if (c == '\0')
	{
		*s = '\0';
		return;
	}

	*s++ = c;
	if (c == '(' || c== ')' || c == '\0')
	{
		*s = '\0';
		return;
	}
	while (1)
	{
		c = nextChar();
		if (c == '\0')
		{
			*s = '\0';
			return;
		}
		if (c == ' ' || c == '\n' || c == '(' || c == ')')
		{
			putback();
			*s = '\0';
			return;
		}
		*s++ = c;
	}
}

double getNumber()
{
	char s[20];
	getNextToken(s);
	double v = atof(s);
	return v;
}

int nest = 0;
void printSpaces()
{
	for (int i = 0; i < nest; i++)
	{
		putchar(' ');
	}
}
#define nprintf	printSpaces(); printf

void parseTree(Node *node)
{
	char s[20];
	getNextToken(s);
	_ASSERT(strcmp(s, "(") == 0);
	double weight = getNumber();
	node->weight = weight;
	//nprintf("w=%f\n", weight);
	getNextToken(s);
	if (strcmp(s, ")") == 0)
	{
		strcpy(node->feature, "");
		return;
	}
	else
	{
		strcpy(node->feature, s);
		//nprintf("f:%s\n", s);
		nest++;
		for (int i = 0; i < 2; i++)
		{
			if (!node->children[i])
			{
				node->children[i] = new Node();
			}
			parseTree(node->children[i]);
		}
		nest--;
		getNextToken(s);
		_ASSERT(strcmp(s, ")") == 0);
	}
}

char features[80][20];
int numFeatures;

double sub(Node *n)
{
	double v = n->weight;
	if (strcmp(n->feature, "") != 0)
	{
		for (int i = 0; i < numFeatures; i++)
		{
			if (strcmp(n->feature, features[i]) == 0)
			{
				break;
			}
		}
		double v2;
		if (i < numFeatures)
		{
			// found
			v2 = sub(n->children[0]);
		}
		else
		{
			v2 = sub(n->children[1]);
		}
		v *= v2;
	}
	return v;
}

double calcCute()
{
	char a[20];
	getNextToken(a);
	char s[20];
	getNextToken(s);
	numFeatures = atoi(s);
	for (int i = 0; i < numFeatures; i++)
	{
		char f[20];
		getNextToken(f);
		strcpy(features[i], f);
	}
	double v = sub(&rootNode);
	return v;
}

int main(int argc, char *argv[])
{
	char line[200];
	gets(line);
	int nTestCases;
	sscanf(line, "%d", &nTestCases);
	for (int i = 0; i < nTestCases; i++)
	{
		printf("Case #%d: \n", i + 1);
		gets(line);
		sscanf(line, "%d", &nInputLines);
		for (int j = 0; j < nInputLines; j++)
		{
			gets(inputLines[j]);
		}
		curLine = 0;
		cur = inputLines[curLine];
		parseTree(&rootNode);

		gets(line);
		int numAnimals;
		sscanf(line, "%d", &numAnimals);
		for (int j = 0; j < numAnimals; j++)
		{
			gets(inputLines[0]);
			nInputLines = 1;
			curLine = 0;
			cur = inputLines[0];
			double v = calcCute();
			printf("%.7f\n", v);
		}
	}
	return 0;
}
