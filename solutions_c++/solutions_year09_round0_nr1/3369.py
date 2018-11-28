#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <conio.h>

using namespace std;

typedef char* charPtr;

vector <string> allPatterns;
vector <string> Dict;

void findAllPattern(string pattern) {
    int i=0, j=1;
    if(pattern.size() == 0)
        return;
        
    int vecSize = allPatterns.size();
    
    if(pattern.at(i) == '('){
        while(pattern.at(j) != ')')
            j++;
        
        if(j-i>2) {       
            if(allPatterns.size() != 0) {     
                for(int k=0; k<j-i-2; k++)
                    for(int n=0;n<vecSize;n++)
                        allPatterns.push_back(allPatterns[n]);
                        
                for(i=1; i<j; i++)
                    for(int n=0;n<vecSize;n++)
                        allPatterns[n+(i-1)*vecSize].append(1,pattern.at(i));
            }
            else {
                for(i=1; i<j; i++){
                    string temp="";
                    temp.insert(temp.begin(),1,pattern.at(i));
                    allPatterns.push_back(temp);
                }
            }
        }
        
  /*      cout<<endl<<"before : patterns for the string : "<<pattern<<endl;
        cout<<"The total combinations of pattern are : "<< allPatterns.size()<<endl;
        for(int t=0; t<allPatterns.size(); t++)
            cout<<allPatterns[t]<<endl;
       */   
        int pIndex=0;
        while(pIndex < allPatterns.size()){  
            bool bMatched = true;              
            for(int dIndex=0; dIndex<Dict.size(); dIndex++){
                bMatched = true;
                for(int k=0;k<allPatterns[pIndex].size();k++){
                       if (allPatterns[pIndex].at(k) != Dict[dIndex].at(k)) {                            
                            bMatched = false;
                            break;
                        }
                    }
                    if(!bMatched)
                        continue;
                    else
                        break;                    
                }
                if(!bMatched) 
                    allPatterns.erase(allPatterns.begin()+pIndex);
                else 
                    pIndex++;
            }
        if(allPatterns.size() == 0)
            return;
 /*       cout<<endl<<"after : patterns for the string : "<<pattern<<endl;
        cout<<"The total combinations of pattern are : "<< allPatterns.size()<<endl;
        for(int t=0; t<allPatterns.size(); t++)
            cout<<allPatterns[t]<<endl;*/
            
        findAllPattern(pattern.substr(j+1));
        
    }
    else{
        while(pattern.at(j) != '(') {
            j++;
            if(j>=pattern.length())
                break;
        }
        if(vecSize == 0) {
                string temp=pattern.substr(i,j-i);
                allPatterns.push_back(temp);
        }
        else {
            for(i=0; i<j; i++) {            
                for(int n=0;n<vecSize;n++)
                    allPatterns[n].append(1,pattern.at(i));
            }
        }
        int pIndex=0;
        while(pIndex < allPatterns.size()){  
            bool bMatched = true;              
            for(int dIndex=0; dIndex<Dict.size(); dIndex++){
                bMatched = true;
                for(int k=0;k<allPatterns[pIndex].size();k++){
                       if (allPatterns[pIndex].at(k) != Dict[dIndex].at(k)) {                            
                            bMatched = false;
                            break;
                        }
                    }
                    if(!bMatched)
                        continue;
                    else
                        break;                    
                }
                if(!bMatched) 
                    allPatterns.erase(allPatterns.begin()+pIndex);
                else 
                    pIndex++;
            }
        if(allPatterns.size() == 0)
            return;
        findAllPattern(pattern.substr(j));
    }
}

int main(){
 
    int L, D, N;
    cin>>L>>D>>N;
    
    string temp;
    
    
    for(int i=0;i<D;i++){
        cin>>temp;
        while(temp.size() > L ) {
            Dict.push_back(temp.substr(0,L-1));
            temp = temp.substr(L);
        }
        Dict.push_back(temp);
        
    }
    sort(Dict.begin(),Dict.end());
    
       
    vector<string> pattern;
    
    for(int i=0;i<N;i++){
        cin>>temp;
        pattern.push_back(temp);
    }
    
    cout<<endl;
    
    for(int i=0;i<N;i++){
        allPatterns.clear();        
        findAllPattern(pattern[i]);
        
 /*       cout<<endl<<"patterns for the string : "<<pattern[i]<<endl;
        cout<<"The total combinations of pattern are : "<< allPatterns.size()<<endl;
        for(int j=0; j<allPatterns.size(); j++)
            cout<<allPatterns[j]<<endl;*/
        cout<<"Case #"<<i+1<<": ";
        
        sort(allPatterns.begin(),allPatterns.end());  
        int count=0;
        int dIndex=0;
        int j=0;
        
        while(j<allPatterns.size() && dIndex < Dict.size()){
                bool bMatched = true;
                for(int k=0;k<L;k++)
                    if (allPatterns[j].at(k) != Dict[dIndex].at(k)) {
                        if(allPatterns[j].at(k) < Dict[dIndex].at(k))
                            j++;
                        else if (allPatterns[j].at(k) > Dict[dIndex].at(k))
                            dIndex++;
                        bMatched = false;
                        break;
                    }
                if(bMatched){
                    j++;
                    dIndex++;
                    count++;
                }
            }
        
        cout<<count<<endl;
        
    }
    
    getch();
} 
