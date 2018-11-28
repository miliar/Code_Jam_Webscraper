#include <iostream>
#include <vector>
using namespace std;

struct coordinate
{
	unsigned long int x, y;
};

int main(void)
{
	unsigned int num_casos;

	cin >> num_casos;
	for(unsigned int c = 1; c <= num_casos; c++)
	{
		unsigned long long int n, A, B, C, D, x, y, M;
		vector<coordinate> trees;
		coordinate aux;

		cin >> n >> A >> B >> C >> D >> x >> y >> M;
		aux.x = x, aux.y = y;
		trees.push_back(aux);
		for(unsigned long long int i = 1; i < n; i++)
		{
			aux.x = (A*aux.x + B) % M;
			aux.y = (C*aux.y + D) % M;
			trees.push_back(aux);
		}

		unsigned long long int tam = trees.size(), count = 0;
		for(unsigned long long int i = 0; i < tam; i++)
		{
			for(unsigned long long int j = i + 1; j < tam; j++)
			{
				for(unsigned long long int k = j + 1; k < tam; k++)
				{
					if((trees[i].x + trees[j].x + trees[k].x) % 3 == 0 && (trees[i].y + trees[j].y + trees[k].y) % 3 == 0)
						count++;
				}
			}
		}
		cout << "Case #" << c << ": " << count << endl;
	}
}

