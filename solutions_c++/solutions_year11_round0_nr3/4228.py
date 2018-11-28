#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{
    int t=0,n,poss,ip,c=1,min,index;
    long long sum;
    string line;
    ifstream myinput;
    ofstream myoutput;
    myinput.open("C-large.in");
    myoutput.open("candy-output-large.in");
    if(myinput.is_open())
    {
        getline(myinput,line);
        for(int i=0;i<line.size();i++)
        {
            t=10*t+int(line[i])-48;
        }
        while(t--)
        {
            n=0;
            min=1000001;
            sum=0;
            getline(myinput,line);
            for(int i=0;i<line.size();i++)
            {
                n=10*n+int(line[i])-48;
            }
            
            int* num;
            num=new int[n];
            index=0;
            getline(myinput,line);
            for(int i=0;i<line.size();i++){
                if(line[i]==' '){num[index++]=ip; ip=0;}
                else ip=10*ip+int(line[i])-48;
            }
            num[index++]=ip; ip=0;
            poss=0;
            for(int i=0;i<n;i++){
                poss=(poss^num[i]);
                if(min>num[i]){min=num[i];}
                sum+=num[i];
            }
            if(poss!=0){
                myoutput<<"Case #"<<c<<": NO"<<endl;
            }    
            else{
                myoutput<<"Case #"<<c<<": "<<sum-min<<endl;
            }
            c++;
            delete[] num;
        }
    }
    return 0;
}
