#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> visited;
vector<long> next;
vector<long> get;
bool looped;

long long calc(int index, long R, long k, const vector<long> &g)
{
    if(R == 0) return 0;
    long long result = 0;
    if(visited[index] && !looped)
    {
        looped = true;
        int loop_length = 0, tmp = index;
        long long loop_result = 0;
        do
        {
            loop_result += get[tmp];
            loop_length++;
            tmp = next[tmp];
        } while(tmp != index);
        result += loop_result * (R/loop_length);

        return result += calc(index, R%loop_length, k, g);
    }
    else
    {
        result += get[index];
        visited[index] = 1;
        return result + calc(next[index], R-1, k, g);
    }
}

int main()
{
	string file = "C-large";
	ifstream ifs((file+".in").c_str());
	ofstream ofs((file+".out").c_str());
	int num_of_problems;

	ifs >> num_of_problems;
    for(int problem=0; problem<num_of_problems; problem++)
	{
        //input
        long R, k, N;
        ifs >> R >> k >> N;
        vector<long> g(N);
        next.assign(N, -1);
        visited.assign(N, 0);
        get.resize(N);
        looped = false;
        for(int i=0; i<N; i++) visited[i] = 0;

        for(int i=0; i<N; i++) { ifs >> g[i]; }


        for(int i=0; i<N; i++)
        {
            int index = i;
            long sum = 0, sum_ = 0;
            do
            {
                sum += g[index];

                index = (index+1) % N;
                sum_ = sum + g[index];
            } while(index != i && sum_ <= k);

            next[i] = index;
            get[i] = sum;

        }

        long long result = 0;
        result += calc(0, R, k, g);
		

        //output
		ofs << "Case #" << problem+1 << ": " << result << endl;
		cout << problem << endl;
	}

	return 0;
}

