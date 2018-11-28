// Network -- Google Code Jam 2010 //
/*
Note : Nothing to say...
Alex
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
typedef signed long int sli;
typedef unsigned long int uli;

struct c // one case
{
    void Convert();
    void Print();
    bool CheckLine(uli i1,uli j1,uli j2, signed short int c);
    bool CheckRow(uli j1,uli i1,uli i2,signed short int c);
    uli MaxSize(uli i1, uli j1,uli size);
    void Cut(uli i1,uli j1, uli size);
    uli M,N;
    vector<signed short int> map;
    vector<string> H;
};

struct out
{
    void Add(uli Size);
    vector<uli> sizes;
    vector<uli> numbers;
};

void out::Add(uli s)
{
    if (sizes.empty())
    {
        numbers.push_back(1);
        sizes.push_back(s);
    }
    else
    {
        if (sizes.back() == s)
        {
            numbers.at(numbers.size()-1)++;
        }
        else
        {
            numbers.push_back(1);
            sizes.push_back(s);
        }
    }
}

uli c::MaxSize(uli i1,uli j1,uli size)
{
    //cout << "Maxsize "<<i1<<" "<<j1<<" "<<map.at(i1*N+j1)<<" "<<size<<endl;
    if (map.at(i1*N+j1) == 0 or map.at(i1*N+j1) == 1)
    {
        if (i1+size<M && j1+size<N)
        {
            //cout << "i1+size, j1+size : " << i1+size << " "<<j1+size <<endl;
            if (CheckLine(i1,j1,j1+size,-1) && CheckLine(i1+size,j1,j1+size,-1)
                && CheckRow(j1+size,i1,i1+size,-1) && CheckRow(j1,i1,i1+size,-1)) // one of these 4 test is useless
            {
                    return MaxSize(i1,j1,size+1);
            }
            else
                    return (size);
        }
        else
        {
            return (size);
        }
    }
    else
    {
        return 0;
    }
}

void c::Cut(uli i1, uli j1, uli size)
{
    for (uli i=i1;i<i1+size;i++)
    {
        for (uli j=j1;j<j1+size;j++)
        {
            map.at(j+i*N) = -1;
        }
    }
}

bool c::CheckLine(uli i1,uli j1,uli j2, signed short int c)
{
    if (c==-1)
    {
        return CheckLine(i1,j1+1,j2,map.at(j1+i1*N));
    }
    else
    {
        if (j1<=j2)
        {
            return ( ((1-c)==map.at(j1+i1*N)) && CheckLine(i1,j1+1,j2,map.at(j1+i1*N)) );
        }
        else
        {
            return true;
        }
    }
}

bool c::CheckRow(uli j1,uli i1,uli i2, signed short int c)
{
    if (c==-1)
    {
        return CheckRow(j1,i1+1,i2,map.at(j1+i1*N));
    }
    else
    {
        if (i1<=i2)
        {
            return ( ((1-c)==map.at(j1+i1*N)) && CheckRow(j1,i1+1,i2,map.at(j1+i1*N)) );
        }
        else
        {
            return true;
        }
    }
}


void c::Convert()
{
    for (uli j=0;j<M;j++) // For each line
    {
        for (uli k=0;k<N/4;k++)
        {
            if (H.at(j).at(k)=='0')
            {
                map.push_back(0);
                map.push_back(0);
                map.push_back(0);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='1')
            {
                map.push_back(0);
                map.push_back(0);
                map.push_back(0);
                map.push_back(1);
            }
            if (H.at(j).at(k)=='2')
            {
                map.push_back(0);
                map.push_back(0);
                map.push_back(1);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='3')
            {
                map.push_back(0);
                map.push_back(0);
                map.push_back(1);
                map.push_back(1);
            }
            if (H.at(j).at(k)=='4')
            {
                map.push_back(0);
                map.push_back(1);
                map.push_back(0);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='5')
            {
                map.push_back(0);
                map.push_back(1);
                map.push_back(0);
                map.push_back(1);
            }
            if (H.at(j).at(k)=='6')
            {
                map.push_back(0);
                map.push_back(1);
                map.push_back(1);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='7')
            {
                map.push_back(0);
                map.push_back(1);
                map.push_back(1);
                map.push_back(1);
            }
            if (H.at(j).at(k)=='8')
            {
                map.push_back(1);
                map.push_back(0);
                map.push_back(0);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='9')
            {
                map.push_back(1);
                map.push_back(0);
                map.push_back(0);
                map.push_back(1);
            }
            if (H.at(j).at(k)=='A')
            {
                map.push_back(1);
                map.push_back(0);
                map.push_back(1);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='B')
            {
                map.push_back(1);
                map.push_back(0);
                map.push_back(1);
                map.push_back(1);
            }
            if (H.at(j).at(k)=='C')
            {
                map.push_back(1);
                map.push_back(1);
                map.push_back(0);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='D')
            {
                map.push_back(1);
                map.push_back(1);
                map.push_back(0);
                map.push_back(1);
            }
            if (H.at(j).at(k)=='E')
            {
                map.push_back(1);
                map.push_back(1);
                map.push_back(1);
                map.push_back(0);
            }
            if (H.at(j).at(k)=='F')
            {
                map.push_back(1);
                map.push_back(1);
                map.push_back(1);
                map.push_back(1);
            }
        }
    }
}

void c::Print()
{
    for (uli j=0;j<M;j++) // For each line
    {
        for (uli k=0;k<N;k++)
        {
            cout << map.at(k+N*j);
        }
        cout << endl;
    }
    cout << endl;
}

int main()
{
    string inputFileName; // Here is what we need
    string outputFileName;
    uli T;
    vector<c> cases;
    vector<out> output;

    cout << "Name of input file : "; // Asking for the input file
    cin >> inputFileName;

    ifstream iFile(inputFileName.c_str(), ios::in); // & trying to open it
    if(iFile)
    {
            string currentLine;
            cout << "Reading ..." << endl << endl;
            iFile >> T;
            cout << T << " cases will folow..."<<endl << endl;

            for (uli i=0;i<T;i++)
            {
                c currentCases;
                iFile >> currentCases.M >> currentCases.N;
                string Hex;
                for (uli j=0;j<currentCases.M;j++) // For each line
                {
                    iFile >> Hex;
                    currentCases.H.push_back(Hex);
                }
                cases.push_back(currentCases);
            }
        iFile.close();

        cout << "Processing..." << endl;


        for (uli c_count=0;c_count<T;c_count++)  // For each cases
        {
            cout << "Case : " << c_count+1 <<endl;
            c currentCases;
            currentCases = cases.at(c_count);
            out answer;

            currentCases.Convert();
            currentCases.Print();

            bool exit=true;
            uli currentMax=0;
            uli currentSize=0;
            uli iCurrent=1024;
            uli jCurrent=1024;
            while (exit)
            {
                currentMax=0;
                iCurrent=1024;
                jCurrent=1024;
                for (uli i=0;i<currentCases.M;i++)
                {
                    for (uli j=0;j<currentCases.N;j++)
                    {
                        currentSize = currentCases.MaxSize(i,j,1);
                        //cout <<"CurrentSize : "<< currentSize <<endl;
                        if (currentSize > currentMax)
                        {
                            currentMax = currentSize;
                            iCurrent = i;
                            jCurrent = j;
                        }
                    }
                }
                //cout << "Max : " << currentMax<<endl;
                if (currentMax > 0)
                {
                    currentCases.Cut(iCurrent,jCurrent,currentMax);
                    answer.Add(currentMax);
                }
                else
                {
                    exit = false;
                }
            }

            output.push_back(answer);
        }


        cout << "Name of output file : ";   // Asking for output file
        cin >> outputFileName;

        ofstream oFile(outputFileName.c_str(), ios::out | ios::trunc);
        if(oFile)
        {
                out currentAnswer;
                for (uli i=0;i<cases.size();i++)
                {
                    currentAnswer = output.at(i);
                    oFile << "Case #" << i+1 << ": " << currentAnswer.sizes.size() << endl;
                    for (uli k=0;k<currentAnswer.sizes.size();k++)
                    {
                        oFile << currentAnswer.sizes.at(k) << " " << currentAnswer.numbers.at(k) << endl;
                    }
                }

                oFile.close();
        }
        else
        {
            cout << "Unable to open the output file : " << outputFileName.c_str() << endl;
        }


    }
    else
    {
         cout << "Unable to open the input file : " << inputFileName.c_str() << endl;
    }


    cout << "Exiting ..." << endl;
    return 0;
}
