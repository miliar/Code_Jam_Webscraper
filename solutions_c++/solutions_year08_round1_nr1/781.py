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
    inFile.open("heck.in");
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
        int ans=80000001;
        vector<int>a1;
        vector<int>a2;
        getline(inFile,a);
        se=atoi(a.c_str());
        
        
        if(se==0)
        break;
        
        for(i=0;i<2;i++)
        {
            getline(inFile,a);
            stringstream iss;
            iss<<a;
            int m;
            while(iss>>m){
            if(i==0)
            a1.PB(m);
            else a2.PB(m);
           
            }
        }
        
        sort(ALL(a2));
        
        do{
            
            int sum=0;
            for(i=0 ;i<se;i++)
            {
                sum+=a1[i]*a2[i];
            }
            
            if(sum<ans)
            ans=sum;
        }while(next_permutation(ALL(a2)));

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
