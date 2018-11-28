#include<vector>
#include<iostream>
#include<conio.h>
#include<string>
#include<algorithm>
#include<fstream>
#include<stdlib.h>

using namespace std;



int main( int argc, char* argv[])
{
    
    ifstream inf;
    //inf.open(argv[1]);
	inf.open("a3.in");
    ofstream outf;
    //outf.open( argv[2]);
	outf.open( "d2.in");
    
    char c;
    
    int total, caseno;
    const int size=200;
    char line[size];
    
    
    
//    while( inf)
  //  {
           inf>>total;
           caseno=0;
           
           
           
           
           
       while(total>caseno)
       {
                    //inf.getline(line, size);
                    //cout<<caseno<<" "<< line<<endl;      
                    //outf<<line<<endl;
                    //getch();
                  int noofse, noofqs;
                  
                  string ln;
                  
                  inf>>noofse;
                  
                  vector<string> sengs;
                  
                  sengs.clear();
                  
				  inf.getline(line, size);

                  for(int  n = 0 ; noofse> n; n++)
                  {
                       inf.getline(line, size);
                       ln = line;
                       sengs.push_back( ln);
                       }
				  

				  cout<< "search engines are"<<endl;
					
				  for(  n = 0 ; noofse> n; n++)
                  {
                       cout<<sengs[n]<<endl;
                       }

                  
                  
                  inf>>noofqs;
				  inf.getline(line, size);
                  vector<string> qs;
                  qs.clear();
                  
                  for( n = 0 ; noofqs> n; n++)
                  {
                       inf.getline(line, size);
                       ln = line;
                       qs.push_back( ln);
                       }

				  cout<< "qs are"<<noofqs<<endl;
					
				  for(  n = 0 ; noofqs> n; n++)
                  {
                       cout<<qs[n]<<endl;
                       }
				  
				
				vector<bool> longestesc;
				
				longestesc.clear();
                
                longestesc.resize( noofse);
                
                for(int i =0; i< longestesc.size(); i++)
                        longestesc[i] = true;
                
                int noofesc =0, swits=-1;
                
                 i=0; int j=0,k, currq=0;
                
                while( i < noofse && currq < noofqs)
                {
                       swits++;
                       
                       while(j < noofse && currq < noofqs)
                       {
                               
                               for( k=0; k<noofse; k++)
                               {
                                    if( qs[currq] == sengs[k])
                                    {
                                        if(longestesc[k]) j++;
                                        
                                        if( j<noofse)
                                            longestesc[k] = false;

										break;
                                        
                                        }
                                    
                                    }
                                    
                                    
                                    currq++;     
                               
                               }
                       
                       if ( j== noofse) currq--;

					   j=1;
                       
                       for( int l =0; l<noofse; l++)
                               {
                                    longestesc[l] = ! (longestesc[l]);
                                    }
                                             
                       }

				if(swits<0)
					swits =0;
                    
                    outf<<"Case #" << caseno+1<< ": "<< swits <<endl;
                    cout<<"Case #" << caseno+1<< ": "<<  swits <<endl;
                    
                    caseno++;
                          
					
                          }    
       
       //getch();
           
           
    inf.close();
    outf.close();
    
    
	return 0;    
    }
