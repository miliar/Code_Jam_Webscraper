#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char** argv)
{
    ifstream fin("C.in");
    ofstream fout("C.out");
    int N;
    vector<int> count;
    string msg = "welcome to code jam";
    
    fin >> N;
    for(int t = 1; t <= N; t++)
    {
        string text;
        count.clear();
        count.resize(msg.size());
        getline(fin, text);
        if(text.size() == 0) getline(fin, text);
        
        for(int i = 0; i < text.size(); i++)
        {
            vector<int> new_count(count);
            if(text[i] == msg[0])
            {
                new_count[0]++;
            }
            
            for(int j = 1; j < msg.size(); j++)
            {
                if(text[i] == msg[j])
                {
                    new_count[j] += count[j - 1];
                }
            }
            
            for(int j = 0; j < msg.size(); j++)
            {
                count[j] = new_count[j] % 10000;
            }
        }
        
        char answer[100];
        sprintf(answer, "%04d", count[msg.size() - 1]);
        fout << "Case #" << t << ": " << answer << endl;
    }
    
    fin.close();
    fout.close();
    return 0;
}