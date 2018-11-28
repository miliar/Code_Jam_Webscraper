#include <cstdlib>
#include <fstream>
#include <iostream>

using namespace std;
void printRPI(ofstream & ofile, int test, int teams_num, float * RPI)
{
     
     ofile<<"Case #"<< test<<":"<<endl;
     int team;
     for(team = 0; team<teams_num; team++)
     {
              ofile<<RPI[team]<<endl;
     }
}
int main()
{
    ifstream ifile;
    ifile.open("A-large.in");
    ofstream ofile;
     ofile.open("output.txt");
    int cases_num;
    ifile>>cases_num;
    int test;
    for(test =0; test<cases_num; test++)
    {
             int teams_num; ifile>>teams_num;
             char ** schedule = new char*[teams_num];
             int * games_num = new int[teams_num];
             int * wins_num = new int[teams_num];
             float * OWP = new float[teams_num];
             float * OOWP = new float[teams_num];
             float * RPI = new float[teams_num];
             int team;
             for(team = 0; team<teams_num; team++)
             {
                      schedule[team] = new char [teams_num];
                      games_num[team] = 0;
                      wins_num[team] = 0;
                      
                      char c;int opponent; 
                      for(opponent = 0; opponent<teams_num; opponent++)
                      {
                                   ifile>>c;
                                  
                                   schedule[team][opponent] = c;
                                   if(c == '1')
                                   {
                                        games_num[team]++;
                                        wins_num[team]++;
                                   }
                                   else if(c == '0')
                                   {
                                        games_num[team]++;
                                   }
                      }
             }
             
             for(team = 0; team<teams_num; team++)
             {
                      OWP[team] = 0;
                      int opponent; 
                      for(opponent = 0; opponent<teams_num; opponent++)
                      {
                                   if(schedule[opponent][team] == '1')
                                   OWP[team] = OWP[team] +  (float)(wins_num[opponent]-1)/ (float)(games_num[opponent]-1);
                                   else if(schedule[opponent][team] == '0')
                                   OWP[team] = OWP[team] +  (float)(wins_num[opponent])/ (float)(games_num[opponent]-1);     
                      }
                      OWP[team] = OWP[team]/games_num[team];
             }
             
             for(team = 0; team<teams_num; team++)
             {
                      OOWP[team] = 0;
                      float WP = (float)wins_num[team] / (float)games_num[team];
                      
                      int opponent;
                      for(opponent = 0; opponent<teams_num; opponent++)
                      {
                                   if(schedule[team][opponent] == '1')
                                   OOWP[team] = OOWP[team] +  OWP[opponent];
                                   else if(schedule[team][opponent] == '0')
                                   OOWP[team] = OOWP[team] +  OWP[opponent];     
                      }
                      OOWP[team] = OOWP[team]/games_num[team];
                      RPI[team] = 0.25 * WP + 0.5 * OWP[team] + 0.25 * OOWP[team];                      
             }
             printRPI(ofile, test+1, teams_num, RPI);
             delete games_num;
             delete wins_num;
             delete OWP;
             delete OOWP;
             delete RPI;
             for(team = 0; team<teams_num; team++)
             {
                      delete schedule[team];
             }
             delete [] schedule;
    }
    return EXIT_SUCCESS;
}
