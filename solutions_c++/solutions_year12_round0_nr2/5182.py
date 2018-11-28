#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
    ifstream inputFile("input");
    string line;
    int l=1;
    
    getline(inputFile, line);
    
    while (getline(inputFile, line))
    {
        istringstream ss(line);

       
        int total_players,surprising_events, score;
        int best_players=0;

        ss >>  total_players >> surprising_events >> score; 
        int scores[10];
        int normal=0;
        int normal_best;
        int surprising_best;
        if ((score-1)>0){
            normal_best=(score-1)*2+score;
        }else {                       
            normal_best = score;
	}

        if ((score-2)>0){
		surprising_best=((score -2)*2+score);
	}else {
		surprising_best=score;
	}

        for(int i=0;i<total_players;i++){
        	ss >> scores[i];      
          
                if ( normal_best<= scores[i]){
                        ++best_players;
                }else if( surprising_best<= scores[i]) {
                    if((surprising_events - 1) >= 0) {
                        surprising_events--;
                        ++best_players;
                    }
                }                                
        }  
cout << "\nCase #"; 

cout << l++;
cout << ": "   ;    


cout << best_players;

       
    }
}
