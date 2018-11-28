#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("2.out");
    ifstream fin("2.in");
	
      int numCase;
      int L,N,C;
      long long int t;
      int c[1000];
      long long int time;
      int max, max1, max2;
      int last;
      
      
      fin >> numCase;
      for(int i=0; i<numCase; i++) {
			

			
	         fin>>L>>t>>N>>C;
	         for(int j=0; j<C; j++){
			       fin>>c[j];		
			 }
			 
			 t=t/2;
			 
			 last=-1;
			 
			 int s=0;
			 while(t>0){		//after this, s=the first full star to consider
					
			    t-=c[s%C];
			    s++;		 
			 }
			 //cout<<"s= "<<s<<",t= "<<t<<endl;
			 
			 if(t==0){last=0;}                    		
			 else if(t<0){last=-t;}
			 //cout<<"-t= "<<-t<<"last= "<<last<<endl;   
			    
			    
		/*	   int key,i;
               for(int j=1;j<num;j++){
                    key=data[j];
                    i=j-1;
                    while(data[i]>key && i>=0){
                       data[i+1]=data[i];
                       i--;
                    }
                    data[i+1]=key;
               }                          */
               
               
             time=0;  
               
             for(int j=0; j<N; j++){
			    time+=c[j%C];
			 }  
             time=time*2;
             
             
			   
             if(L==0){;

					
			 }
             else if(L==1){
					max=last;
					for(int k=s; k<N; k++){
					 	if(c[k%C]>max){max=c[k%C];}
			//		cout<<"k= "<<k<<",max= "<<max<<endl;
					}
					time=time-max;
			 }
			 else if(L==2){
					max1=last;
					max2=0;
					
					for(int k=s; k<N; k++){
					 	if(c[k%C]>max1){max2=max1; max1=c[k%C]; }
					 	else if(c[k%C]>max2){max2=c[k%C];}
				//	cout<<"k= "<<k<<",c[k%C]= "<<c[k%C]<<endl; 	
				//	cout<<"max1= "<<max1<<",max2= "<<max2<<endl;
					}
					time=time-max1-max2;
										
					
			 }
			 
			 
			 
			 
			 
			 
	
	


      fout<<"Case #"<<i+1<<": "<<time<<endl;
  
      }
	
	
	

	
    system("PAUSE");
    return EXIT_SUCCESS;
}
