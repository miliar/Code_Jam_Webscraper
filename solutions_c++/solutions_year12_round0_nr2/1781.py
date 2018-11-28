#include<iostream>
#include<cmath>
#include <cstdlib>
using namespace std;
#include <fstream>





int main(int argc, char** argv) {

    int k, n,s,p,t,sur,num;
    char *buffer;
    buffer = new char[10];
    ifstream in;
    ofstream out;
    in.open("B-large.in", ios_base::in);
    out.open("output.txt", ios_base::out);
    
    
    if (in && out) {
        in>>buffer;
        cout<<buffer<<endl;
        //# cases
        k = atoi(buffer);
        cout<<k<<endl;
        for (int j = 0; j < k; j++) {
			sur=0;
		    num=0;
			in>>buffer;
			n = atoi(buffer);
			cout<<n<<endl;
			in>>buffer;
			s = atoi(buffer);
			cout<<s<<endl;
			in>>buffer;
			p = atoi(buffer);
			cout<<p<<endl;
			int* T=new int[n];
			for(int i=0;i<n;i++){
				in>>buffer;
			    T[i] = atoi(buffer);
			    cout<<T[i]<<"\t";
			}
			cout<<endl;
			
			
			for (int i=0;i<n;i++){
				if (T[i]%3==0 && T[i]/3>=p && T[i]/3>=0){
					num++;
					cout<<"yes"<<endl;
					
				}
				else if((T[i]+1)%3==0 && (T[i]+1)/3>=p && (T[i]+1)/3>=1){
					num++;
					cout<<"yes"<<endl;
					
				}
				else if((T[i]+2)%3==0 && (T[i]+2)/3>=p && (T[i]+2)/3>=1){
					num++;
					cout<<"yes"<<endl;
					
				}
				
				else if(sur<s && (T[i]+2)%3==0 && (T[i]+2)/3>=p && (T[i]+2)/3>=2){
					num++;
					sur++;
					cout<<"surprice"<<endl;
					
				}
				else if(sur<s && (T[i]+3)%3==0 && (T[i]+3)/3>=p && (T[i]+3)/3>=2){
					num++;
					sur++;
					cout<<"surprice"<<endl;
					
				}
				else if(sur<s && (T[i]+4)%3==0 && (T[i]+4)/3>=p && (T[i]+4)/3>=2){
					num++;
					sur++;
					cout<<"surprice"<<endl;
					
				}
			}			
            out<<"Case #"<<j+1<<": "<<num<<endl;
			//system("Pause");            
        }
		
    }
    in.close();
    out.close();
    system("Pause");
}
