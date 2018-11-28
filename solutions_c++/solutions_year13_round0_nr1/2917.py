#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void checkHorizontal(int  mat[4][4],bool & tokenX,bool & tokenO)
{
    for(int a=0;a<4;a++)
    {
        int counter=0;
        for(int b=0;b<4;b++)
        {
            counter+=mat[a][b];
            if(counter==4)
            {
                tokenX=true;
                break;
            }
            else if(counter==-4)
            {
                tokenO=true;
                break;
            }
        }
    }
}

void checkVertical(int  mat[4][4],bool & tokenX,bool & tokenO)
{
    for(int a=0;a<4;a++)
    {
        int counter=0;
        for(int b=0;b<4;b++)
        {
            counter+=mat[b][a];
            if(counter==4)
            {
                tokenX=true;
                break;
            }
            else if(counter==-4)
            {
                tokenO=true;
                break;
            }
        }
    }
}

void checkDiagonal(int  mat[4][4],bool & tokenX,bool & tokenO)
{
    int counter=0;
    for(int a=0;a<4;a++)
    {
        counter+=mat[a][a];
        if(counter==4)
        {
            tokenX=true;
        }
        else if(counter==-4)
        {
            tokenO=true;
        }
    }
    counter=0;
    for(int a=0;a<4;a++)
    {
        counter+=mat[3-a][a];
        if(counter==4)
        {
            tokenX=true;
        }
        else if(counter==-4)
        {
            tokenO=true;
        }
    }
//    int previous=0,counter=0;
//    for(int a=0;a<4;a++)
//    {
//        if(mat[a][a]!=0)
//        {
//            if(mat[a][a]==previous)
//            {
//                counter+=mat[a][a];
//                if(counter==4)
//                {
//                    tokenX=true;
//                }
//                else if(counter==-4)
//                {
//                    tokenO=true;
//                }
//            }
//            else
//            {
//                counter=mat[a][a];
//                previous=mat[a][a];
//            }
//        }
//        else
//        {
//            counter=mat[a][a];
//            previous=mat[a][a];
//        }
//    }
//    for(int a=0;a<4;a++)
//    {
//        if(mat[3-a][a]!=0)
//        {
//            if(mat[3-a][a]==previous)
//            {
//                counter+=mat[3-a][a];
//                if(counter==4)
//                {
//                    tokenX=true;
//                }
//                else if(counter==-4)
//                {
//                    tokenO=true;
//                }
//            }
//            else
//            {
//                counter=mat[3-a][a];
//                previous=mat[3-a][a];
//            }
//        }
//        else
//        {
//            counter=mat[3-a][a];
//            previous=mat[3-a][a];
//        }
//    }
}

int main ()
{
    vector<int> data;
    string line;
    ifstream infile ("/Users/diego/Desktop/Google Code Jam/ticTacToeTomek/data.in");
    ofstream outFile ("/Users/diego/Desktop/Google Code Jam/ticTacToeTomek/data.out");
    
    int cases;
    bool tokenX,tokenO,dotExists;
    
    if (infile.is_open() && outFile.is_open())
    {
        infile >> cases;
        for(int i=0;i<cases;i++)
        {
            //read
            dotExists=false;
            int matX[4][4]={0};
            int matO[4][4]={0};
            getline(infile, line);
            for(int j=0;j<4;j++)
            {
                getline(infile, line);
                for(int k=0;k<4;k++)
                {
                    if(line[k]=='.')
                    {
                        dotExists=true;
                        matX[j][k]=0;
                        matO[j][k]=0;
                    }
                    else if(line[k]=='X')
                    {
                        matX[j][k]=1;
                        matO[j][k]=1;
                    }
                    else if(line[k]=='O')
                    {
                        matX[j][k]=-1;
                        matO[j][k]=-1;
                    }
                    else //T
                    {
                        matX[j][k]=1;
                        matO[j][k]=-1;
                    }
                }
            }
            
            //find winners
            tokenX=false;
            tokenO=false;
            
            cout << "H" << endl;
            checkHorizontal(matX,tokenX,tokenO);
            cout << "X:" << tokenX << " O:" << tokenO << endl;
            checkHorizontal(matO,tokenX,tokenO);
            cout << "X:" << tokenX << " O:" << tokenO << endl;
            
            cout << "V" << endl;
            checkVertical(matX,tokenX,tokenO);
            cout << "X:" << tokenX << " O:" << tokenO << endl;
            checkVertical(matO,tokenX,tokenO);
            cout << "X:" << tokenX << " O:" << tokenO << endl;
            
            cout << "D" << endl;
            checkDiagonal(matX,tokenX,tokenO);
            cout << "X:" << tokenX << " O:" << tokenO << endl;
            checkDiagonal(matO,tokenX,tokenO);
            cout << "X:" << tokenX << " O:" << tokenO << endl;
            
            cout << "X:" << tokenX << " O:" << tokenO << endl;
            
            if(tokenX)
            {
                outFile << "Case #" << i+1 << ": X won" << endl;
            }
            else
            {
                if(tokenO)
                {
                    outFile << "Case #" << i+1 << ": O won" << endl;
                }
                else
                {
                    if(dotExists)
                    {
                        outFile << "Case #" << i+1 << ": Game has not completed" << endl;
                    }
                    else
                    {
                        outFile << "Case #" << i+1 << ": Draw" << endl;
                    }
                }
            }
        }
        
        infile.close();
        outFile.close();
    }
    else cout << "Unable to open file";
    
    return 0;
}