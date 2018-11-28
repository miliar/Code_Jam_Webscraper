#define maxL 15
#define maxD 25
#define maxN 10

#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

string str[maxD];
int L, D, N;

bool findstr(string tempstr)
{
    for(int i = 0; i < D; i++)
    {
        if( tempstr == str[i])
            return true;
    }
    return false;
}

int main()
{
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("A-small-attempt0.out");
    //cin>>L>>D>>N;
    infile>>L>>D>>N;
    for(int i = 0; i < D; i++)
    {
        //cin>>str[i];
        infile>>str[i];
    }

    string s;
    string tempstr[maxL];
    int len, count;
    int num[maxL];
    int tempnum[maxL];
    for(int i = 0; i < N; i++)
    {
        //cin>>s;
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

        /*for(int j = 0; j < L; j++)
        {
            cout << num[j] << ' ';
            cout << tempstr[j]<<endl;
        }*/
		s = "";
		lennum = 0;
		count = 0;
		memset(tempnum, 0, sizeof(tempnum));
        while(1)
        {
			if(tempnum[0] >= num[0])break;
			if( tempnum[lennum] >= num[lennum] )
			{
				tempnum[lennum-1]++;
				tempnum[lennum] = 0;
				s = "";
				lennum = 0;
			}
			s += tempstr[lennum][tempnum[lennum]];
			lennum++;
			if(lennum >= L)
			{
				//cout<<s<<endl;
				if(findstr(s)) count++;
				tempnum[lennum-1]++;
				s = "";
				lennum = 0;
			}	
		}
		//cout<<"Case #"<<i+1<<": "<<count<<endl;
		outfile<<"Case #"<<i+1<<": "<<count<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
