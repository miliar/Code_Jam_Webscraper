#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip.h>
#include <string>
using namespace std;

int main(int argc, char *argv[]){
		//test
		string str[3], ans[3];
		str[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
		str[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
		str[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
		ans[0]="our language is impossible to understand";
		ans[1]="there are twenty six factorial possibilities";
		ans[2]="so it is okay if you want to just give up";
		char map[26];
		for (int i=0; i<3; i++){
				int len = str[i].length();
				const char* the_string = str[i].c_str();
				const char* the_answer = ans[i].c_str();
				for (int j=0; j<len+1; j++){
						//cout<<the_string[j]<<" "<<the_answer[j]<<endl;
						if (the_string[j]!=' ')
								map[the_string[j]-'a']=the_answer[j];
						//cout<<the_string[j]-'a'<<" <-> "<<the_answer[j]<<endl;
				}
		}	
		//cout<<"abcdefghijklmnopqrstuvwxyz"<<endl;
		map[16]='z';
		map[25]='q';
		for (int i=0; i<26; ++i){
				//cout<<char('a'+i)<<" "<<map[i]<<endl;
		}
		//return 0;
        ifstream ins;
        ins.open(argv[1]);
        int Ncase;
        ins>>Ncase;
        int the_case = 0;
		string zombie;
		getline(ins, zombie);
        while (the_case++ < Ncase){
				string input;
				getline(ins,input);
				const char* store=input.c_str();
				cout<<"Case #"<<the_case<<": ";
				for (int k=0; k<input.length(); ++k){
						if (store[k]!=' ')
								cout<<map[store[k]-'a'];
						else
								cout<<' ';
				}
				cout<<endl;
        }
        ins.close();
        return 0;
}

