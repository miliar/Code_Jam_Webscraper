#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector> 
#include <fstream>
#include <string>
#include <map>


using namespace std;

int aTrains[2400];
int bTrains[2400];

class run {
      public:
      int dir; // A-B = 0, B-A = 1
      int leave;
      int arrive;
      run(int, int, int, int);
};

run::run(int a, int b, int c, int d) {
             dir =a;
             leave =b;
             arrive = c+d;
             if (arrive%100 >59) arrive += 40;
}

void reset(int a, int b) {
    // cout << "reset a=" << a << " b=" << b << endl;
     
     	for (int q = 0; q<2400; q++) {
        aTrains[q] = a;
        bTrains[q] = b;
        }
}

int train (int sta, int io, int time) {
    if (io == 0) { //add train
           if (sta == 0) {
                 //  cout << "a train adding at " << time <<endl;
                 //  getchar();
                   for (int i = time;i<2400;i++) {
                       aTrains[i]++;
                   }
           }
           else if (sta == 1) {
                   //cout << "b train adding at " << time <<endl;
                 //  getchar();
                  for (int j = time;j<2400;j++) {
                       bTrains[j]++;
                   }
           }
           return 0;
    }
    if (io == 1) { //sub train
    
           if (sta == 0) {
                   //cout << "a train leaving at " << time <<endl;
                   //cout << aTrains[time] << " trains in station" << endl;
                  // getchar();
                   if(aTrains[time]  == 0) return 1;
                   else
                   for (int i = time;i<2400;i++) {
                       aTrains[i]--;
                   }
                   return 0;
           }
           if (sta == 1) {
                   //cout << "b train leaving at " << time <<endl;
                   //cout << bTrains[time] << " trains in station" << endl;
                   //getchar();
                   if(bTrains[time]  == 0) return 1;
                   else
                   for (int i = time;i<2400;i++) {
                       bTrains[i]--;
                   }
                   return 0;
           }
    } 
                  
}

int timeToInt(string time) {
    int result = 0;    
    string abLine(time.begin(), time.begin() + time.find(":"));
    result = atoi(abLine.c_str())*100;
    string baLine(time.begin() + time.find_first_of(":")+1, time.end());
    result = result + atoi(baLine.c_str()); 
    return result;
}
  
    

int main() {
    
	//Opens file and prints to cout whether it succeeded/failed	
    string fName = "in.txt"; // **** INPUT FILE NAME HERE **** 		
    ifstream musicFile( fName.c_str() );	
    if (musicFile.fail() ) 
    {
	    //cout << "File not found" << endl;
	}
	//else cout << "Got the file" << endl << endl;
	
	string sLine;

	
	int nCases;
	int abCount;
	int baCount;
	
	int aNeed=0;
	int bNeed=0;
	
	int delay;
	
	
	ofstream myfile;
    myfile.open ("1_A_small_b.txt");

	
	
		getline(musicFile, sLine); //reads in file line by line
		nCases = atoi(sLine.c_str());
       // cout << nCases << " cases" << endl;
        
        for (int z = 0; z <nCases;z++) {
            myfile << "Case #" << z+1 << ": ";
            //myfile << "Case #" << z+1 << ": ";
           multimap<int, run> sched;
           
            getline(musicFile, sLine);
            delay = atoi(sLine.c_str());          
            //cout << delay << " min delay" << endl;   
            
            
            getline(musicFile, sLine);
            string abLine(sLine.begin(), sLine.begin() + sLine.find(" "));
            abCount = atoi(abLine.c_str());
            string baLine(sLine.begin() + sLine.find_first_of(" "), sLine.end());
            baCount = atoi(baLine.c_str()); 
            
           // cout << abCount << " ab trains, " << baCount << " ba trains" << endl;
            
            int leave;
            int arrive;
            
            for (int y = 0; y < abCount; y++) {
                getline(musicFile, sLine);
                string line(sLine.begin(), sLine.begin() + sLine.find(" "));
                leave = atoi(line.c_str());
                string lineb(sLine.begin() + sLine.find_first_of(" "), sLine.end());
                arrive = atoi(lineb.c_str());            
                //cout << "leave: " << timeToInt(line) << " arrive:" << timeToInt(lineb) << endl;
                run a(0, timeToInt(line), timeToInt(lineb), delay);
                sched.insert(pair<int, run>(timeToInt(line), a));
                //ab schedule
            }
            
            
            for (int y = 0; y < baCount; y++) {
                getline(musicFile, sLine);
                string line(sLine.begin(), sLine.begin() + sLine.find(" "));
                leave = atoi(line.c_str());
                string lineb(sLine.begin() + sLine.find_first_of(" "), sLine.end());
                arrive = atoi(lineb.c_str());            
               //cout << "leave: " << timeToInt(line) << " arrive:" << timeToInt(lineb) << endl;
                run a(1, timeToInt(line), timeToInt(lineb), delay);
                sched.insert(pair<int, run>(timeToInt(line), a));
                //ab schedule
            }
            
           // cout << "populated sched " << endl;
           // getchar();
            multimap<int, run>::iterator it = sched.begin(); 
            
            
            if ((*it).second.dir == 0) aNeed = 1;
            if ((*it).second.dir == 1) bNeed = 1;
            int res;
            
            reset(aNeed, bNeed);
            it = sched.begin();
            
          // cout << "starting while " << endl;                     
            while(1) {      
            res = train((*it).second.dir,1, (*it).second.leave);
            //cout << "res  " << res << endl;
            if (res) {
                     if((*it).second.dir) bNeed++;
                     else aNeed++;
                     reset(aNeed, bNeed);
                     it = sched.begin();
                     continue;
            }
            if((*it).second.dir) train(0,0,(*it).second.arrive);
            else train(1,0,(*it).second.arrive);
            
            it++;
            if (it == sched.end()) break;
            } 
            myfile << aNeed << " " << bNeed << endl;
            
            aNeed = 0;
            bNeed = 0;
            sched.clear();                            

        }
    getchar();
    //myfile.close();
    return 0;
}
