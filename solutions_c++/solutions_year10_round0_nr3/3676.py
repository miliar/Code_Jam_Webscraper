#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main(){


	string line; char* line1; char* l;
	
	ifstream myfile ("C-small-attempt0.in.txt");
	ofstream output ("C-small-attempt0.out.txt");
	
	getline (myfile,line); 
	
	line1 = new char [line.size()+1];
	strcpy (line1, line.c_str());
	
		
	int T = atoi(line1);
	
	delete[] line1;
	
	int cur = 0;
	
	while (cur<T) {
		
		getline (myfile,line); 
		line1 = new char [line.size()+1];
		strcpy (line1, line.c_str());
		
		l = strtok (line1 , " ");
		
		int R = atoi(l);
		
		l = strtok (NULL , " ");
		
		int k = atoi(l);
		
		l = strtok (NULL , " ");
		
		int N = atoi(l);
		
		delete[] line1;
		
		int* group = new int [N]; int i = 0;
		
		getline (myfile,line); 
		
		line1 = new char [line.size()+1];
		strcpy (line1, line.c_str());
		
		//////////
		
		l = strtok (line1 , " ");
		while (l)
		{
			group[i] = atoi(l);
			i++;
			l = strtok (NULL , " ");
			
		} delete[] line1;
		
		//***********CHECKING*********////
		/*cout << "T is " << T <<" R is " << R << " k is " << k << " N is " << N << endl;
		
		for (i=0; i<=N-1; i++) {
			cout << group[i] << endl;
		}
		
		//***********END CHECKING*********/////
		
		int this_ride = 0, total = 0, k_tmp = 0, latest_index = 0, sub_flag = 0;
		
		
		while (this_ride < R) {
			
			k_tmp = 0; 
			
			for (i=latest_index; k_tmp <= k; i++) {
				
				if(i > (N-1))
					i = i - (N-1) - 1;
				
				if(k_tmp && (i == latest_index))
				{sub_flag = 1; break;}
				
				k_tmp += group[i];
				
				
			} 
			
			if(!sub_flag){
				k_tmp = k_tmp - group[i-1]; 
				latest_index = i - 1;
			}else {
				latest_index = i ;
			}

			
			//cout << "this ride is " << this_ride << " k_tmp is "<< k_tmp<<endl; 
			//cout << "latest index is " <<latest_index <<endl;
			
			total+= k_tmp; this_ride++; 
			
		}
		
		output << "Case #" << cur+1 << ": " << total << endl;
		//cout << "Case #" << cur+1 << ": " << total << endl;
		
	cur++;
	}
	
	myfile.close();
	output.close();
	
	return 0;

}