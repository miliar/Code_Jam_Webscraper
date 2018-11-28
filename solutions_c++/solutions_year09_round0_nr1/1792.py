#include <iostream> 
#include <fstream> 
#include <string>
#include <vector>   

using namespace std;

const char file_in[] = "A-large.in";
const char file_out[] = "A-large.out";

struct Tokens
{
    int L;
    int D;
    int N;
};


int main()
{
    ofstream output; 
    ifstream input;
    Tokens tokens; 
    string test;

    input.open(file_in);
    output.open(file_out);
    if(input.fail())
    {
        cout<<"Open file error!"<<endl;
    }
    
    input>>tokens.L>>tokens.D>>tokens.N;

    char **alien;   
    alien = new char*[tokens.D];   
    for(int i=0;i<tokens.D;i++)
    {   
        alien[i] = new char[tokens.L];   
    }

    for(i=0;i<tokens.D;i++)
    {       
        input>>alien[i];
        //cout<<alien[i]<<endl;
    }
    
    for(int n=0; n<tokens.N; n++)
    {
        test.empty();
        input>>test;
        //cout<<test;

        bool flag = false;
        int found = 0;   //find case counter

        string *str = new string[tokens.L];
        int l = 0;
        int len = test.length();
        for(int j=0; j<len; j++)
        {
            if(test.at(j) == '(')
            {
                flag = true;
                continue;
            
            }

            if(test.at(j) == ')')
            {
                flag = false;
                l++;
                continue;
            }

            if(flag)
            {
                str[l] += test.at(j);
            }
            else
            {         
                str[l] += test.at(j);
                l++;
            }
        }

        for(i=0; i<tokens.D; i++)
        {
            flag = true;
            for(j=0 ; j<tokens.L; j++)
            {
                if( string::npos == str[j].find(alien[i][j]))
                {
                    flag = false;
                    break;
                }
            }
            if(flag)
            {
                found++;
            }
        }
        output<<"Case #"<<n+1<<": "<<found<<endl;
        delete[] str; 
    }
    delete[] alien;
    input.close();
    output.close();

    //system("PAUSE");
    return 0;
}
