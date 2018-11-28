#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <malloc.h>
#include <string.h>

using namespace std;

int iComb(int,int,int);
void print(int);
vector< vector< int> > vPosTab;
string sFind="welcome to code jam";

int main()
{
    int iCases,iIndex=0;
    cin>>iCases;
    char flush[10];
    cin.getline (flush,1);
    
    
    
       
    while(iIndex<iCases)
    {
                        char sG[500];

              int k=0;
              char c;
              char d = '\n';

                cin.getline (sG,500);

            string sGiven;
            string::iterator p;
            p=sGiven.begin();
            for(int i =0;sG[i]!='\0';i++)
            {
                    sGiven=sGiven+sG[i];
                    
            }
                        
                        
                        
                        
                        
                        

          
          vector<int> vPos;
          
          int j,i=-1;

          for(int iIndex1=0;iIndex1<sFind.size();iIndex1++)
          {
            
            if(iIndex1!=0)
            {
                          i=vPosTab[iIndex1-1][0];
            }
            
            while(1)
            {
                            j = sGiven.find(sFind[iIndex1],i+1);
                            if(j!=string::npos)
                            {
                                               vPos.push_back(j);
                                               i=j;
                            }
                            else
                            {
                             
                          
                                vPosTab.push_back(vPos);
                                vPos.clear();
                                break;
                            }
            }
          }
          
          int iOccurence=0;
          iOccurence=iComb(0,-1,iOccurence);

          cout<<"Case #"<<iIndex+1<<": ";
          print(iOccurence%10000);
          cout<<endl;
          vPosTab.clear();
          iIndex++;
                  
          
    }    
}

void print(int iOcc)
{
          cout<<iOcc/1000;
          iOcc=iOcc%1000;
          cout<<iOcc/100;
          iOcc=iOcc%100;
          cout<<iOcc/10;
          iOcc=iOcc%10;
          cout<<iOcc;
          return;
}
int iComb(int iRow,int iMinIndex,int iOccurence)
{
 
    for(int k=0;k<vPosTab[iRow].size();k++)
    {
            if(vPosTab[iRow][k]>iMinIndex)
            {
                if(iRow==sFind.size()-1)
                {
                     iOccurence++;
                }
                else
                {
                    iMinIndex=vPosTab[iRow][k];
                    iOccurence=iComb(iRow+1,iMinIndex,iOccurence);
                }
            }
    }
    return iOccurence;
}
                    


    

