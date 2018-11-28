#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
#define oo 1.0e9
typedef unsigned long long i64;

int main()
{
    int test_cases=0,dim[2],k,count,case_num=1;
    int poss;
    string line;
    ifstream myinput; ofstream myoutput;
    myinput.open("A-large.in");
    myoutput.open("output.txt");
    if(myinput.is_open())
    {
        getline(myinput,line);
        for(int i=0;i<line.size();i++)
        {test_cases=test_cases*10+int(line[i])-48;}
        
        while(test_cases--)
        {
            getline(myinput,line);
            dim[0]=0;
            dim[1]=0;
            k=0;
            for(int i=0;i<line.size();i++)
            {
                if(line[i]==' ') k++;
                else{
                    dim[k]=10*dim[k]+int(line[i])-48;
                }
            }
            count=0;
            string mat[dim[0]][dim[1]];
            for(int i=0;i<dim[0];i++)
            {
                getline(myinput,line);
                for(int j=0;j<line.size();j++)
                {
                    if(line[j]=='#'){ count++; mat[i][j]='#';}
                    else mat[i][j]='.';
                }
            }
            if(count%4!=0) myoutput<<"Case #"<<case_num<<": \nImpossible"<<endl;
            else{
                poss=1;
                for(int i=0;i<dim[0]-1;i++)
                {
                    for(int j=0;j<dim[1]-1;j++)
                    {
                        if(mat[i][j][0]=='#'){
                            if(mat[i][j+1][0]!='#' || mat[i+1][j][0]!='#' || mat[i+1][j+1][0]!='#') poss=0;
                        else{
                            mat[i][j]=char(47);
                            mat[i][j+1]=char(92);
                            mat[i+1][j]=char(92);
                            mat[i+1][j+1]=char(47);
                        }
                        }    
                        if(poss==0) break;
                    }
                    if(poss==0){
                        myoutput<<"Case #"<<case_num<<": \nImpossible"<<endl;
                        break;
                    }
                }
                if(poss==1)
                {
                    myoutput<<"Case #"<<case_num<<":\n";
                    for(int i=0;i<dim[0];i++)
                    {
                        for(int j=0;j<dim[1];j++)
                        {
                            myoutput<<mat[i][j][0];
                        }
                        myoutput<<"\n";
                    }
                }
            }
            case_num++;
        }
    }
    myoutput.close();
    system("pause");
    return 0;
}

