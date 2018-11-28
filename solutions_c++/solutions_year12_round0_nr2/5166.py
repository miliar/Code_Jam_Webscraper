#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
    int T, S, p, N;
    vector<int> score;
    int count;
    ifstream cin(argv[1]);
    ofstream cout("outB.txt");
    cin >> T;
    for(int t = 0; t < T; t++)
    {
	count = 0;
	cin >> N >> S >> p;
	score.resize(N);
	for(int i = 0; i < N; i++)
	    cin >> score[i];
	
	for(int i = 0; i < N; i++)
	{
	    if(score[i] >= (3 * p -2))
		count++;
	    else if(((score[i] == (3*p-3)) || (score[i] == (3*p-4))) && S)
	    {
		if(p-2 >=0)
		{
		    count++;
		    S--;
		}
	    }
	}
	cout << "Case #" << t+1 << ": " << count << endl;
    }
    return 0;
}
