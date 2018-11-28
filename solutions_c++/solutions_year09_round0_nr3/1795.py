#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

const char * toseek = "welcome to code jam";
const int dim = 19;

int Solve(const string& str)
{
    int res = 0;
    vector<int> countw(dim);
    for (int i=0;i < str.size();++i)
    {
        char c = str[i];
        switch (c)
        {
        case 'w':
            countw[1] = (countw[1]+1)%1000;
            break;
        case 'e':
            countw[2]= (countw[2]+countw[1])%1000;
            countw[7]= (countw[7]+countw[6])%1000;
            countw[15]= (countw[15]+countw[14])%1000;
            break;
        case 'l':
            countw[3]= (countw[3]+countw[2])%1000;
            break;
        case 'c':
            countw[4]= (countw[4]+countw[3])%1000;
            countw[12]= (countw[12]+countw[11])%1000;
            break;
        case 'o':
            countw[5]= (countw[5]+countw[4])%1000;
            countw[10]= (countw[10]+countw[9])%1000;
            countw[13]= (countw[13]+countw[12])%1000;
            break;
        case 'm':
            countw[6]= (countw[6]+countw[5])%1000;
            res= (res+countw[18])%1000;
            break;
        case ' ':
            countw[8]= (countw[8]+countw[7])%1000;
            countw[11]= (countw[11]+countw[10])%1000;
            countw[16]= (countw[16]+countw[15])%1000;
            break;
        case 't':
            countw[9]= (countw[9]+countw[8])%1000;
            break;
        case 'd':
            countw[14]= (countw[14]+countw[13])%1000;
            break;
        case 'j':
            countw[17]= (countw[17]+countw[16])%1000;
            break;
        case 'a':
            countw[18]= (countw[18]+countw[17])%1000;
            break;
        }
    }
    return res;
}

int main (int argc,char * argv[])
{
    int N;
    cin >> N;
    cin.ignore();
    for (int i=0;i < N;++i)
    {
        char buf[512];
        cin.getline(buf,512);
        string t (buf);
        cout << "Case #" << i+1 << ": " << setw(4) << setfill('0') << Solve(t) << endl;
    }
    return 0;
}

