#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
string real[]={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "};
string google[]={"y","h","e","s","o","c","v","x","d","u","i","g","l","b","k","r","z","t","n","w","j","p","f","m","a","q"," "};
int count=0;	
string l;
	ifstream myfile ("input.txt");
	if (myfile.is_open()){
		do{
			getline (myfile,l);
				if (l[0]=='3'){
				}
				else{
				int i=0;
				int G=0;
				while (G<l.size()){
					char *a=new char[google[i].size()+1];
					a[google[i].size()]=0;
					memcpy(a,google[i].c_str(),google[i].size());
					char b=*a;

					char *c=new char[real[i].size()+1];
					c[real[i].size()]=0;
					memcpy(c,real[i].c_str(),real[i].size());
					char d=*c;
					
					if (l[G]==d){
					  l[G]=b;
					  G++;
					  i=-1;
				
					}
					 i++;
				}
				count++;
				cout<<"Case #"<<count<<": "<<l<<endl;}
			}while (!myfile.eof());
	myfile.close();
			}
	 
system("pause"); 
return 0;
}