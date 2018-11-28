#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

int* C[100];

typedef struct __tagdigit_node
{
	int digit_num;
	__tagdigit_node* next;
}digit_node;

void init_yanghui(int* input[], int nSize)
{
	input[0] = new int [3];
	memset (input[0], 0, 3 * sizeof(int));
	input[1] = new int [3];
	input[1][0] = 1;
	input[1][1] = 1;
	input[1][2] = 0;
	for (int i = 2; i != nSize; ++i)
	{
		input[i] = new int [i + 1];
		input[i][0] = 1;
		input[i][i] = 1;
		for (int j = 1; j < i; ++j)
			input[i][j] = input[i-1][j-1] + input[i-1][j];
	}
}

void digit_mov(int input, std::set<int>& movNum)
{
	digit_node* head = NULL;
	digit_node* current = NULL;

	movNum.insert(input);

	head = (digit_node*)malloc(sizeof(digit_node));
	head->digit_num = input % 10;
	input /= 10;

	current = head;
	int digit_count = 1;
	while (input > 0)
	{
		digit_node* newnode = (digit_node*)malloc(sizeof(digit_node));
		newnode->next = current;
		newnode->digit_num = input % 10;
		current = newnode;

		input /= 10;
		++digit_count;
	}
	head->next = current;

	current = head->next->next;
	int weight = 1;
	for (int i = 0; i != digit_count - 1; ++i)
		weight *= 10;
	for (int i = 0; i != digit_count - 1;  ++i)
	{
		if (current->digit_num == 0)
		{
			current = current->next;
			continue;
		}
		int siftedNum = 0;
		int current_weight = weight;
		digit_node* value_node = current;
		for (int j = 0; j != digit_count; ++j)
		{
			siftedNum += current_weight * value_node->digit_num;
			current_weight /= 10;
			value_node = value_node->next;
		}
		current = current->next;

		movNum.insert(siftedNum);
	}

	for (int i = 0; i != digit_count; ++i)
	{
		digit_node *freenext = current->next;
		free(current);
		current = freenext;
	}
}

int main(int argc, char *argv[])
{
	if (argc != 3)
	{
		std::cerr << "The input parameter error!" << std::endl;
		return -1;
	}

	std::ifstream iFile(argv[1]);
	std::ofstream oFile(argv[2]);

	if (!iFile.is_open())
	{
		std::cerr << "Can not open input file!" << std::endl;
		return -1;
	}

	init_yanghui(C, 100);

	int T, A, B;
	iFile >> T;
	for (int i = 0; i != T; ++i)
	{
		iFile >> A >> B;
		int TotalPair = 0;
		std::vector<bool> flag(B - A + 1, true);
		for (int j = A; j != B + 1; ++j)
		{
			if (!flag[j - A])
				continue;
			flag[j - A] = false;
			std::set<int> movNum;
			digit_mov(j, movNum);
			int sift_num = 0;
			std::set<int>::iterator it = movNum.begin();
			while(it != movNum.end())
			{
				if (*it >= A && *it <= B)
				{
					++sift_num;
					flag[*it - A] = false;
				}
				++it;
			}
			TotalPair += C[sift_num][2];
		}

		oFile << "Case #" << i + 1 << ": " << TotalPair << std::endl;
	}

	for (int i = 0; i != 100; ++i)
		delete C[i];

	iFile.close();
	oFile.close();

	return 0;
}