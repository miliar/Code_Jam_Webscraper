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
    int test_cases=0,pd,pg,pd1,pow2,pow5,case_num=1,ip[3],k;
    i64 N,comp;
    string line;
    ifstream myinput;
    ofstream myoutput;
    myinput.open("A-large.in");
    myoutput.open("output.txt");
    if(myinput.is_open())
    {
        getline(myinput,line);
        for(int i=0;i<line.size();i++)
        {test_cases=test_cases*10+int(line[i])-48;}
        while(test_cases--)
        {
            ip[0]=ip[1]=ip[2]=k=0;
            getline(myinput,line);
            for(int i=0;i<line.size();i++)
            {
                if(line[i]==' '){k++;}
                else ip[k]=ip[k]*10+int(line[i])-48;
            }
                
            N=ip[0];
            pd=ip[1];
            pg=ip[2];
            cout<<N<<" "<<pd<<" "<<pg<<endl;
            if(N==0) myoutput<<"Case #"<<case_num<<": "<<"Broken"<<endl;
            else if(pd<100 && pg==100) myoutput<<"Case #"<<case_num<<": "<<"Broken"<<endl;
            else if (pd>0 && pg==0) myoutput<<"Case #"<<case_num<<": "<<"Broken"<<endl;
            else if(pd==100 && pg==100) myoutput<<"Case #"<<case_num<<": "<<"Possible"<<endl;
            else if(pd==0 && pg==0) myoutput<<"Case #"<<case_num<<": "<<"Possible"<<endl;
            else
            {
                pow2=pow5=0;
                pd1=pd;
                while(pd1%2==0){
                    pow2++;
                    pd1/=2;
                    if(pow2==2) break;
                }
                while(pd1%5==0){pow5++; pd1/=5;}
                comp=100;
                if(pow2>=2) comp=25; 
                else if(pow2==1) comp=50;
                if(pow5==2) comp/=25;
                else if(pow5==1) comp/=5;
                
                if(N<comp) myoutput<<"Case #"<<case_num<<": "<<"Broken"<<endl;
                else myoutput<<"Case #"<<case_num<<": "<<"Possible"<<endl;
            }
            case_num++;
        }
    }    
    myoutput.close();
    system("pause");
    return 0;
}
