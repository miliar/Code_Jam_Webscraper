#include <iostream>
using namespace std;

int main (int argc, char * const argv[]) 
{
	freopen("input4.txt", "rt", stdin);
	freopen("output4.txt", "wt", stdout);
	
	int T; 
	cin >> T;
	
	int array[1000], nfarray[1000], index[1000];
	bool fixed[1000];
	
	for(int i = 0; i < T; i++) {

		int N;
		cin >> N;
		int nfixed = 0;
		for (int j = 0; j < N; j++) {
			cin >> array[j];
			if (array[j] == j+1)
			{
				fixed[j] = true;
				nfixed++;
			}
			else
				fixed[j] = false;
		}
		
		int times = 0;
		
		while (nfixed < N) 
		{
			for (int j = 0, k = 0; j < N; j++) 
			{
				if (fixed[j] == false) 
				{
					nfarray[k] = array[j];
					index[k++] = j+1;
				}
			}
			
			bool b = true;
			//for (int j = 2; j < N-nfixed-1 && b == true; j++) 
			int j = 2;
			do 
			{
				for (int l = 0; l <= N-nfixed-j; l++) 
				{
					bool foundpair = true;
					for (int m = l; m < l + j; m++) 
					{
						if (nfarray[m] < index[l] || nfarray[m] > index[l+j-1])
						{
							foundpair = false;
							break;
						}
					}
					if (foundpair == true)
					{
						for (int m = l; m < l + j; m++) 
							fixed[index[m]-1] = true;
						nfixed += j;
						times += j;
						b = false;
						break;
					}
				}
				
				j++;
				
			}while (j <= N-nfixed && b == true);
		}
		
		
		cout << "Case #" << i+1 << ": " << times << ".000000" << endl;
		
	}
	
	return 0;
}

