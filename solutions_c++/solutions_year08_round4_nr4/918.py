// D.cpp
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

vector<int> permArr;

void AddPermutationArr(const int *v, const int size)
{
	if (v != 0) {
		for (int i = 0; i < size; i++)
			permArr.push_back(v[i]);
	}
}


void permute(int *v, const int start, const int n)
{  
  if (start == n-1) {
	AddPermutationArr(v, n);
  }
  else {
    for (int i = start; i < n; i++) {
      int tmp = v[i];
      
      v[i] = v[start];
      v[start] = tmp;
      permute(v, start+1, n);
      v[start] = v[i];
      v[i] = tmp;
    }
  }
}

void MakePermutationArr(int N)
{
	int* Value = new int[N];
	for (int i = 0; i < N; i++)
		Value[i] = i;
	permArr.clear();
	permute(Value, 0, N);
	delete Value;
}

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int N;
	cin >> N;
	for (int cnt = 1; cnt <= N; cnt++)
	{
		int k;
		cin >> k;
		MakePermutationArr(k);
		char S[60000];
		char S2[60000];
		cin >> S;
		int len = strlen(S) / k;
		long cnt2 = 0;
		long minResult = 1000000;
		while (permArr.size() > cnt2)
		{
			vector<int> pArr;
			for (int j = 0; j < k; j++)
				pArr.push_back(permArr[cnt2++]);
			char* ptrSrc = S;
			char* ptrDst = S2;
			long cnt3 = strlen(S) / k;
			for (int j = 0; j < cnt3; j++)
			{
				for (int bb = 0; bb < k; bb++)
					ptrDst[bb] = ptrSrc[pArr[bb]];
				ptrSrc += k;
				ptrDst += k;
			}
			S2[strlen(S)] = 0;
			long result = 1;
			char lastChar = S2[0];
			for (int j = 1; j < strlen(S2); j++)
			{
				if (S2[j] != lastChar)
				{
					result++;
					lastChar = S2[j];
				}
			}
			if (result < minResult)
				minResult = result;
		}
		cout << "Case #" << cnt << ": " << minResult << endl;
	}
}

