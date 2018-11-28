/*
 * robots.cpp
 *
 *  Created on: 2011-5-6
 *      Author: sky
 */

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include "robots.h"
using namespace std;
void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}
void readindata(string line, vector<task*> &orange,vector<task*> &blue,vector<string> &orders){
	vector<string> temp;
	Tokenize(line,temp," ");
	int order=1;
	for (int i=1;i<temp.size();i=i+2){
		if(temp[i]=="B"){
			orders.push_back("B");
			task* temptask=new task(order++,atoi(temp[i+1].c_str()));
			blue.push_back(temptask);
		}
		if(temp[i]=="O"){
			orders.push_back("O");
			task* temptask=new task(order++,atoi(temp[i+1].c_str()));
			orange.push_back(temptask);
		}
	}

}
void calculate_timespan(vector<task*> &container){
	if(container.size()==0) return;
	container[0]->timespan=container[0]->position-1;
	for(int i=1;i<container.size();i++){
		container[i]->timespan=abs(container[i]->position-container[i-1]->position);
	}
}
int accumulate(vector<task*> orange, vector<task*> blue,vector<string> orders){
	int total=0;
	string pre_color;
	int pre_span=0;
	int blue_track=0;
	int orange_track=0;
	if(orders[0]=="O"){
		total=orange[0]->timespan+1;
		orange_track++;
		pre_color="O";
		pre_span=orange[0]->timespan+1;
	}
	if(orders[0]=="B"){
		total=blue[0]->timespan+1;
		blue_track++;
		pre_color="B";
		pre_span=blue[0]->timespan+1;
	}
	for(int i=1;i<orders.size();i++){
		if(orders[i]==pre_color){
			if(orders[i]=="B"){
				pre_span=pre_span+blue[blue_track]->timespan+1;
				total=total+blue[blue_track]->timespan+1;
				blue_track++;
				continue;
			}
			if(orders[i]=="O"){
				pre_span=pre_span+orange[orange_track]->timespan+1;
				total=total+orange[orange_track]->timespan+1;
				orange_track++;
				continue;
			}
		}
		else{
			if(orders[i]=="B"){
				if(blue[blue_track]->timespan<=pre_span){
					pre_span=1;
					total=total+1;
					pre_color="B";
					blue_track++;
					continue;
				}
				if(blue[blue_track]->timespan>pre_span){
					pre_span=blue[blue_track]->timespan-pre_span+1;
					total=total+pre_span;
					pre_color="B";
					blue_track++;
					continue;
				}
			}
			if(orders[i]=="O"){
				if(orange[orange_track]->timespan<=pre_span){
					pre_span=1;
					total=total+1;
					pre_color="O";
					orange_track++;
					continue;
				}
				if(orange[orange_track]->timespan>pre_span){
					pre_span=orange[orange_track]->timespan-pre_span+1;
					total=total+pre_span;
					pre_color="O";
					orange_track++;
					continue;
				}
			}

		}
	}
	return total;
}
int main(){
	string line;
	int linenumber=0;
	ifstream ifile("new");
	while(getline(ifile,line)){
		if(linenumber==0) {linenumber++;continue;}
		vector<task*> orange;
		vector<task*> blue;
		vector<string> orders;
		readindata(line,orange,blue,orders);
		calculate_timespan(orange);
		calculate_timespan(blue);
		int seconds=accumulate(orange,blue,orders);
		cout<<"Case #"<<linenumber<<": "<<seconds<<endl;
		linenumber++;
	}

return 1;
}
