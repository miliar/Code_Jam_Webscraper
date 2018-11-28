#include <string>
#include <vector>
#include<iostream>
#include<map>
#include<sstream>
#include<set>
#include<cctype>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<functional>
#include<cmath>
#include<cstdlib>
// BEGIN CUT HERE
#include<conio.h>
#include<fstream>
// END CUT HERE

using namespace std;
#define F(i,n)  for( i=0; i<n; i++)


#define PB push_back
#define ALL(x) x.begin(),x.end()
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))


int main(){

int sum = 0,i,j;
int N=0;
int cas=0;
    int x;
    ifstream inFile;
    ofstream myfile;
    myfile.open ("out.in");
    inFile.open("test2.in");
    if (!inFile) {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }
    string a;
    getline(inFile,a);
    N=atoi(a.c_str());
    int mmm=0;
    if(N==0)
    return -1;
    while(1)
    {

        int se=0,nq=0;
        int ans=0;
        getline(inFile,a);
        se=atoi(a.c_str());
        //cout<<"sse = "<<se;
        if(se==0)
        break;
        map<string,int> as;
        vector<string>search;
        for(i=0;i<se;i++)
        {
            string sename ;
            getline(inFile,sename);
            //cout<<"se name = "<<sename;
            search.PB(sename);
            as[sename]=1;
        }
        getline(inFile,a);
        nq=atoi(a.c_str());
        //cout<<"nq = "<<nq;
        int cc=0;
        //cout<<"size = "<<search.size();
        for(i=0;i<nq;i++)
        {
            string query;
            getline(inFile,query);
            //cout<<"se name = "<<query;
            as[query]=2;
            cc=0;
            for(j=0;j<se;j++)
            {
                if(as[search[j]]==2)
                cc++;
            }
            if(cc==se){
                for(j=0;j<se;j++)
                {
                    as[search[j]]=1;
                }
                as[query]=2;
                ans++;
                
            }
        }
        
        
        //wor writting to a file
        cas++;
        myfile<<"Case #"<<cas<<": "<<ans<<"\n";
        mmm++;
        if(mmm==N)
        break;
     
    }


  inFile.close();
  myfile.close();
  
  
  
    getch();
    return 0;
}
