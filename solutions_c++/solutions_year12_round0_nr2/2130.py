#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	ifstream infile;
	ofstream outfile;
        int T,N,S,p,j=1,count=0,q;
        int *nums;

	infile.open("Input.txt", ios::in);
	outfile.open("Output.txt", ios::out);
        infile>>T;
        for (q=0;q<T;q++)
        {
            count=0;
            infile>>N>>S>>p;
            nums=new int[N];
            for (int i=0;i<N;i++)
                infile>>nums[i];
            for (int i=0;i<N;i++)
            {
                if (nums[i]>3*(p-1))
                {
                        count++;
                }
                else if ((S>0) && (nums[i]>=p+(2*(p-2))) && p>1)
                {
                    count++;
                        S--;
                }
            }
            outfile<<"Case #"<<j<<": "<<count;
            if (T-1!=q)
                outfile<<endl;
            j++;
        }
	
	infile.close();
	outfile.close();
        return 0;
}


