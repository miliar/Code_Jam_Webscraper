#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;
struct Test{
	   string name;
	   int num;
	   Test(){num=0;}
};
int string_num(string& n){
	int k=0,j=n.size()-1,num=0;
	while(k<n.size() && j>=0){
		   num=num*10+(n[k]-'0');
 	   	   j--;
 	   	   k++;
  		}
	return num;
}
int main(){
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	string n,name;
	Test element;
	vector<Test> engin;
	vector<string> search;
	int num=0;
	getline(in,n);
	num=string_num(n);
	int i=1;
	while(i<=num){
         int sw=0;
		 string n1;
		 int m=0;
		 getline(in,n1,'\n');
		 m=string_num(n1);
		 int k=0;
		 while(k<m){
			getline(in,name,'\n');
			element.name=name;
			engin.push_back(element);
		    k++;
		   }
   		   getline(in,n1,'\n');
   		   m=string_num(n1);
   		   k=0;
		 while(k<m){
			getline(in,name,'\n');
			search.push_back(name);
			int j=0;
			bool nall=true;
			while(j<engin.size()){
	  		    if(engin[j].name==name){
					engin[j].num++;
					if(engin[j].num==1){
			  		   int f=0;
			  		   nall=false;
			  		   while(f<engin.size()){
   						   if(engin[f].num==0){
			   						nall=true;
			   						break;
						   }
			  			   f++;
					   }
					   if(!nall){
	   			 	      sw++;
	   			 	      f=0;
	   			 	      while(f<engin.size()){
  						      engin[f].num=0;
  						      f++;
						  }
						  engin[j].num=1;
					   }
			  		}
					  break;					
				}
				j++;
	  		}
	  		k++;
		 }	
		 out<<"Case #"<<i<<": "<<sw<<endl;
 		 i++;
 		 engin.clear();
 		 search.clear();
	 }
	
}
