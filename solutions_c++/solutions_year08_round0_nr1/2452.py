#include <iostream>  
#include <algorithm>  
#include <cstring>  
#include <cstdlib>  
#include <vector>  
#include <string>  
 
using namespace std;

int main()
{      
       int MAX_LENGTH = 100;
       char line[MAX_LENGTH];
       
       int n;   
       cin>>n;
       cin.getline(line, MAX_LENGTH);

       for(int ci=0;ci<n;ci++){

	       int serch_num=0;
	       cin>>serch_num;
 	       cin.getline(line, MAX_LENGTH);
               vector<string> serch_name;

	       for(int ser=0;ser<serch_num;ser++){
                       cin.getline(line, MAX_LENGTH);
                       serch_name.push_back(line);
               } 




	      int arry[serch_num];
              memset(arry,0,sizeof(arry)); 
	 
           

              int query_num;
	      cin>>query_num;
	      cin.getline(line, MAX_LENGTH);
              vector<string> query_name;


	      for(int ser=0;ser<query_num;ser++){
                       	cin.getline(line, MAX_LENGTH);
			if(query_name.empty())
				query_name.push_back(line);
                       	else if(line!=*(query_name.end()-1)){ 
				query_name.push_back(line);
			}
               }     

		
	      
	      if(query_num==0 or serch_num==1)
			cout<<"Case #"<<ci+1<<": "<<"0"<<endl;               

	      else  {
			
			int st=0;
			string s,s1,temp;

			vector<string>::iterator  mark,l,m,p=query_name.begin();
              		while(p!=query_name.end()){
				l=find(serch_name.begin(),serch_name.end(),*p);
				
				m=p;
				p++;
				int sum=0;
				if(arry[l-serch_name.begin()]!=1){ 
					arry[l-serch_name.begin()]=1;
              				for(int j=0;j<serch_num;j++){
						sum+=arry[j];			
					}
				}
			
				if(sum==serch_num-1){	mark=m;}	
				temp=s;
				if(sum==serch_num){   
					s=*m;								
					if(temp!=s){
						st+=1;
				       		memset(arry,0,sizeof(arry)); 
						query_name.erase(query_name.begin(),m);
						p=query_name.begin();
					}
					if(temp==s){
						st+=1;
						memset(arry,0,sizeof(arry));
						query_name.erase(query_name.begin(),mark);				
				        	p=query_name.begin();
					}	
				}
                        }
			int sum=0;
              		for(int j=0;j<serch_num;j++){
				sum+=arry[j];			
			}
			if(sum==serch_num-1 and temp==s){
				if(find(query_name.begin(),query_name.end(),s1)!=query_name.end())  st+=1;}
			if(sum==serch_num-1 and temp!=s){
				if(find(query_name.begin(),query_name.end(),s1)!=query_name.end())  st+=1;}
						
			cout<<"Case #"<<ci+1<<": "<<st<<endl;	
	       }
                      
               

	 }



     return 0; 
 }
