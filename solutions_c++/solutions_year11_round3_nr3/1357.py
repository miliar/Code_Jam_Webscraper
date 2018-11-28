#include<vector>
#include<iostream>
#include<fstream>
#include<algorithm>

using namespace std;

long long int solve(vector<long long int> &F, long long int L, long long int H)
{
	for(long long int f = L; f <= H; f++){
		bool harmony = true;
		for(size_t i = 0; i < F.size(); i++){
			if(f < F[i]){
				if(F[i] % f > 0){
					harmony = false;
					break;
				}
			}
			else if(f > F[i]){
				if(f % F[i] > 0){
					harmony = false;
					break;
				}
			}
		}
		if(harmony)
			return f;
	}
	return 0;
}

int main(int argc, char *argv[])
{
	ifstream ifs(argv[1]);
	int T;
	ifs >> T;
	for(int x = 0; x < T; x++){
		size_t N;
		long long int L, H;
		ifs >> N >> L >> H;

		vector<long long int> F(N);
		for(size_t i = 0; i < N; i++)
			ifs >> F[i];

		long long int answer;
		answer = solve(F, L, H);
		cout << "Case #" << x + 1 << ": ";
		if(answer > 0)
			cout << answer;
		else 
			cout << "NO";
		cout << endl;
	}
	return 0;
}
