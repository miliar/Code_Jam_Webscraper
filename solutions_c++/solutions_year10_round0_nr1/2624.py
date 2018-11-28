#include <cmath>
#include <fstream>
#include <iostream>

using namespace std;

int case_num;

void pause()
{
		char s;
		cin >> s;
}

int parse_file(char *file_name)
{
		//open file
		fstream fin;
		fin.open(file_name,fstream::in);

		//output file
		fstream fout;
		fout.open("result.txt",fstream::out);
		
        //read variables
        fin >> case_num;
        
        //do cases
        int case_now=1;
        int k,n;
        while( case_now <= case_num ){
               fin >> n >> k;
               //cout << case_now << "-> " << n << ":" << k << endl;
               int temp = k % int(( pow(2,double(n)) ));
               //cout << "dsf" << temp << endl;
               bool result = ( temp == int(( pow(2,double(n)) )) -1 );
               //if( result )
               //cout << "ON" << endl;
               //else
               //cout << "OFF" << endl;
               
               //to file
               if( result )
               fout << "Case #" << case_now << ": ON" << endl;
               else
               fout << "Case #" << case_now << ": OFF" << endl;
               
               case_now++;
        }
                                		
                                        
                        
        //close file
		fin.close();
		fout.close();
        return 0;	
}
    
int main()
{
	char s[3];
	//parse_file("A-small-attempt0.in");
	//parse_file("A-large-practice.in");
    //parse_file("test.txt");
    parse_file("A-large.in");
	pause();
	return 0;
}
