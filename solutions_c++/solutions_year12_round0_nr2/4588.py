#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int t = 0, //num test cases
        n = 0, //num googleers
        s = 0, //num sups
        p = 0; //number
    
    int tmp = 0;
    int pc = 0; //max score count
    int s_on = 2;
    
    vector<int> scores;
    
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    
    fin >> t;
    
    for(int i=0; i<t; i++){
        fin >> n;
        fin >> s;
        fin >> p;
        pc = 0; //reset
        
        scores.clear(); //empty score buff
        
        for(int g=0; g<n; g++){
            fin >> tmp;
            scores.push_back(tmp);
        }
        
        for(int g=0; g<n; g++){
            scores[g] = scores[g] - p;
            
            if(scores[g] < 0) continue;
            
            if( (scores[g] >= ((p*2)-2)) )// && (scores[g] <= ((p*2)+2+s_on)) )
            {
                ++pc;
            }
            else if( (scores[g] >= ((p*2)-4)) )//chk for sup
            {
                if(s > 0){
                    ++pc;
                    --s; //no more surprises
                }
            }
        }
        
        fout << "Case #" << i+1 << ": " << pc << endl;
    }
    
    //system("pause");
    
    fout.close();
    fin.close();
    return 0;
}
