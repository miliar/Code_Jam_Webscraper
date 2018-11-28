#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<int> sort(vector<int> set);
vector<vector<int> > makeBinary(vector<int> set);
vector<int> add(vector<vector<int> > binaries);
int sumVector(vector<int> RS);
bool compareTallies(vector<int> LS, vector<int> RS);
bool checkAllZeros(vector<int> tally);
int main()
{
    ifstream input ("input.txt");
    ofstream output ("output.txt");

    int cases;
    input >> cases;

    for(int a = 0; a < cases; a ++)
    {
        int nums;
        input >> nums;
        vector<int> set;
        vector<int> origset;
        for(int b = 0; b < nums; b++)
        {
            int tempI;
            input >> tempI;
            set.push_back(tempI);
        }
        if(set.size() == 2)
        {
            if(set[0] == set[1])
            {
                output << "Case #" << a+1 <<": " <<set[0] << endl;
            }
            else
            {
                output << "Case #" << a +1<<": " <<"NO" <<endl;
            }

        }
        else
        {
            set = sort(set);
            origset = set;
            vector<vector<int> > binaries = makeBinary(set);

            vector<int> tally = add(binaries);


            //check if all tally
            int location;
            if(checkAllZeros(tally))
            {




                int finalTally = 0;
                for(int n = 0; n < origset.size()-1; n++)
                {
                    finalTally+=origset[n];
                }

                output << "Case #" << a+1 <<": " <<finalTally << endl;
            }
            else
            {
                output << "Case #" << a +1<<": " <<"NO" <<endl;
            }
        }



    }
    return 0;
}
vector<int> sort(vector<int> set)
{
    bool changed = true;
    while(changed == true)
    {

    changed = false;
        for(int x = 0 ; x < set.size()-1; x ++)
        {
            if(set[x] < set[x+1])
            {
                int temp = set[x];
                set[x] = set[x+1];
                set[x+1] = temp;
                changed = true;
            }
        }
    }
    return set;



}

vector<vector<int> > makeBinary(vector<int> set)
{
    vector<vector<int> > binaries;
    vector<vector<int> > backBinaries;
    int longestLength = 0;
    for(int x = 0; x < set.size(); x ++)
    {
        vector<int> bckWrds;
        while(set[x] !=0)
        {
            bckWrds.push_back(set[x] %2);
            set[x] = set[x]/2;
        }
        backBinaries.push_back(bckWrds);
        if(bckWrds.size() > longestLength)
        {
            longestLength = bckWrds.size();
        }


    }
    for(int x = 0; x < backBinaries.size(); x ++)
    {
        while(backBinaries[x].size() < longestLength)
        {
            backBinaries[x].push_back(0);
        }


    }
    for(int x = 0; x < backBinaries.size(); x ++)
    {
        vector<int> frwrds;
        for(int y = backBinaries[x].size()-1; y >= 0 ; y --)
        {
            frwrds.push_back(backBinaries[x][y]);
        }
        binaries.push_back(frwrds);


    }


    return binaries;
}
vector<int> add(vector<vector<int> > binaries)
{
    vector<int> tally;
    for(int x = 0; x < binaries[0].size() ; x++)
    {
        tally.push_back(0);
    }
    for(int x = 0; x < binaries.size(); x ++)
    {
        for(int y = 0; y < binaries[x].size(); y ++)
        {
            if(tally[y] == 0 && binaries[x][y] == 0 || tally[y] == 1 && binaries[x][y] == 1)
            {
                tally[y] = 0;
            }
            else
            {
                tally[y] = 1;
            }
        }
    }
    return tally;
}

bool checkAllZeros(vector<int> tally)
{
    bool zeros = true;
    for(int x = 0; x < tally.size(); x ++)
    {
        if(tally[x] != 0)
        {
            zeros = false;
        }
    }
    return zeros;
}

bool compareTallies(vector<int> LS, vector<int> RS)
{
    bool match = true;
    for(int x = 0; x < LS.size(); x ++)
    {
        if(LS[x] != RS[x])
        {
            match = false;
        }

    }
    return match;

}

int sumVector(vector<int> RS)
{
    int tally= 0;
    for(int x = 0; x < RS.size(); x ++)
    {
        tally += RS[x];
    }
    return tally;
}
