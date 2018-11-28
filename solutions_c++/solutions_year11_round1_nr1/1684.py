
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
    std::ofstream fout("out.out");
	std::ifstream fin("in.in");
	
    int num;
    fin>>num;
    long n,pd,pg;
    for(int i = 1;i<=num;++i)
    {
        fout<<"Case #"<<i<<": ";
        fin>>n>>pd>>pg;
        if(pg == 100 && pd !=100)
        {
            fout<<"Broken"<<endl;
            continue;
        }
        if(pg ==0 && pd != 0)
        {
            fout<<"Broken"<<endl;
            continue;
        }
        if(n>=100)
        {
            fout<<"Possible"<<endl;
            continue;
        }
        bool flag = false;
        for(int i = 1;i<=n;++i)
        {
            if((i*pd)%100 == 0)
            {
                fout<<"Possible"<<endl;
                flag = true;
                break;
            }

        }
        if(flag) continue;
        fout<<"Broken"<<endl;
    }
    fin.close();
	fout.close();
	return 0;
}
