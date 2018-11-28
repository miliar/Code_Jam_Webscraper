#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("3.out");
    ifstream fin("3.in");
	
      int numCase;
      fin >> numCase;
 //     cout<<"numCase= "<<numCase<<endl; 
      int numCandy; 
      int nowCandy; 
      int nowPatrickSum; 
      int nowSeanSum;
      int smallest; 
      
      for(int i=0; i<numCase; i++) {
	        fin>> numCandy;
//	        cout<<"numCase= "<<numCase<<", numCandy= "<<numCandy<<endl; 
	        nowPatrickSum=0; 
	        nowSeanSum=0; 
	        smallest=1000001; 
            for(int j=0;j<numCandy;j++){
                    fin>> nowCandy; 
//                    cout<<"numCase= "<<numCase<<", numCandy= "<<numCandy<<", nowCandy= "<<nowCandy<<endl; 
                    nowPatrickSum=(nowPatrickSum|nowCandy)-(nowPatrickSum&nowCandy); 
                    nowSeanSum+=nowCandy; 
                    if(nowCandy<smallest){smallest=nowCandy;}
//                    cout<<"nowPatrickSum= "<<nowPatrickSum<<", nowSeanSum="<<nowSeanSum<<", smallest="<<smallest<<endl; 
            } 
      
      if(nowPatrickSum!=0){fout<<"Case #"<<i+1<<": NO"<<endl;} 
      else{fout<<"Case #"<<i+1<<": "<<nowSeanSum-smallest<<endl;} 
 
      }
	
	
	

	
    system("PAUSE");
    return EXIT_SUCCESS;
}
