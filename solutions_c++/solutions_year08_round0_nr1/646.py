#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >>t;
    int caseNum=1;
    while (t--)
    {
        int aprNum=0;
        int s;
        int changeNum=0;
        cin >>s;
        string srcAng[100];
        getline(cin,srcAng[0]);
        for (int i=0;i<s;i++)
            getline(cin,srcAng[i]);
        int q;
        cin >>q;
        string query[1000];
        int qNum=0;
        getline(cin,query[0]);
        for (int i=0;i<q;i++)
        {
            getline(cin,query[qNum]);
            int numOfNotEqual=0;
            for (int j=0;j<s;j++)
                if (query[i]!=srcAng[j])
                    numOfNotEqual++;        
            if (numOfNotEqual!=s)
                qNum++;
        }
        //for (int i=0;i<qNum;i++)
            //cout <<i <<": " <<query[i] <<endl; //test
        int be=0;
        for (int i=0;i<qNum;i++)
        {
            //cout <<"No." <<i <<" " <<query[i] <<" is in queue" <<endl; //test
            //system("PAUSE");
                bool ifAprd=false;
                for (int j=be;j<i;j++)
                {
                    //cout <<"COMPARING with " <<j <<' ' <<query[j] <<endl; //test
                    if (query[i]==query[j])
                    {
                        ifAprd=true;
                        goto ne;
                    }
                }
                ne:
                if (!ifAprd)
                {
                    aprNum++;
                    //cout <<"aprNum changed to " <<aprNum <<endl;
                }
            if (aprNum==s)
            {
                aprNum=1;
                be=i;
                changeNum++;
            }
        }
        cout <<"Case #" <<caseNum <<": " <<changeNum <<endl;
        caseNum++;
    }
    return 0;
}
