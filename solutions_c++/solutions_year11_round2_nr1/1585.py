# include <iostream>
# include <cstdio>
# include <algorithm>
# include <vector>
# include <fstream>

using namespace std;


    ifstream in("A-large.in");
    ofstream out("output.txt");

void calculateRPI(const vector<string> &matrix){
       
       double WP[101]={0.0}, OWP[101]={0.0}, OOWP[101]={0.0}, RPI[101]={0.0};
       double won[101]={0}, played[101] = {0};
       
       for(int i = 0; i < matrix.size(); ++i){
               for(int j = 0; j < matrix[i].size(); ++j){
                         if(matrix[i][j] != '.'){
                                         played[i]++;
                                         
                                         if(matrix[i][j]=='1'){
                                                               won[i]++;
                                              }
                              }                              
                       }
                       if(played[i])
                       WP[i] = (double)(won[i]/played[i]);
               }
               
               //OWP
               for(int i = 0; i < matrix.size(); ++i){
                       for(int j = 0; j < matrix[i].size(); ++j){
                               if(matrix[i][j] != '.'){
                                               if(matrix[i][j] == '1'){
                                                               if(played[j]-1 > 0)
                                                               OWP[i]+=((won[j])/(played[j]-1));
                                                    }
                                               else {
                                                               if(played[j]-1 > 0 && won[j]-1 > 0)
                                                               OWP[i]+=((won[j]-1)/(played[j]-1));
                                                    }
                                    }
                               }                              
                               if(played[i])
                               OWP[i]/=(played[i]);
                       }
       
               //OOWP
               for(int i = 0; i < matrix.size(); ++i){
                       int played = 0;
                       for(int j = 0; j < matrix.size(); ++j){
                               if(matrix[i][j] != '.'){
                                               OOWP[i]+=(OWP[j]);
                                               played++;
                                    }
                               }
                               if(played)
                               OOWP[i]/=played;
                       }
       
                       for(int i = 0; i<matrix.size(); ++i){
                               out<<(0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);                              
                               if(i != matrix.size() -1 ){
                                       out<<endl;
                                    }
                               }   
       
       }

int main()
{
    
    int T, cas = 0;
    in>>T;
    
    while(T--){
               int N;
               in>>N;
               
               string row;
               vector<string> matrix;
               
               while(N--){
                          in>>row;
                          matrix.push_back(row);
                          }
                                                        
               out<<"Case #"<<++cas<<": "<<endl;
               calculateRPI(matrix);
               out<<endl;
               }
 
 return 0;   
}
