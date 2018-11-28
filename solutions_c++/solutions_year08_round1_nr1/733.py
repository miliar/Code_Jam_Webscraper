#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> A, B;

void sort();
int getProduct();

void getInput()
{
	int T, z, N;

	cin >> T;

	for (int i = 0; i<T; i++)
	{
		A.clear();
		B.clear();

		cin >> N;

		for (int j = 0; j<N; j++)
		{
			cin >> z;

			A.push_back(z);
		}

		for (int j = 0; j<N; j++)
		{
			cin >> z;

			B.push_back(z);
		}

		sort();
		cout << "Case #" << i+1 << ": " << getProduct() << endl;

	}
}

void sort()
{
	int temp;

    for (int i = 0; i < (int)(A.size() -1); i++)
    {
		for(int j = 1; j < (int)A.size(); j++)
        {
			if (A[j] < A[j-1])
            {
				temp = A[j];
				A[j] = A[j-1];
				A[j-1] = temp;
            }
        }
    }
	for (int i = 0; i < (int)(B.size() -1); i++)
    {
		for(int j = 1; (int) j < B.size(); j++)
        {
			if (B[j] > B[j-1])
            {
				temp = B[j];
				B[j] = B[j-1];
				B[j-1] = temp;
            }
        }
    }
}

int getProduct()
{
	int t = 0;

	for (int i = 0; i < (int) A.size(); i++)
	{
		t+= A[i]*B[i];
	}

	return t;
}

void main()
{
	getInput();

}