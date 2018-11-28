#include <iostream>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <string>
#include <queue>

using namespace std;

int main(){
    // r = rides/day k = max passengers n = number of groups
    int r = 5; int k = 10; int n = 10; int cases = 0; int c = 0;
    size_t p, q;
    queue<int> rideline;
    string line = "";
    ifstream text ("C-small-attempt1.in");
    ofstream output ("output.txt");
    if(text.is_open()){
                       getline(text, line);
                       istringstream conv(line);
                       conv >> cases;
                       cout << "cases: " << cases << endl;
                       while(!text.eof()){
                       getline(text, line);
                       istringstream buff(line);
                       buff >> r;
                       buff >> k;
                       buff >> n;
                       getline(text, line);
                       istringstream buff2(line);
                       int temp = 0;
                       for(int i=0;i<n;i++){ 
                               buff2 >> temp;
                               rideline.push(temp);
                               }
                       int t = 0;
                       int money=0;
                       if(cases >= 1){
                       for(int i=0;i<r;i++){
                               t=k;
                               int cnt = 0;
                                   bool loopif = true;
                                        while(loopif){
                                        int temp = rideline.front();
                                        t-=temp;
                                        if(t<0 || cnt == rideline.size()){loopif = false;}
                                        else if(t>=0 && cnt<rideline.size()){
                                        rideline.pop();
                                        rideline.push(temp);
                                        money +=temp;
                                        cnt++;
                                        }//elseif
                                        }//while
                                        }//for
                                        cases--;
                                        while(!rideline.empty()){rideline.pop();}
                                        c++;
                                        cout << "=" << money << " " << c << endl;
                                        output << "Case #" << c << ": " << money << endl;
                       }}
                       text.close();
         }
    cin.get();
}
