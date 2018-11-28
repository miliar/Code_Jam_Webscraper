#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

void swap(int& A, int& B)
{
	int t = A;
	A = B;
	B = t;
}
bool gcd(int A, int B)
{
	int count = 0;
	while (B>0 && A/B == 1)
	{
		count++;
		int t = A%B;
		A = B;
		B = t;
	}
	
	if (count%2==0)
		return true;
	else return false;
	
}

int main()
{
    ifstream ifs("C-small-attempt0.in");
    ofstream ofs("C-small-attempt0.out");

    int T;
	int A1, A2, B1, B2;

	//ofs.setf(ios::fixed, ios::floatfield);
	//ofs.precision(7);

    ifs >> T;
    for (int i=0;i<T;i++)
    {
		ifs >> A1 >> A2 >> B1 >> B2;
		int count = 0;
		for (int j=A1;j<=A2;j++)
			for (int l=B1;l<=B2;l++)
			{
				int A = j; int B = l;
				if (A<B) swap(A, B);
				if (gcd(A,B))
					count++;
			}
		ofs << "Case #" << i+1 << ": " << count << endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}
