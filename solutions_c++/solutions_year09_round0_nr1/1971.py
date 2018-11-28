#define L 15
#define D 5000
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int cL=3,cD=5,cN=4;
    int i,j,k,l,m,n;
    ifstream input("input.txt");
    ofstream output("output.txt");
    char words[D][L];
    char possiblechars[L][26];
    char possibleindex[26];
    bool isValid;
    char temp;
    int validwords=0;
    input>>cL>>cD>>cN;
    for(i=0;i<cD;i++)
                     input>>words[i];
    for(i=0;i<cN;i++)
    {
                     
    for(j=0;j<cL;j++)
                     possibleindex[j]=0;
    
    j=0;
    temp=1;
    bool inbracket=false;
    while(j<cL)
    {
           input>>temp;
           if(temp=='(')
           {
                        inbracket=true;
                        
           }
           else if(temp==')')
           {
                inbracket=false;
                j++;
           }
           else if(inbracket==true)
           {
               possiblechars[j][possibleindex[j]++]=temp;
           }
           else
           {
               possiblechars[j][possibleindex[j]++]=temp;
               j++;
           }
    }
    validwords=0;
    for(j=0;j<cD;j++)
    {
                     isValid=true;
                     for(k=0;k<cL && isValid==true;k++)
                     {
                                      isValid=false;
                                      for(l=0;l<possibleindex[k];l++)
                                      {
                                                       if(words[j][k]==possiblechars[k][l])
                                                       {
                                                                                        isValid=true;
                                                                                        break;
                                                       }
                                      }
                     }
                     if(isValid==true)
                     {
                                      validwords++;
                     }
    }
    output<<"Case #"<<(i+1)<<": "<<validwords++<<"\n";
}
input.close();
output.close();  
    return 0;
}
