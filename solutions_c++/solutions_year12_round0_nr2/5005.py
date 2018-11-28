#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    freopen("B-large.in" , "rt" , stdin);
    freopen("out-l-5.txt" , "wt" , stdout);
    //  4
//3 1 5 15 13 11
// 2 0 5 11 12
    int tCases;

    cin>>tCases;
    for(int k=0; k<tCases; k++)
    {
        int N;
        int S;
        int p;
        cin>>N>>S>>p;
        int r = 0;
        int *scores = new int[N];
        for(int i=0; i<N; i++)
        {
            cin>>scores[i];
           // if(scores[i] == 0)continue;
            int d = scores[i]/3;
            /*if(d >= p)
            {
                r++;
                //S--;
            }*/
            //else
            //{
                int q = scores[i]%3;
                if(q == 0)
                {
                    if(d >= p)r++;
                    else if(d+1 >= p && d-1 >= 0 && S>0)
                    {
                        r++;
                        S--;
                    }
                }
                else if(q == 1)
                {
                    if(d+1 >= p)r++;
                }
                else if(q == 2)
                {
                    if(d+1 >= p)r++;
                    else if(d+2 >= p && S>0)
                    {
                        r++;
                        S--;
                    }
                }
                /*
                if(scores[i]%3 == 1 || scores[i]%3 == 2)
                {
                    if(d+1 >= p)
                    {
                        r++;
                        continue;
                    }
                }
                if((scores[i]%3 == 2||scores[i]%3 == 0) && d+2 >= p && S>0)
                {

                    r++;
                    S--;
                }
                */
                //else if()
            //}
        }
        cout<<"Case #"<<(k+1)<<": ";
        cout<<r<<endl;
    }

    //cout << "Hello world!" << endl;
    return 0;
}
