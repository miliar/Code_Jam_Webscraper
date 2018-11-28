#define maxL 15
#define maxD 5000
#define maxN 500

#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

string str[maxD];
int L, D, N;

int main()
{
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("A-small-attempt1.out");
	//ifstream infile("A-large.in");
	//ofstream outfile("A-large.out");
	//ifstream infile("a.in");
	//ofstream outfile("a.out");
	infile>>L>>D>>N;
    for(int i = 0; i < D; i++)
    {
        infile>>str[i];
    }
    
    string s;
    string tempstr[maxL];
    int len, count;
    int num[maxL];
    for(int i = 0; i < N; i++)
    {
		infile>>s;
        len = s.length();
        memset(num, 0, sizeof(num));
        int lennum = 0;
        bool flag = false;
        for(int j = 0; j < maxL; j++)
        {
            tempstr[j] = "";
        }
        for(int j = 0; j < len; j++)
        {
            if(s[j] == '(')
            {
                flag = true;
            }
            else if(s[j] == ')')
            {
                flag = false;
                lennum++;
            }
            else if(flag)
            {
                num[lennum]++;
                tempstr[lennum] += s[j];
            }
            else if(!flag)
            {
                num[lennum] = 1;
                tempstr[lennum] = s[j];
                lennum++;
            }
        }
        count = 0;
        int j, k;
        for(int ii = 0; ii < D; ii++)
        {
	        for( j = 0; j < L; j++)
	        {
				for( k = 0; k < num[j]; k++)
				{
					if(str[ii][j] == tempstr[j][k])
						break;
				}
				if( k >= num[j] ) break;
			}
			if( j >= L ) count++;
		}
		outfile<<"Case #"<<i+1<<": "<<count<<endl;
	}
	infile.close();
    outfile.close();
    return 0;
}

		
