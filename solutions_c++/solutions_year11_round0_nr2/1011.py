#include <iostream>
#include <string>
#include <vector>
#include <math.h>


using namespace std;

int main(){
    
	int max;
	cin >> max;
	
	for(int i = 0; i < max; i++){
        
        string elements, tempinput;
        vector<string> oppose;  int cc;
        vector<string> combine; int oc;
        
        
        cin >> cc;
        //input
        for(int j = 0; j < cc; j++){
            string temp;
            cin >> temp;
            combine.push_back(temp);
        }
        
        cin >> oc;
        //input
        for(int j = 0; j < oc; j++){
            string temp;
            cin >> temp;
            oppose.push_back(temp);
        }
        
        int max2;
        cin >> max2;
        
        cin >> elements;
        
        //cout << "H"; cout.flush();
        //cout << elements;
        //invoke
        for(int j = 2; j <= max2;){
            string tempstr = elements.substr(0,j);
            
            for(int k = 0; k < cc; k++){
                const char c[3] = {combine[k].data()[1], combine[k].data()[0], NULL};
                int compos = tempstr.find(combine[k].substr(0,2),0);
                if(compos == string::npos) 
                    compos = tempstr.find(c,0);
                if(compos != string::npos){
                    tempstr.replace(compos, 2, 1, combine[k].data()[2]);
                }
            }
            
            for(int k = 0; k < oc; k++){
                int compos = tempstr.find(oppose[k].substr(0,1),0);
                int compos2 = tempstr.find(oppose[k].substr(1,1),0);
                if(compos != string::npos && compos2 != string::npos) {
                    tempstr.clear();
                }
            }
            
            
            
            elements.replace(0, j, tempstr.data(), tempstr.length());
            j = tempstr.length() + 1;
			max2 = elements.length();
            
        }
        cout << "Case #" << i+1 << ": [";
        for(int k = 0; k < elements.length(); k++){
            cout << elements.substr(k,1);
            if(k + 1 != elements.length())  cout << ", ";
        }
        cout << "]" << endl;
	}
	
	return 0;
}