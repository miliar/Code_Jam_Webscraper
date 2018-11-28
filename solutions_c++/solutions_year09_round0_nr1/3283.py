#include <iostream>
#include <fstream>
#include <stdio.h>
#include <conio.h>
#include <vector>
#include <string>

using namespace std;

ifstream in("input.txt");
ofstream out("result.txt");

vector<string> word_list;
//vector<string> querry_list;

int L, D, N;

void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        lastPos = str.find_first_not_of(delimiters, pos);
        pos = str.find_first_of(delimiters, lastPos);
    }
}


int main (void) {
    
    vector<string> tokens;
    vector<int> check;
    vector<int> indice;
    
    in>>L>>D>>N;
    for (int i=0; i<D; i++) {
        string tmp;
        in>>tmp;
        word_list.push_back(tmp);
    }
    
    
    
    for (int i=0; i<N; i++) {
        int COUNT=0;
        int prod = 1;
        string tmp;
        in>>tmp;
        tokens.clear();
        indice.clear();
        check.clear();
        Tokenize(tmp, tokens, "()"); 
        size_t found;
        
        for (int j=0; j<tokens.size(); j++) {
            indice.push_back(0);
            found=tmp.find(tokens[j]);
            if (found==0) check.push_back(0);
            else if (tmp[(int)found-1]=='(') { check.push_back(tokens[j].size()); prod*=tokens[j].size(); }
            else check.push_back(0);
        }
        //cout<<"REZ -----------"<<tmp<<endl;   
        /*----varianta 2-----
        for (int k=0; k<D; k++) {
            bool bun = true;
            int t = 0;
            for (int m=0; m<word_list[k].size();) {
                bool flag=false;
                if (check[t]!=0) {
                   for (int p=0; p<tokens[t].size(); p++)
                       if (word_list[k][m]==tokens[t][p]) {
                          flag=true;
                          break;
                       }
                   if (flag) { m++; t++;}
                   else bun=false;
                }
                else {
                     int p;
                     for (p=0; p<tokens[t].size();) {
                         if (word_list[k][m]==tokens[t][p]) {
                            p++; m++; 
                         }     
                         else { bun=false; break;}
                     }
                     if (p==tokens[t].size()) t++;
                }
            }
        if (bun) COUNT++;
        cout<<word_list[k]<<" "<<COUNT<<endl;  
            
                                           
        }   */
        int flag=0;
        for (int k=0; k<word_list.size(); k++) {
            
            int litera=0;
            for (int m=0; m<tokens.size(); m++) {
                if (check[m]!=0) {
                   flag=0;
                   for (int p=0; p<tokens[m].size(); p++)
                       if (word_list[k][litera]==tokens[m][p]) flag++;
                   if (!flag) { flag = 0; break; } 
                   litera++;
                }
                else {
                   flag=0;
                   for (int p=0; p<tokens[m].size(); p++)
                       if (word_list[k][litera+p]==tokens[m][p]) flag++;
                   if (flag!=tokens[m].size()) {flag=0; break;}
                   litera+=tokens[m].size();
                }
            }
                if (flag) COUNT++;
        }
                
        
        out<<"Case #"<<i+1<<": "<<COUNT<<endl;
             
    }
    //for (int i=0; i<tokens.size(); i++) cout<<tokens[i]<<" "<<check[i]<<endl;        
    in.close();
    out.close();    
    
    return 0;    
}
