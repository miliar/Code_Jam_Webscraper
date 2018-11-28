#include <iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
    ifstream f_in("D:\\inp.txt");
    ofstream f_out("D:\\out.txt");
    int t;
    int c,d,n;
    f_in>>t;
    for(int itri=1;itri<=t;itri++)
    {
        f_in>>c;
        vector<string> com(c);
        for(int itr=0;itr<c;itr++)
        {
            f_in>>com[itr];
        }

        f_in>>d;
        vector<string> opp(d);
        for(int itr=0;itr<d;itr++)
        {
            f_in>>opp[itr];
        }

        string inp;
        f_in>>n;
        f_in>>inp;
        string res;
        res.push_back(inp[0]);
        int length=1;
        char temp1,temp2;
        int fg;

        for(int itr=1;itr<n;itr++)
        {
            fg=0;
            temp1=res[length-1];
            temp2=inp[itr];
            for(int itrj=0;itrj<c;itrj++)
            {
                if((temp1==com[itrj][0] && temp2==com[itrj][1]) || (temp1==com[itrj][1] && temp2==com[itrj][0]) )
                {
                    res[length-1]=com[itrj][2];
                    fg=1;
                    break;
                }
            }

            for(int itrj=0;itrj<d && fg==0;itrj++)
            {
                if(temp2==opp[itrj][0])
                {
                    temp1=opp[itrj][1];
                    for(int q=0;q<length;q++)
                    {
                        if(temp1==res[q])
                        {
                            res.clear();
                            length=0;
                            fg=2;
                            break;
                        }
                    }
                }
                else if(temp2==opp[itrj][1])
                {
                    temp1=opp[itrj][0];
                    for(int q=0;q<length;q++)
                    {
                        if(temp1==res[q])
                        {
                            res.clear();
                            length=0;
                            fg=2;
                            break;
                        }
                    }
                }
            }
            if(fg==0)
            {
                res.push_back(temp2);
                length++;
            }

        }
        f_out<<"Case #"<<itri<<": [";
        for(int itr=0;itr<length;itr++)
        {
            if(itr!=0)
            f_out<<", ";
            f_out<<res[itr];
        }
        f_out<<"]"<<endl;
    }
    return 0;
}
