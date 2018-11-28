#include <fstream>
#include <vector>
using namespace std;

vector <char> combine1;
vector <char> combine2;
vector <char> combine3;
vector <char> oppose1;
vector <char> oppose2;

void checkOppose(vector <char>& answer)
{
    if(answer.size() == 1) return;
    char element = answer[answer.size()-1];
	for(int i=0; i<answer.size()-1; i++)
	{
		for(int j=0; j<oppose1.size(); j++)
		{
			if(oppose1[j] == answer[i])
				if(oppose2[j] == element)
				{
					answer.clear();
					return;
				}
                        if(oppose2[j] == answer[i])
				if(oppose1[j] == element)
				{
					answer.clear();
					return;
				}
		}
	}
}

void checkCombine(vector <char>& answer, char element)
{
		answer.push_back(element);
		if(answer.size() == 1) return;
        for(int i=0; i<combine1.size(); i++)
        {
            if(answer[answer.size()-1] == combine1[i])
            {
                if(answer[answer.size()-2] == combine2[i])
                {
                    answer.pop_back();
                    answer.pop_back();
                    answer.push_back(combine3[i]);
                }
            }
            if(answer[answer.size()-2] == combine1[i])
                if(answer[answer.size()-1] == combine2[i])
                {
                    answer.pop_back();
                    answer.pop_back();
                    answer.push_back(combine3[i]);
                }
        }
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int testcases;
	vector < vector <char> > answer;
	fin >> testcases;
	while(testcases--)
	{
		int combine, oppose, invoke;
		vector <char> final;
		fin >> combine;
		while(combine--)
		{
			char temp;
			fin >> temp;
			combine1.push_back(temp);
			fin >> temp;
			combine2.push_back(temp);
			fin >> temp;
			combine3.push_back(temp);
		}
                fin >> oppose;
                while(oppose--)
                {
                       char temp;
                       fin >> temp;
                       oppose1.push_back(temp);
                       fin >> temp;
                       oppose2.push_back(temp);
                }
                fin >> invoke;
                while(invoke--)
                {
        	        char temp;
                        fin >> temp;
                        checkCombine(final, temp);
                        checkOppose(final);

                }
                combine1.clear();
                combine2.clear();
                combine3.clear();
                oppose1.clear();
                oppose2.clear();
                answer.push_back(final);
        }
	for(int i=0; i<answer.size(); i++)
	{
		fout << "Case #" << i+1 << ": [";
		for(int j=0; j<answer[i].size(); j++)
		{
			fout << (answer[i])[j];
			if(j+1 < answer[i].size()) fout << ", ";
		}
		fout << "]" << endl;
	}
	return 0;
}
