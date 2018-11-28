#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
typedef unsigned long long i64;
int main()
{
    int test_cases=0,ip[3],k,N,L,H,case_num=1,t,f[100];
    bool poss;
    string line;
    ifstream myinput; ofstream myoutput;
    myinput.open("C-small-attempt0.in");
    myoutput.open("output.txt");
    if(myinput.is_open())
    {
        getline(myinput,line);
        for(int i=0;i<line.size();i++)
        {test_cases=test_cases*10+int(line[i])-48;}
        while(test_cases--)
        {
            getline(myinput,line);
            ip[0]=ip[1]=ip[2]=k=0;
            for(int i=0;i<line.size();i++)
            {
                if(line[i]==' ') k++;
                else{
                    ip[k]=10*ip[k]+int(line[i])-48;
                }
            }
            N=ip[0];
            L=ip[1];
            H=ip[2];
            getline(myinput,line);
            if(L==1) myoutput<<"Case #"<<case_num<<": 1"<<endl;
            else{
                k=0;
                for(int i=0;i<N;i++)
                {f[i]=0;}
                for(int i=0;i<line.size();i++)
                {
                    if(line[i]==' '){k++;}
                    else{
                        f[k]=10*f[k]+int(line[i])-48;
                    }
                }
                
                t=L;
                while(t<=H){
                    poss=1;
                    for(int i=0;i<N;i++)
                    {
                        if(t%f[i]==0 || f[i]%t==0) continue;
                        else {poss=0; break;}
                    }
                    if(poss==false) t++;
                    else break;
                }
                if(poss==0) myoutput<<"Case #"<<case_num<<": NO"<<endl;
                else myoutput<<"Case #"<<case_num<<": "<<t<<endl;
            }            
            case_num++;
        }
    }
    myoutput.close();
    system("pause");
    return 0;
}

