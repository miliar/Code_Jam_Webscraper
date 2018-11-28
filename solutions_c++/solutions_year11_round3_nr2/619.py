#include <iostream>
#include <vector>
using namespace std;

unsigned long long int T, L, t, N, C;
int ct[1001];
double gain[1001];

int main(void)
{
	cin >> T;
	for(unsigned int numCase = 1; numCase <= T; numCase++)
	{
		cin >> L >> t >> N >> C;
		
		vector<int> st, at;
		int accum = 0;
		for(unsigned int i = 0; i < C; i++) cin >> ct[i];
		for(unsigned int i = 0, j = 0; i < N; i++)
		{	
			st.push_back(ct[j]);
			at.push_back(accum);
			accum += ct[j] * 2;
			
			j++;
			if(j == C) j = 0;
		}
		
		for(unsigned int i = 0; i < N; i++)
		{
			int aux = t - at[i];
			
			if(aux < 0) aux = 0;
			
			gain[i] = 2 * st[i] - (aux + (st[i] - aux / 2.0));
		}
		
		int total = 0;
		for(unsigned int i = 0; i < N; i++) total += 2 * st[i];
		
		for(unsigned int i = 0; i < L; i++)
		{
			int pos = 0;
			double maxg = -1;
			
			for(unsigned int j = 0; j < N; j++)
			{
				if(gain[j] > maxg)
				{
					pos = j;
					maxg = gain[j];
				}
			}
			
			total -= gain[pos];
			gain[pos] = -1;
		}
		
		cout << "Case #" << numCase << ": " << total << endl;
	}
}
