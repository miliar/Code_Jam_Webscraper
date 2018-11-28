#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ifstream ifile("data.txt");

    int p;
    ifile >> p;

    ofstream ofile("out.txt");
    for(int j=0;j<p;j++){
        int n,k;
        ifile >> n;
        ifile >> k;

        if(k%2==0){
            ofile << "Case #"<<j+1 <<": OFF"<<endl;
            continue;
        }

        vector<bool> vec(n,false);
 
        for(int i=0;i<k;i++){
			for(int m=0;m<k;m++){
	 	       if(vec[m]){
	    	       vec[m]=false;
	           }else{
	        	   vec[m]=true;
			       break;
	     	   }
			}
        }

        bool test=true;
        for(int i=0;i<vec.size();i++){
            if(!vec[i]){
                test=false;
                break;
            }
        }
        if(test){
            ofile << "Case #"<<j+1 <<": ON"<<endl;
        }else{
            ofile << "Case #"<<j+1 <<": OFF"<<endl;
        }

    }
    ofile.close();
    ifile.close();

    return 0;

}
