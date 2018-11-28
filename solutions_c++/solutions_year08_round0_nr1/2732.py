#include "SavingtheUniverse.h"

SavingtheUniverse::SavingtheUniverse()
{
	this->maxIndex = 0;
	this->lastEng = "";
}

SavingtheUniverse::~SavingtheUniverse()
{
}
string lastEng = "";

int SavingtheUniverse::maxNextIndex(string queries[], string eng[],int engines,int qry){
	int i,j;
	int max = 0;
	
	bool found = true;
	for(i = 0;i < engines;i++){
		for(j = this->maxIndex;j < qry;j++){
			if(eng[i] != lastEng){
				if(eng[i] == queries[j]){
					if(max < j){
						max = j;
						found = true;
						break;
					} else {
						found = true;
						break;
					}
				} else {
					found = false;
				}
			} else {
				break;
			}
		}
//		this->maxIndex = j;
		if(!found){
			max = qry;
			break;
		}
		
	}
	if(j >= qry){
		max = j;
	} else {
		lastEng = queries[max];
	}
	this->maxIndex = max+1;
	return max;
}

int SavingtheUniverse::getMinQuery(string queries[], string eng[],int engines,int qry){
	int result = 0;
	int i;
	int j;
	bool doesHave = false;
	if(qry != 0 && engines != 0){
		for(i = 0;i < engines;i++){
			for(j = 0;j < qry;j++){
				if(eng[i] == queries[j]){
					doesHave = true;
					break;
				} else {
					doesHave = false;
				}
			}
			if(!doesHave){
				break;
			}
		}	
		
		if(doesHave){
			int x = 0;
			while(x < qry){
				x = this->maxNextIndex(queries,eng,engines,qry);
				if(x < qry){
					result++;
				}
				cout << x << endl;
			}
		}
	}
	return result;
}

int main(){
	SavingtheUniverse *s = new SavingtheUniverse();
	fstream fIn;
	fstream fOut;
	fIn.open("A-small-attempt3.in",ios::in);
	fOut.open("test.out",ios::out);
	string buffer = "";
	getline(fIn,buffer);
	int entries = atoi(buffer.c_str());
	int engines = 0;
	int qry = 0;
	int i = 0;
	int cas = 1;
	while(entries > 0){
		getline(fIn,buffer);
		engines = atoi(buffer.c_str());
		string eng[engines];
		i = 0;
		while(i < engines){
			getline(fIn,buffer);
			eng[i] = buffer;
			i++;
		}
		getline(fIn,buffer);
		qry = atoi(buffer.c_str());
		string queries[qry];
		i = 0;
		while(i < qry){
			getline(fIn,buffer);
			queries[i] = buffer;
			i++;
		}
		s->maxIndex = 0;
		s->lastEng = "";
		if(cas == 5){
			int a = 0;
			a++;

		}
		int result = s->getMinQuery(queries,eng,engines,qry);
		fOut << "Case #" << cas << ": " << result << endl;
		entries--;
		cas++;
	}
	
	return 0;
}
