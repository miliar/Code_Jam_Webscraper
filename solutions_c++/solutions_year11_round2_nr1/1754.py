#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
 #include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("1.out");
    ifstream fin("1.in");
	
      int numCase;
      int n;
      fin >> numCase;
      char a[100][100];
      double wp[100];
      double owp[100];
      double oowp[100];
      
      
      
      int match[100];
      int win[100];
  //    cout<<"array build"<<endl;
      
      for(int i=0; i<numCase; i++) {
	         fin>>n;
	     //    cout<<"N="<<n<<endl;
	         for(int j=0; j<n;j++){
					win[j]=0;
					match[j]=0;
					wp[j]=0;
			      	for(int k=0; k<n;k++){
			      		  fin>>a[j][k];
			      	//	  cout<<"a["<<j<<"]["<<k<<"] fin="<<a[j][k]<<endl;	
			      		  if(a[j][k]=='0'){match[j]++;}
			      		  else if(a[j][k]=='1'){match[j]++;win[j]++;}
			 
			        }
					wp[j]=double(win[j])/double(match[j]);	
					 //cout<<"win[j]="<<win[j]<<", match[j]="<<match[j]<<endl; 
					 //cout<<"wp["<<j<<"] ="<<wp[j]<<endl;		 
			 }
	        
	
	         for(int j=0; j<n;j++){
					owp[j]=0;
			      	for(int k=0; k<n;k++){
                           if(a[j][k]=='0'){owp[j]+=double(win[k]-1)/double(match[k]-1);}
                           else if(a[j][k]=='1'){owp[j]+=double(win[k])/double(match[k]-1);}
		 
			        }
					owp[j]=double(owp[j])/double(match[j]);
					//cout<<"owp["<<j<<"] ="<<owp[j]<<endl;		
			 }
			 
	         for(int j=0; j<n;j++){
					oowp[j]=0;
			      	for(int k=0; k<n;k++){
						   
                           if(a[j][k]=='0'){oowp[j]+=owp[k];
						   //cout<<"Calculating oowp: owp["<<j<<"] ="<<owp[j]<<endl;
						   }
                           else if(a[j][k]=='1'){oowp[j]+=owp[k];
						   //cout<<"oowp["<<j<<"] ="<<oowp[j]<<endl;	
						   }
                           	
		 
			        }
					oowp[j]=double(oowp[j])/double(match[j]);	
					//cout<<"oowp["<<j<<"] ="<<oowp[j]<<endl;	
			 }			 
	


      fout<<"Case #"<<i+1<<": "<<endl;
	         for(int j=0; j<n;j++){
                  fout<<fixed << setprecision(12) << double(0.25)*wp[j]+double(0.5)*owp[j]+double(0.25)*oowp[j]<<endl;	
			 }
  
      }
	
	
	

	
    system("PAUSE");
    return EXIT_SUCCESS;
}
