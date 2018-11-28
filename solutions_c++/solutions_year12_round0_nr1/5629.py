#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int array_mapping[27] = {};
    char line;
    ifstream fp;
    fp.open("input");
    int i=1;

    array_mapping[1]=25;
    array_mapping[2]=8;
    array_mapping[3]=5;
    array_mapping[4]=19;
    array_mapping[5]=15;
    array_mapping[6]=3;
    array_mapping[7]=22;
    array_mapping[8]=24;
    array_mapping[9]=4;
    array_mapping[10]=21;
    array_mapping[11]=9;
    array_mapping[12]=7;
    array_mapping[13]=12;
    array_mapping[14]=2;
    array_mapping[15]=11;
    array_mapping[16]=18;
    array_mapping[17]=26;
    array_mapping[18]=20;
    array_mapping[19]=14;
    array_mapping[20]=23;
    array_mapping[21]=10;
    array_mapping[22]=16;
    array_mapping[23]=6;
    array_mapping[24]=13;
    array_mapping[25]=1;
    array_mapping[26]=17;
   
 
    if(!fp) return 1; 
    	
	while((line = fp.get()) != EOF) {       
	       	if (line == '\n'){
                        cout << "\n";
			cout << "Case #" ;
			cout << i++;
                        cout << ": ";
                    
		}else if (line >= 97 && line <= 122 ) {
		        int temp = array_mapping[line-96]+96;
		        line = char(temp);
	       		cout << line;
		}else if (line >= 48 && line <= 57) {
                }else {
		        cout << line;
		}
       }
   fp.close(); 
   return 0;   
}

