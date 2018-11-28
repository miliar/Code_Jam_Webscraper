#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<fstream>

using namespace std;

int main(int argc,char *argv[]) {


	if(argc != 2)
		return 0;
	string cases;
	int casenum;
	ifstream ifs(argv[1]);
	vector<string> full_seq;
	if(ifs.is_open()) {
                  while(ifs.good()) {     
			string input;
			getline(ifs,input);
			full_seq.push_back(input);
                 }
                ifs.close();  
	}
	casenum = atoi(&(full_seq[0].at(0))); 
	int itr = 1; 
	while(itr <= (casenum)) {
		int num = atoi(&(full_seq[itr].at(0)));
		int time=0;
		int movement = 0;
		int opos=1;
		int bpos=1;
                int first_space = (int)full_seq[itr].find(" ",0);
		string useful_seq(full_seq[itr],(first_space + 1),full_seq[itr].length() - (first_space +1));
		int i=0;
		while(/*i <= (num*4 - 1)*/ 1) {
			int movetopos = atoi(&(useful_seq.at(i+2)));
                        //cout<<"movetopos is "<<movetopos<<endl;
			if(useful_seq.at(i) == 'O')  {
				if(movetopos >= opos)
					movement = movetopos - opos;
				else 
					movement = opos - movetopos;
				time = time + (movement);
				time++;
				opos = movetopos;
				size_t found = useful_seq.find('B',i+1);
				if(found != string::npos) {
					int pos = atoi(&(useful_seq.at(int(found) + 2)));
                                        int subtract;
                                        if(pos >= bpos)
                                           subtract = pos - bpos;
                                        else 
                                           subtract = bpos - pos;  
					if(subtract <= (movement+1))
						bpos = pos;
					else { 
                                                if(pos > bpos)
						    bpos += (movement + 1);
                                                 else if(pos < bpos)
                                                    bpos -= (movement + 1);
                                        } 

				}

			}  
			else if(useful_seq.at(i) == 'B')  {
				if(movetopos >= bpos)
					movement = movetopos - bpos;
				else
					movement = bpos - movetopos;
				time = time + movement;
				time++;
				bpos = movetopos;
				size_t found = useful_seq.find('O',i+1);
				if(found != string::npos) {
					int pos = atoi(&(useful_seq.at(int(found) +2 )));
                                        int subtract;
                                        if(pos >= opos)
                                           subtract = pos - opos;
                                        else 
                                           subtract = opos - pos;  
					if(subtract <= (movement+1))
						opos = pos;
					else {
                                                if(pos > opos)
						    opos += (movement + 1);
                                                 else if(pos < opos)
                                                    opos -= (movement + 1);
                                        }  
				}

			}
                        //cout<<"time is "<<time<<endl;
                        size_t space = useful_seq.find(" ",i+2);
                        if(space != string::npos)  
			    i = (int)useful_seq.find(" ",i + 2) + 1;
                        else 
                            break;
		}
		printf("Case #%d: %d \n",itr,time);
		itr++;
	}

	return 0;
}
