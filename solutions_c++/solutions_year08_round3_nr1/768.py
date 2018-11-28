#include <stdio.h>
#include <iostream>
#include <list>

using namespace std;

void readcase(FILE* fp, int caseno);

int main(int argc, char* argv[])
{
    FILE* fp;
    char buff[256];
    int N;

    if(argc < 2)
    {
	cout << "no input" << endl;
	return 1;
    }
    fp = fopen(argv[1], "r");

    fgets(buff, 255, fp);
    sscanf(buff, "%d", &N);
    for(int i=0; i<N; i++)
    {
	readcase(fp, i+1);
    }
    fclose(fp);

    return 0;
}

void readcase(FILE* fp, int caseno)
{
    char buff[256];
    int P, K, L, let, i;
    list<int> letters;
    list<int>::reverse_iterator riter;

    int total = 0;

    fgets(buff, 255, fp);
    sscanf(buff, "%d %d %d", &P, &K, &L);

    for(i=0; i<L; i++)
    {
	fscanf(fp, "%d", &let);
	letters.push_back(let);
    }
    letters.sort();

    for(i=0, riter=letters.rbegin(); riter != letters.rend(); riter++, i++)
    {
	int weight = (int)(i / K) + 1;
	total += (weight * (*riter));
	//cout << weight << " * " << (*riter) << endl;
    }

    cout << "Case #" << caseno << ": " << total << endl;

    // read EOL
    fgets(buff, 255, fp);
}


