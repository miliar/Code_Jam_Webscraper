#include <map>
#include <vector>
#include <string>
#include <fstream>


bool findCombine(const std::map<std::string, char>& combine, std::string& input)
{
    bool change = false;
    if (input.size() >= 2)
    {
        std::string sub = input.substr(input.size() - 2, 2);

        std::map<std::string, char>::const_iterator fit = combine.find(sub);
        if (fit == combine.end())
        {
            sub.clear();
            sub = input[input.size() - 1];
            sub += input[input.size() - 2];
            fit = combine.find(sub);
        }

        if (fit != combine.end())
        {
            //input.erase(input.size() - 2, 2);
            input.resize(input.size() - 2);
            input += fit->second;
            change = true;
        }
    }
    return change;
}


void blackBox(const std::map<std::string, char>& combine
              , const std::vector<std::string>& oppose
              , const std::string& invoke
              , std::string& result)
{
    result.clear();
    const std::string::const_iterator endit = invoke.end();
    for ( std::string::const_iterator it = invoke.begin(); it != endit; ++it)
    {
        if (!result.empty())
        {
            // combine
            result += *it;
            while (findCombine(combine, result))
            {
                ;
            }
            //printf("%s\n", result.c_str());

            //oppose
            const std::vector<std::string>::const_iterator endit = oppose.end();
            for ( std::vector<std::string>::const_iterator it = oppose.begin(); it != endit; ++it)
            {
                if (result.find((*it)[0]) != std::string::npos && result.find((*it)[1]) != std::string::npos)
                {
                    result.clear();
                }
            }
        }
        else
        {
            result += *it;
        }
    }
    //printf("%s\n", result.c_str());
}

int main(void)
{

    //std::map<std::string, char> combine;
    //std::vector<std::string> oppose;
    //std::string invoke, result;

    //oppose.reserve(28); //0~28

    //combine["EE"] = 'Z';
    //oppose.push_back("QE");
    //invoke = "QEEEERA";

    //blackBox(combine, oppose, invoke, result);



    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");

    if (infile)
    {
        int testNum(0);
        infile >> testNum;

        std::map<std::string, char> combine;
        std::vector<std::string> oppose;
        std::string invoke, result;
        std::string tmp;

        int integer(0);

        for (int t = 0; t < testNum; ++t)
        {
            //combine
            infile >> integer;
            for (int i = 0; i < integer; ++i)
            {
                infile >> tmp;
                combine[tmp.substr(0, 2)] = tmp[2];
                tmp.clear();
            }
            //oppose
            infile >> integer;
            for (int i = 0; i < integer; ++i)
            {
                infile >> tmp;
                oppose.push_back(tmp);
                tmp.clear();
            }
            //invoke
            infile >> integer;
            infile >> invoke;

            blackBox(combine, oppose, invoke, result);


            outfile << "Case #" << t + 1 << ": [";
            for (int r = 0; r < static_cast<int>(result.size()); ++r)
            {
                if (r != 0)
                {
                    outfile << ", ";
                }
                outfile << result[r];
            }
            outfile << "]" << std::endl;

            combine.clear();
            oppose.clear();
            invoke.clear();
            result.clear();

        }
    }
    infile.close();
    outfile.close();

    system("pause");
    return 0;
}
