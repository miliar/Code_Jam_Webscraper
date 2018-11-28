#include <iostream>
#include <fstream>

using namespace std;

void sort (int f[], int L)
{
	for (int i=0; i<L; i++)
	{
		for (int j=0; j<L-1; j++)
		{
			if (f[j] < f[j+1])
			{
				int temp = f[j];
				f[j] = f[j+1];
				f[j+1] = temp;
			}
		}
	}
}

int main (int argc, char *argv[])
{
        fstream file;

        file.open (argv[1], ios::in);

        int N;
        file >> N;

	for (int i=0; i<N; i++)
	{

		int P, K, L;
		file >>P >>K >>L;
		int freq[1001];
		for (int j=0; j<L; j++)
			file >> freq[j];

		sort (freq, L);
		int keystrokes = 0;
		int pos = 1;
		for (int j=1; j<=L; j++)
		{
			keystrokes += (pos*freq[j-1]);
			if (j%K == 0)
				pos++;
		}
                cout <<"Case #" <<i+1 <<": " <<keystrokes <<endl;
        }
        return 0;
}
        
