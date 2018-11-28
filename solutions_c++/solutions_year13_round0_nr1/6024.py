//
//  main.cpp
//  Tic-Tac
//
//  Created by Tushar Singh on 4/12/13.
//  Copyright (c) 2013 Tushar Singh. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
using namespace std;

class file_op
{
    int case_no;
    ifstream infile ;
    ofstream outfile;
    void write_file(string);
    int opr(string a[4] );
    
public:
    void read_file();
    
};



void file_op::read_file()
{
    
    string line;
    
    //Variables final_line,med_line;
    int i=0;
    int result;
    
    infile.open ("/tmp/Input.in");
    outfile.open("/tmp/Output.in");
    if (infile.is_open())
    {
            getline (infile,line);
            case_no=  atoi(line.c_str());
            //i++;
        for(i=0;i<case_no;i++)
        {
            int l=0;
            string arg[4];
            do
            {
                getline (infile,line);
                arg[l]=arg[l]+line;
                l++;
            }while(l!=4);            
            getline (infile,line);


           //   cout<<"Case #"<<i+1<<"\n"<<arg[0]<<"\n"<<arg[1]<<"\n"<<arg[2]<<"\n"<<arg[3];
            //cout<<endl<<endl;
            result=opr(arg);
           // cout<<result;
            if(result==0)
            {
               write_file("Case #"+ to_string(i+1) +": Game has not completed"+"\n");
            }
            else if(result==1)
            {
                write_file("Case #"+ to_string(i+1) +": Draw"+"\n");
            }
            else if(result==2)
            {
                write_file("Case #"+ to_string(i+1) +": O won"+"\n");
            }
            else 
            {
                write_file("Case #"+ to_string(i+1) +": X won"+"\n");
            }
            //write_file("Case #"+ to_string(i++) +to_string(result)+"]\n");
           // cout<<result<<endl;
            
            

            
        }
       
        
    }
    else
    {
        cout << "Unable to open input file";
        
    }
    
    cout<<"\nDone!";
    infile.close();
    outfile.close();
    
}

int file_op::opr(string a[4] )
{
    
    int r=-1,row=0,col=0,diag=0,i=0;
    int flag=0,dot=0;
    for(row=0;row<4;row++)
    {
        if ((a[row].find_first_of("."))!=-1)
        {
            dot=1;
        }
        if((a[row].find_first_of("O"))!=-1)
        {
         if((a[row].find_first_of("X"))==-1 && ((a[row].find_first_of("."))==-1))
         {
             flag=1;
             r=2;
             row=5;
             
         }
        }
        else if((a[row].find_first_of("X"))!=-1)
        {
            if((a[row].find_first_of("O"))==-1 && ((a[row].find_first_of("."))==-1))
            {
                flag=1;
                 r=3;
                row=5;
               
            }
        }
        

        
    }
    if(flag==0)
    {
        for(col=0;col<4;col++)
        {
            string a_col;
            a_col.push_back(a[0][col]);
            a_col.push_back(a[1][col]);
            a_col.push_back(a[2][col]);
            a_col.push_back(a[3][col]);
            if((a_col.find_first_of("O"))!=-1)
            {
                if((a_col.find_first_of("X"))==-1 && ((a_col.find_first_of("."))==-1))
                {
                    flag=1;
                    r=2;
                    col=5;
                    
                }
            }
            else if((a_col.find_first_of("X"))!=-1)
            {
                if((a_col.find_first_of("O"))==-1 && ((a_col.find_first_of("."))==-1))
                {
                    flag=1;
                    r=3;
                    col=5;;
                    
                }
            }

            
        }
    }
    if(flag==0)
    {
        for(diag=0;diag<=3;diag=diag+3)
        {
            string a_diag;
            a_diag.push_back(a[0][abs(diag-0)]);
            a_diag.push_back(a[1][abs(diag-1)]);
            a_diag.push_back(a[2][abs(diag-2)]);
            a_diag.push_back(a[3][abs(diag-3)]);
            if((a_diag.find_first_of("O"))!=-1)
            {
                if((a_diag.find_first_of("X"))==-1 && ((a_diag.find_first_of("."))==-1))
                {
                    flag=1;
                    r=2;
                    diag=4;
                    
                }
            }
            else if((a_diag.find_first_of("X"))!=-1)
            {
                if((a_diag.find_first_of("O"))==-1 && ((a_diag.find_first_of("."))==-1))
                {
                    flag=1;
                    r=3;
                    diag=4;
                    
                }
            }
                        
        }
    }
    if(flag==0 && dot == 1)
    {
        return 0;
    }
    else if(flag==0)
    {
        return 1;
    }
    else{
    return r;
    }
}

void file_op::write_file(string s)
{
    if (outfile.is_open())
    {
        outfile<<s;
        
    }
    else
    {
        cout << "Unable to open file";
        
    }
}

int main(int argc, const char * argv[])
{
    string s;
    file_op f;
    f.read_file();
    return 0;
}


