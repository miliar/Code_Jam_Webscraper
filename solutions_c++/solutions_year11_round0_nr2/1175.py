#include <string>
#include <stdio.h>
#include <map>
#include <set>
#include <iostream>
#include <algorithm>
#include <vector>

#define STRINGLENGTH 101

using namespace std;

void process_str(map<char, char>& combineKey, map<string, char>& combine, map<char, char>& oppose, string& str, vector<char>& eleList) {
	int i = 0, length = str.length();
	string tmp;
	vector<char>::iterator iter;
	while( i < str.length()) {
		eleList.push_back(str[i]);

		if(combineKey.find(str[i]) != combineKey.end()) {
			//iter = find(eleList.begin(), eleList.end(), combineKey[str[i]]);
			if(eleList.size() >= 2 && eleList[eleList.size() -  2] == combineKey[str[i]]) {
				string temp;
				temp.assign(1, str[i]); temp.append(1, combineKey[str[i]]);
				eleList.pop_back(); eleList.pop_back();
				eleList.push_back(combine[temp]);
			}
		}

		if(oppose.find(eleList[eleList.size() -1]) != oppose.end()) {
			iter = find(eleList.begin(), eleList.end(), oppose[str[i]]);
			if(iter != eleList.end())
				eleList.clear();
		}

		i++;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* ifile = fopen("B-small-attempt0.in", "r");
	if(ifile == NULL) {
		printf("open file error!");
		return -1;
	}
	FILE* out = fopen("out", "w");

	int recordNo;
	fscanf(ifile, "%d", &recordNo);
	printf("Record: %d\n", recordNo);

	int i = 1;
	map<string, char> combine;
	map<char, char> combineKey;
	map<char, char> oppose;
	int combineNo, opposeNo;
	char temp[STRINGLENGTH];
	int strLen;
	vector<char> eleList;

	while( i <= recordNo) {
		combine.clear();
		oppose.clear();
		eleList.clear();
		combineKey.clear();
		fscanf(ifile, "%d", &combineNo);
		int j = 0;
		while(j < combineNo) {
			fscanf(ifile, "%s", temp);
			string tempStr(temp, 2);
			combine[tempStr.c_str()] = temp[2];
			tempStr.assign(1, temp[1]);
			tempStr.append(1, temp[0]);
			combine[tempStr] = temp[2];
			combineKey[temp[0]] = temp[1];
			combineKey[temp[1]] = temp[0];
			j++;
		}

		fscanf(ifile, "%d", &opposeNo);
		j = 0;
		while(j < opposeNo) {
			fscanf(ifile, "%s", temp);
			//oppose.insert(temp);
			oppose[temp[1]] = temp[0];
			oppose[temp[0]] = temp[1];
			j++;
		}

		fscanf(ifile, "%d", &strLen);
		fscanf(ifile, "%s", temp);

		string msg(temp, strLen);
		process_str(combineKey, combine, oppose, msg, eleList);

		printf("%s\n", msg.c_str());

		fprintf(out, "Case #%d: [", i);
		
		size_t k;
		for(k = 0; k < eleList.size(); k++) {
			if( k < eleList.size() -1) 
				fprintf(out, "%c, ", eleList[k]);
			else
				fprintf(out, "%c", eleList[k]);
		}
		//cout<<k<<msg.length()<<endl;
		//if(msg.length() == 0) {
		fprintf(out, "]\n");
		i++;
	}

	return 0;
}

