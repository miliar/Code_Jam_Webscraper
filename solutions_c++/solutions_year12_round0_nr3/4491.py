/*
*sigh, this is a bad code
*/
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <string>
#include <vector>
using namespace std;



int main()
{

    unsigned int testDataNum=0;
    unsigned int index=0;
    unsigned int pairNum=0;




    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    string spair_n;
    string spair_m;

    int ipair_n;
    int ipair_m;

    cin>>testDataNum;

    while( ++index <= testDataNum )
    {
        cin>>spair_n>>spair_m;

        stringstream pair_n(spair_n);
        pair_n>>ipair_n;
        stringstream pair_m(spair_m);
        pair_m>>ipair_m;

        for(int i=ipair_n ; i<ipair_m ; i++)
        {
            stringstream intTostr(spair_n);
            intTostr<<i;
            spair_n=intTostr.str();

            for( int j=0 ; j<spair_n.size()-1 ; j++)
            {
                string temp=spair_n.substr(1);
                temp+=spair_n[0];

                stringstream tempss(temp);
                int intTemp;

                tempss>>intTemp;

                if(intTemp>i && intTemp<=ipair_m  )
                {

                    pairNum++;
                }
                spair_n=temp;
            }
        }

        cout<<"Case #"<<index<<": "<<pairNum<<endl;
        pairNum=0;
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
