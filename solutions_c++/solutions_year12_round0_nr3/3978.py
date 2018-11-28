#include<iostream>
#include<string>
#include<cmath>
#include<sstream>
#include<set>
using namespace std;
int main()
      {
          int T,CASE=1;
          cin>>T;
          int A=0,B=0,ans,nRS;
          string SA,SSA,RS;
		  
          while(T--){
					
                     cin>>A>>B;					 
                     ans=0;
					cout<<"Case #"<<CASE<<": ";
					CASE++;
					 		  int minn=(A < 10 ? 1 :   
							(A < 100 ? 2 :   
							(A < 1000 ? 3 :   
							(A < 10000 ? 4 :   
							(A < 100000 ? 5 :   
							(A < 1000000 ? 6 :   
							(A < 10000000 ? 7 :  
							(A < 100000000 ? 8 :  
							(A < 1000000000 ? 9 :  
							10)))))))));
							int minnt=(int)pow(10.0,minn-1);
                     while(A < B){
								 stringstream st;
                                 st<<A;
                                 st>>SA;
                                 SSA=SA+SA;
								 set<int> t;
                                 for (int i=0;i<SA.length();i++)
                                 {
									
									 stringstream st1;
                                     st1<<SSA.substr(i,SA.length());
                                     st1>>nRS;
									 
									 if(nRS>minnt && nRS>A && nRS <=B){
									 t.insert(nRS);
										//ans++;
										}
                                  }
								  ans+=t.size();t.clear();
								  ++A;
                               
                               }
							   cout<<ans<<endl;
                     }
      return 0;
      }
