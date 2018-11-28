#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
struct CombineElements
{
    vector<char> a;
    vector<char> b;
    vector<char> c;
};
struct OpposedElements
{
    vector<char> a;
    vector<char> b;;
};
int main()
{
    ifstream input ("input.txt");
    ofstream output ("output.txt");
    int cases;
    input >> cases;
    for(int a = 0; a < cases; a ++)
    {
        CombineElements cElems;
        OpposedElements oElems;

        int C, D, N;
        input >> C;
        for(int b = 0; b < C; b++)
        {
            string stemp;
            input >> stemp;
            cElems.a.push_back(stemp[0]);
            cElems.b.push_back(stemp[1]);
            cElems.c.push_back(stemp[2]);


        }

        input >> D;
        for(int b = 0; b < D; b++)
        {
            string stemp;
            input >> stemp;
            oElems.a.push_back(stemp[0]);
            oElems.b.push_back(stemp[1]);

        }

        input >> N;
        string toInvoke;
        input >> toInvoke;

        string elementList = "";

        for(int i = 0; i < toInvoke.length(); i ++)
        {
            elementList += toInvoke[i];
            if(elementList.length() > 1)
            {
                bool combined = false;
                for(int j = 0; j < cElems.a.size(); j++)
                {
                    if((elementList[elementList.length()-1] == cElems.a[j]  && elementList[elementList.length()-2] == cElems.b[j])||(elementList[elementList.length()-1] == cElems.b[j] && elementList[elementList.length()-2] == cElems.a[j]))
                    {
                        string tmp = "";
                        for(int k = 0; k < elementList.length()-2; k++)
                        {
                            tmp+=elementList[k];
                        }
                        tmp += cElems.c[j];
                        elementList = tmp;
                        combined = true;
                    }
                }
                if(combined == false)
                {
                    for(int j = 0; j < oElems.a.size(); j ++)
                    {
                        if(elementList[elementList.length()-1] == oElems.a[j])
                        {
                            for(int k = 0; k < elementList.length()-1; k ++)
                            {
                                if(elementList[k] == oElems.b[j])
                                {
                                    elementList = "";
                                    break;
                                }
                            }
                        }
                        else if(elementList[elementList.length()-1] == oElems.b[j])
                        {
                            for(int k = 0; k < elementList.length()-1; k ++)
                            {
                                if(elementList[k] == oElems.a[j])
                                {
                                    elementList = "";
                                    break;
                                }
                            }
                        }

                    }
                }
            }
        }
        output << "Case #" << a + 1 << ":" << " [";
        if(elementList.length() == 0)
        {
            output << "]" << endl;
        }
        else
        {
            for(int n = 0; n < elementList.length(); n ++)
            {
                if(n ==elementList.length()-1)
                {
                    output << elementList[n];
                }
                else
                {
                    output << elementList[n] << ", ";
                }

            }
            output << "]"<< endl;
        }


    }
    return 0;
}
