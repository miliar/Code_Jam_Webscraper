#include<iostream>
#include<cmath>
#include <cstdlib>
using namespace std;
#include <fstream>

char* circle(char* m,int size,int &times){
	char temp=m[size-2];
	char* B=new char[size];
	for(int i=0;i<size;i++)
		B[i]=m[i];
	times++;
	if(size>2){
		for(int i=size-3;i>=0;i--){
			B[i+1]=B[i];
		}
		B[0]=temp;			
		if(temp=='0'){
			B=circle(B,size,times);
		}
	}
}



int main(int argc, char** argv) {

    int k, n,m,m1,pairs;
    char *buffer;
    char *A;
    char *B;
    char *B1;
    buffer = new char[10];
    ifstream in;
    ofstream out;
    in.open("C-large.in", ios_base::in);
    out.open("output.txt", ios_base::out);
    
    
    if (in && out) {
        in>>buffer;
        //cout<<buffer<<endl;
        //# cases
        k = atoi(buffer);
        //cout<<k<<endl;
        for (int j = 0; j < k; j++) {
			A=new char[10];
    		B=new char[10];
			pairs=0;
			in>>A;
			n = atoi(A);
			//cout<<n<<endl;
			in>>B;
			m = atoi(B);
			//cout<<m<<endl;
			
			int size;
			int times=0;
			for(size=0;B[size]!='\0';size++);
			//cout<<"size: "<<size<<endl;
			while(n<m){
			
				while(times<size){
					B1=circle(B,size+1,times);
					m1=atoi(B1);
					//cout<<"m1: "<<m1<<" times: "<<times<<endl;
					if(times<size && m1<m && m1>=n){
						pairs++;
						//cout<<pairs<<"------------------------------------->pairs"<<endl;
					}
					B=B1;
					if(m1==m)
					break;
				}
				m--;
				itoa(m,B,10);
				//cout<<B<<"---->B"<<endl;
				
				times=0;
				//if(m%50==0)
				//system("Pause");	
			}		 
            out<<"Case #"<<j+1<<": "<<pairs<<endl;
			//system("Pause");            
        }
		in.close();
    	out.close();
    }    
    system("Pause");
}
