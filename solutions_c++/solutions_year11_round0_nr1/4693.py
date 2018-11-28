#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
#define ABS(X) ((X) > 0 ? (X) : (-(X)))
class Step
{
public:
    //true O   false B
    bool bot;
    int number;
};

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    
    int t;
    fin>>t;
    for(int times = 0 ; times < t;times++)
    {
        int result = 0;
        Step step[100];
        int count;
        fin>>count;
        for(int i=0;i<count;i++)
        {
            char a;
            int b;
            fin>>a>>b;
            if(a=='O')
                step[i].bot=true;
            else
                step[i].bot=false;
            step[i].number=b;
        }
        int posa=1;
        int posb=1;
        
        for(int i=0;i<count-1;i++)
        {
            for(int j=i+1;j<count;j++)
            {
                if(step[i].bot != step[j].bot)
                {
                    if(step[i].bot == true)
                    {
                        int next = ABS(step[i].number-posa)+1;
                        int moveb = step[j].number - posb;
                        if( ABS(moveb) < next)
                            posb = step[j].number;
                        else
                            if(moveb > 0)
                                posb += next;
                            else
                                posb -= next;
                    }
                    else
                    {
                        /*
                        int next = ABS(step[i].number-posb);
                        if(step[j].number - posa <= next)
                            posa = step[j].number+1;
                        else
                            posa += next+1;
                            */
                        
                        int next = ABS(step[i].number-posb)+1;
                        int movea = step[j].number - posa;
                        if( ABS(movea) < next)
                            posa = step[j].number;
                        else
                            if(movea > 0)
                                posa += next;
                            else
                                posa -= next;
                    }
                    break;
                }
            }
            if(step[i].bot == true)
            {
                result += ABS(step[i].number - posa) + 1;
                posa = step[i].number;
            }
            else
            {
                result += ABS(step[i].number - posb) + 1;
                posb = step[i].number;
            }
            //cout<<"a:"<<posa<<"  "<<"b:"<<posb<<endl;
        }
            if(step[count-1].bot == true)
            {
                result += ABS(step[count-1].number - posa) + 1;
            }
            else
            {
                result += ABS(step[count-1].number - posb) + 1;
            }
        
        fout<<"Case #"<<times+1<<": "<<result<<endl;
//        cout<<"Case #"<<times<<": "<<result<<endl;
    }


    return 0;
}
