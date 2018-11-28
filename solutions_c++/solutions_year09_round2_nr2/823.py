#include<iostream>
#include<algorithm>
#include <iostream>
#include <fstream>

using namespace std;



int main(){
    ifstream input;
    input.open("b.in");
    ofstream output;
    output.open("b.out");
  
    int T;     
    input>>T;
    
    for(int xxx=1; xxx<=T; xxx++){
            string s;
            input>>s;
            int here = s.size()-1;
    
            while( here>0 && s[here-1]>=s[here])
                   here--;
                                        
            if(here==0){
                        s="0"+s;
                        here =1;
                        }

            int min=here;
            for(int i=here+1; i<s.size(); i++)
                    if(s[here-1]<s[i] && s[i]<s[min])
                        min=i;
                         
            swap(s[here-1],s[min]);
            sort(s.begin()+here,s.end());
    
            output<<"Case #"<<xxx<<": "<<s<<endl;
            }
  //  system("pause");                                                             
    
    return 0;
}

