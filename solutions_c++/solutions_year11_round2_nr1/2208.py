#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <map>
#include <utility>

using namespace std;

class Stat{
      public:
      Stat();
      Stat(int id, int win, int total);
      
      int team_no;
      int win_games;
      int total_games;
};

Stat::Stat(){
}

Stat::Stat(int id, int win, int total){
    team_no = id;
    win_games = win;
    total_games = total;
}

void Func(vector<vector<int> > one_case){
     vector<double> Wps;
     //map<int, pair<int, int> > records;
     vector<Stat> records;
     for(int team=0; team<one_case.size(); team++){
         int total_games = 0;
         int win_games = 0;
         for(int col=0; col<one_case[team].size(); col++){
             if(one_case[team][col] == 1){
                 win_games++;
                 total_games++;
             }else if(one_case[team][col] == 0){
                 total_games++;
             }
         }
         Stat record(team, win_games, total_games);
         records.push_back(record);
         //pair<int, int> temp;
         //temp.first = win_games;
         //temp.second = total_games;
         //records[team].second = temp;
         double wp = float(win_games)/float(total_games);
         Wps.push_back(wp);
     }
     
     //compute OWP
     vector<double>OWps;
     for(int team=0; team<one_case.size(); team++){
         double new_WP = 0;
         double new_count = 0;
         for(int col=0; col<one_case[team].size(); col++){
             if((team!=col)&&(one_case[team][col]!=2)){
                  new_WP += float(records[col].win_games - one_case[col][team])/float(records[col].total_games-1);
                  new_count ++;
             }
         }
         double OWP = float(new_WP)/float(new_count);
         OWps.push_back(OWP);
     }
     
     //compute OOWP
     vector<double> OOWps;
     for(int team=0; team<one_case.size(); team++){
         double new_WP = 0;
         double new_count = 0;
         for(int col=0; col<one_case[team].size(); col++){
             if((team!=col)&&(one_case[team][col]!=2)){
                  new_WP += OWps[col];
                  new_count ++;
             }
         }
         double OWP = float(new_WP)/float(new_count);
         OOWps.push_back(OWP);
     }
     
     for(int team=0; team<one_case.size(); team++){
         cout.precision(10);
         double score = 0.25 * Wps[team] + 0.50 * OWps[team] + 0.25 * OOWps[team];
         cout<<score<<endl;
     }
     
}

int main(int argc, char* argv[]){
    // read-in input file and store all the data in the vector input_data
    ifstream inputfile (argv[1]);
   	string line;
	getline(inputfile,line);
	int case_no = atoi(line.c_str());
    int case_count  =0;

    getline(inputfile,line);
    int team_no = atoi(line.c_str());
    int count = 0;
    case_count ++;
    vector<vector<int> > data_table;
    vector<vector<vector<int> > > input_data;
	while(case_count<=case_no){ 
        if(count < team_no){
           getline(inputfile, line);
           vector<int> row;
           for(int i=0; i<line.length(); i++){
               if (line[i] == '.'){
                   row.push_back(2);
               }else if(line[i] == '1'){
                   row.push_back(1);
               }else{
                   row.push_back(0);
               }
           }
           data_table.push_back(row);
           count++;
        }else{
            /*for(int i=0; i<data_table.size(); i++){
                    for(int j=0; j<data_table[i].size(); j++){
                            cout<<data_table[i][j]<<"\t";
                    }
                    cout<<endl;
            }*/
            case_count++;
            getline(inputfile, line);
            team_no = atoi(line.c_str());
            
            count=0;
            input_data.push_back(data_table);
            data_table.clear();
        }
    }
    
    for(int case_index = 0; case_index<input_data.size(); case_index++){
        cout<<"Case #"<<case_index+1<<": "<<endl;
        Func(input_data[case_index]);
    }
    
    //system("pause");
   
}
