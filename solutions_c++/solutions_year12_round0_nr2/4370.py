//
//  main.cpp
//  Codejam
//
//  Created by Phoom P. on 14/4/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    
    ifstream inFile;
    inFile.open("B-large.in");
    if (!inFile) {
        cerr << "Unable to open file";
        exit(1);   // call system to stop
    } 
    int cases,ans=0,i1,i2,i3;
    inFile >> cases;
    int temp=0,score=0,remain=0;
    for(int i=0;i<cases;i++){
        inFile>>i1;
        inFile>>i2;
        inFile>>i3;
        temp=0,score=0,remain=0;
        for(int a=0 ; a< i1;a++){
            inFile>>temp;
            score =temp/3;
            remain= temp-(3*score);
            
            if (score>=i3) {
                ans++;
            }
            else if (i3-score==1 && remain>0) {
                ans++;
            }
            else if (i3-score==1 && remain==0 && i2>0 && score!=0) {
                ans++; i2--;
            }
            else if (i3-score==2 && remain>1 && i2>0){
                ans++; i2--;
            }
        }

        
        
        
        
       cout <<"Case #"<<i+1<<": "<<ans<<"\n";
       
        ans=0;
    }
    inFile.close();
    return 0;
}

