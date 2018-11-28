#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{


long long int caseNumber;


char c[36][3];
char d[28][2];
char totalN[105];
int totalN_size;
int cCase, dCase, n;
char nowN;

ofstream fout("1.out");
ifstream fin("1.in");
fin >> caseNumber;


for(int i=0; i<caseNumber; i++) {
      for(int j=0;j<36;j++){
			c[j][1]=0;
			c[j][2]=0;
			c[j][3]=0;
			}
      for(int j=0;j<28;j++){
			d[j][1]=0;
			d[j][2]=0;
			}
			
	  fin>>cCase;
      for(int j=0;j<cCase;j++){
			fin>>c[j][1]>>c[j][2]>>c[j][3];
			}	  
	  
	  fin>>dCase;
      for(int j=0;j<dCase;j++){
			fin>>d[j][1]>>d[j][2];
			}
			
	  fin>>n;
	  totalN_size=0;
	  
//	cout<<"Current cCase: "<<cCase<<", current dCase: "<<dCase<<", n="<<n<<endl;	  
      for(int j=0;j<n;j++){
			fin>>nowN;
//			cout<<"Current input: "<<nowN<<", current total: "<<totalN<<endl;
			for(int k=0; k<cCase; k++){
					if((nowN==c[k][1])&&(totalN[totalN_size-1]==c[k][2])){totalN[totalN_size-1]=c[k][3];nowN=0;break;}
					else if((nowN==c[k][2])&&(totalN[totalN_size-1]==c[k][1])){totalN[totalN_size-1]=c[k][3];nowN=0;break;}
					
			}
			
			if(nowN!=0){
				for(int k=0; k<dCase; k++){				    
				    for(int m=0; m<totalN_size; m++){
					       	if(nowN==d[k][1]&&totalN[m]==d[k][2]){totalN_size=0;nowN=0;break;}
					       	else if(nowN==d[k][2]&&totalN[m]==d[k][1]){totalN_size=0;nowN=0;break;}
					}
			    }
		    }
		    
			if(nowN!=0){totalN[totalN_size]=nowN;totalN_size++;}	
	  }	  

      fout<<"Case #"<<i+1<<": [";
	  for(int j=0; j<totalN_size; j++){
			if(j==(totalN_size-1)){fout<<totalN[j];}
			else{fout<<totalN[j]<<", ";}
			}
	  fout<<"]"<<endl;
}
	
	
	
	
    system("PAUSE");
    return EXIT_SUCCESS;
}
