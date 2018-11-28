#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <vector>
#include <map>

using namespace std;

int FindMinSwitches(const vector<string>& engines, const vector<string>& queries)
{
    map<string, int> eng_map;
    map<string, int>::iterator msi;
    
    for (int i = 0; i < engines.size(); ++i)
        eng_map.insert(pair<string, int> (engines[i], 0));

    int num_switch = 0, unique_eng = 0;
    for (int i = 0; i < queries.size(); ++i)
    {
        msi = eng_map.find(queries[i]);
        if (msi != eng_map.end())
        {
            if (msi->second == 0)
            {
                msi->second = 1;
                unique_eng += 1;
            }
            if (unique_eng == engines.size())
            {
                num_switch += 1;
                unique_eng = 1;
                for (msi = eng_map.begin(); msi != eng_map.end(); ++msi)
                    msi->second = 0;
                eng_map[queries[i]] = 1;
            }
        }
        else
        {
            cout << "error found unknown query " << queries[i] << endl;
        }
    }

    return num_switch;
}

void ParseFile(const char* input_file, const char* output_file)
{
    vector<string> engines;
    vector<string> queries;

    /*engines.push_back("goog");
    engines.push_back("yahu");
    queries.push_back("goog");
    queries.push_back("yahu");
    queries.push_back("goog");

    cout << "Case #" << "1" << ": " << FindMinSwitches(engines, queries) << endl;
    return;*/
    ifstream in_file(input_file, ios_base::in);
    if (!in_file)
    {
        cerr << input_file << " copuld not be opened" << endl;
        return;
    }

    ofstream out_file(output_file, ios_base::out);
    if (!out_file)
    {
        cerr << output_file << " could not be opened" << endl;
        in_file.close();
        return;
    }

    int num_lines = 0, num_engines = 0, num_queries = 0;
    string line;
    getline(in_file, line);
    istringstream str_stream(line);
    str_stream >> num_lines;
    for (int i = 0; i < num_lines; ++i)
    {
        line.clear();
        engines.clear();
        queries.clear();
        getline(in_file, line);
        istringstream strm(line);
        strm >> num_engines;
        for (int j = 0; j < num_engines; ++j)
        {
            line.clear();
            getline(in_file, line);
            engines.push_back(line);
        }

        line.clear();
        getline(in_file, line);
        istringstream strm2(line);
        strm2 >> num_queries;
        for (int j = 0; j < num_queries; ++j)
        {
            line.clear();
            getline(in_file, line);
            queries.push_back(line);
        }

        out_file << "Case #" << (i+1) << ": " << FindMinSwitches(engines, queries) << endl;
    }

    in_file.close();
    out_file.close();

    return;
}

int main(int argc, const char** argv)
{
    if (argc != 3)
    {
        cerr << "Invocation: " << argv[0] << " <input_file> <output_file>" << endl;
        return 1;
    }

    ParseFile(argv[1], argv[2]);
    return 0;
}
