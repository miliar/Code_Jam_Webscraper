#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int explode(string str, string delim, string *result);

int main(int argc, char **argv)
{
    ifstream iFile("input.txt");
    if(iFile.fail())
    {
        cout<<"Unable to open input file!"<<endl;
        exit(1);
    }
    
    char temp[1024];
    iFile.getline(temp, 1024);
    int rowNo = atoi(temp);
    
    ofstream oFile("output.txt");
    int tokCount = 0;
    int googlers = 0, surprises = 0, maxPoint = 0;
    for(int i = 0; i<rowNo; i++)
    {
        iFile.getline(temp, 1024);
        string input(temp);
        string result[512]="";
        
        tokCount = explode(input, " ", result);
        googlers = atoi(result[0].c_str());
        surprises = atoi(result[1].c_str());
        maxPoint = atoi(result[2].c_str());
        int maxPointGooglerCount = 0;
        //cout<<"G: "<<googlers<<" S: "<<surprises<<" M: "<<maxPoint<<endl;
        for(int j = 0; j<googlers; j++)
        {
            int totalPoints = atoi(result[j+3].c_str());
            int remainder = totalPoints%3;
            int points[3];
            fill_n(points, 3, (totalPoints - remainder)/3);
            switch(remainder)
            {
                case 0:
                    if(surprises>0)
                        if(points[0]<maxPoint && (maxPoint-points[0])==1)
                            if(points[1]>0)
                            {   points[0]+=1;
                                points[1]-=1;
                                surprises--;
                            }
                    break;
                case 1:
                    points[0]+=1;
                    break;
                
                case 2:
                    if(points[0]<maxPoint && (maxPoint-points[0])==2 && surprises>0)
                    {
                        points[0]+=2;
                        surprises--;
                    }
                    else
                    {
                        points[0]+=1;
                        points[1]+=1;
                    }
                    break;
                    
            case 3:
                if(points[0]<maxPoint && (maxPoint-points[0])==2 && surprises>0)
                {
                    points[0]+=2;
                    surprises--;
                }
                else if(points[1]<maxPoint && (maxPoint-points[1])==2 && surprises>0)
                {
                    points[1]+=2;
                    surprises--;
                }
                else
                {
                    points[0]+=1;
                    points[1]+=1;
                    points[2]+=1;
                }
                    break;
                    
            }
            if(points[0]>=maxPoint || points[1]>=maxPoint || points[2]>=maxPoint)
                maxPointGooglerCount++;
        }
        oFile<<"Case #"<<(i+1)<<": "<<maxPointGooglerCount<<endl;
    }
    
    oFile.close();
    iFile.close();
    return 0;
}

int explode(string str, string delim, string *result)
{
    char *token;
    char cStr[1024];
    int i = 0;
    strcpy(cStr, str.c_str());
    
    token = strtok(cStr, delim.c_str());
    while(token!=NULL)
    {
        result[i++] = token;
        token = strtok(NULL, delim.c_str());
    }
    return i;
}
