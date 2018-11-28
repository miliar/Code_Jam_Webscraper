#include<iostream>
#include<fstream>
#include<cstdlib>
#include<string>
using namespace std;

int queryNumber,Case,searchEngineNumber,result;
int main()
{
    ifstream FIN("input.txt");
    ofstream FOUT("output.txt");
    string searchEngine[100];
    int table[100][1001];
    char tmp[256];
    for(int i=0;i<100;i++) // initialize the table
    {
        table[i][0] = 0;
    }
    

    FIN >> Case;
    cout << Case << endl;
    for(int caseNumber=1;caseNumber<=Case;caseNumber++)
    {
        FIN >> searchEngineNumber;
        //cout << searchEngineNumber << endl;
        FIN.getline(tmp,256);        // get rid of line break
        for(int i=0;i<searchEngineNumber;i++)
        {
            FIN.getline(tmp,256);
            searchEngine[i] = tmp;
            //cout << searchEngine[i] << endl;
        }
        
        FIN >> queryNumber;
        //cout << queryNumber << endl;
        FIN.getline(tmp,256);        // get rid of line break
        for(int i=1;i<=queryNumber;i++)
        {
            FIN.getline(tmp,256);
            string query = tmp;
            //cout << query << endl;
            for(int j=0;j<searchEngineNumber;j++)
            {
                if(query == searchEngine[j])
                {
                    int min = 9999;
                    for(int k=0;k<searchEngineNumber;k++)
                        if(k!=j&&table[k][i-1]<min)
                            min = table[k][i-1];                
                    //cout << "min = " << min << endl;
                    table[j][i] = min + 1;
                }
                else
                {
                    table[j][i] = table[j][i-1];
                }
            }   
        }
        result=9999;
        for(int i=0;i<searchEngineNumber;i++)
        {
            cout << i << " : " << table[i][queryNumber] << endl;
            if(table[i][queryNumber]<result)
                result = table[i][queryNumber];
        }
        cout << "Case #" << caseNumber << ": " << result << endl;
        FOUT << "Case #" << caseNumber << ": " << result << endl;        
    
    }
    cin >> searchEngineNumber;
}
