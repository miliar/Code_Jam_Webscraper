#include <iostream>
#include <algorithm>
using namespace std;

char digit[300];

int main(){
    int cases;
    cin >> cases;
    int count = cases;
    cin.getline(digit, 300);  

    while(cases--){
        cin.getline(digit, 300); 

	bool check = false;
        for(int i = 0; i < strlen(digit)-1; i++){
	    if(digit[i] < digit[i+1]){
	        check = true;
		break;
	    }
        }

        if(check){
	for(int i = strlen(digit)-1; i >= 0; i--){
            char min = '0'+12;
            int point = i;	    
            for(int j = i+1; j < strlen(digit); j++)
	        if(digit[j] > digit[i] && digit[j] < min){
		    min = digit[j];	
		    point = j;
		}
	    if(min != ('0'+12)){
	        char tmp = digit[i];
		digit[i] = digit[point];
	        digit[point] = tmp;
	        sort(digit+i+1, digit+strlen(digit));
	        break;	
	    }
	}		 

        cout << "Case #" << count-cases << ": " << digit << '\n';
	}else{
	    int min = '0'+12;
	    int point = 0;
	    for(int i = 0; i < strlen(digit); i++)
	        if(digit[i] != '0' && digit[i] < min){
		    min = digit[i];
		    point = i;
		}
            digit[point] = '0';
	    sort(digit, digit+strlen(digit));
	    cout << "Case #" << count-cases << ": " << min << digit << '\n';    		
	}
    }

}
