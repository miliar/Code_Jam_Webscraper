#include <iostream>
#include <stdlib.h>
#include <fstream>


using namespace std;

int recycle(int a,int b){
		if (b == 1){
			return (a % 10)*(a>99?100:10)+a/10;
		}
		else
			return (a % 100)*10+a/100;
	}
	
int main(){
    
    
    ifstream in("1.in");
    ofstream out("1.out");
    int N;
    
    in >> N;
    
    for(int i = 0;i<N;i++){
            int num = 0;
				int a,b;
				in >> a >> b;
				for(int j = a;j<b;j++){
					if (j<10)
						continue;
					else{
						if (recycle(j,1)>j && recycle(j,1)<=b){
							num++;
						}
						if (j>99 && recycle(j,2)>j && recycle(j,2)<=b)
                        {
							num++;
						}
					}
						
				}
            out << "Case #" <<i+1<<": "<<num<<endl;
    }    
}
